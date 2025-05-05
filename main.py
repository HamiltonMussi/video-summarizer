import os
from video import Video
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
system_prompt = "You are an assistant that analyzes the transcription of a Youtube video \
and provides a short summary"

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

openai = OpenAI()

def create_user_prompt(video: Video):
    user_prompt = f"You are looking at a transcription of a Youtube video."
    user_prompt += "\nThe transcription of this video is as follows; \
    please provide a short summary of this video. \
    \n\n"
    user_prompt += video.transcription
    return user_prompt

def create_messages(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": create_user_prompt(website)}
    ]

def get_summary(url: str):
    video = Video(url)
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = create_messages(video)
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    url = input("Type the URL of the Youtube video you want to summarize: ")
    summary = get_summary(url)
    print("\nVideo summary:\n")
    print(summary)