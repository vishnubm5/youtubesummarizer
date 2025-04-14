import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

# Load environment variables
load_dotenv()

# Configure Gemini AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for Gemini AI
prompt = """You are a YouTube Video Summarizer. 
You will be taking the transcript text and summarizing the entire video 
and providing the important summary in points within 200 or 250 words. 
Please provide the summary here: 
"""

# Function to extract video ID safely
def get_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if parsed_url.netloc in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]
    elif parsed_url.netloc in ["youtu.be"]:  # For shortened URLs like youtu.be/xyz123
        return parsed_url.path.lstrip("/")
    return None

# Function to extract transcript from YouTube
def extract_transcript_details(youtube_video_url):
    try:
        video_id = get_video_id(youtube_video_url)
        if not video_id:
            return None, "Invalid YouTube URL. Please check and try again."
        
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = " ".join([i['text'] for i in transcript_text])
        return transcript, None

    except Exception as e:
        return None, str(e)

# Function to generate summary using Gemini AI
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit UI
st.title("YouTube Transcript to Detailed Notes Converter")

youtube_link = st.text_input("Enter the YouTube Video URL")

if youtube_link:
    video_id = get_video_id(youtube_link)
    if video_id:
        st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
    else:
        st.error("Invalid YouTube URL. Please check and try again.")

if st.button("Get Detailed Notes"):
    transcript_text, error = extract_transcript_details(youtube_link)

    if error:
        st.error(f"Error: {error}")
    elif transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes")
        st.write(summary)
    else:
        st.error("Could not retrieve transcript. Please check the video URL or try again later.")
