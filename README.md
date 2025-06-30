# 🎥 YouTube Video Summarizer with Gemini AI

This is a Streamlit-based web app that generates **detailed summaries** from any YouTube video's transcript using **Gemini Pro (Google Generative AI)**.

It extracts the transcript of the video and feeds it to Gemini to create a concise summary in bullet points — great for quick learning, revision, or note-taking!

---

## ✨ Features

- 🔗 Paste a YouTube video link and get an instant summary.
- 🧠 Uses **Google's Gemini Pro** LLM to generate high-quality notes.
- 📝 Summarizes transcripts into ~200–250 word bullet points.
- 📺 Supports full YouTube and short `youtu.be` links.
- 🖼️ Displays the video thumbnail for context.
- ⚡ Built with Streamlit — easy to deploy and use.

---


## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini Pro)](https://ai.google.dev/)
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🧪 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/youtube-summarizer.git
cd youtube-summarizer

2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

3. Create .env file
Add your Gemini API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
4. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py


