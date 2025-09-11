import os
# Force Python to know FFmpeg path
os.environ["PATH"] += os.pathsep + r"C:\Users\seq_rincy\Downloads\ffmpeg-8.0-essentials_build\ffmpeg-8.0-essentials_build\bin"
 
import whisper

model = whisper.load_model("base")  # load once at startup

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']
