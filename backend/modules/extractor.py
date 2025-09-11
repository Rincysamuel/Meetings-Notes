import re

def extract_action_items(text):
    action_keywords = [
        "schedule", "prepare", "send", "review", "assign",
        "update", "follow up", "finalize", "complete", "submit"
    ]
    
    sentences = re.split(r'(?<=[.!?])\s+', text)
    action_items = []

    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in action_keywords):
            action_items.append(sentence.strip())

    return action_items if action_items else ["No action items found."]
