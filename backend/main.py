from fastapi import FastAPI, UploadFile, File
import shutil
import os
from backend.modules.transcriber import transcribe_audio

from backend.modules.summarizer import summarize_text
from backend.modules.extractor import extract_action_items

app = FastAPI()
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcript = transcribe_audio(file_path)
    summary = summarize_text(transcript)
    action_items = extract_action_items(transcript)

    return {
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items
    }
