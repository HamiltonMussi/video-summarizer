import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url: str):
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    if match:
        return match.group(1)
    else:
        return None
    
def extract_video_transcription(url: str):
    video_id = extract_video_id(url)
    transcription = YouTubeTranscriptApi.get_transcript(video_id)
    full_transcription = " ".join([item['text'] for item in transcription])
    return full_transcription

class Video: 
    def __init__(self, url):
        self.transcription = extract_video_transcription(url)
        
        

    