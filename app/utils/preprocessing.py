import re

def load_comments_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        comments = f.readlines()
    return [c.strip() for c in comments if c.strip()]

def clean_comment(text):
    # remove URLs, emojis, special characters, extra spaces
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r"[^\w\s,.!?]", '', text)          
    text = re.sub(r"\s+", " ", text)                     
    return text.strip()
    
def preprocess_comments(file_path):
    raw_comments = load_comments_from_txt(file_path)
    cleaned = [clean_comment(c) for c in raw_comments]
    return cleaned
