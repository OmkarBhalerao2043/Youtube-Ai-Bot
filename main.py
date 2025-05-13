import streamlit as st
import openai
import os
from dotenv import load_dotenv

from youtube_api import search_youtube
from ai_analyzer import analyze_titles_with_gpt
from utils import extract_titles, extract_urls

# Load API keys from .env
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Streamlit UI
st.set_page_config(page_title="YouTube AI Video Finder", page_icon="🎬")
st.title("🎯 YouTube Video Finder with AI")
st.write("Enter a topic to find the most relevant video using YouTube + ChatGPT.")

query = st.text_input("🔎 What are you searching for?", "")

if st.button("Find Best Video") and query:
    with st.spinner("Searching YouTube..."):
        videos = search_youtube(query, YOUTUBE_API_KEY)
        if not videos:
            st.error("No suitable videos found.")
        else:
            titles = extract_titles(videos)
            urls = extract_urls(videos)

            st.success("✅ Videos found! Analyzing with AI...")
            best = analyze_titles_with_gpt(titles)

            st.subheader("📺 All Filtered Videos")
            for title, url in zip(titles, urls):
                st.write(f"- [{title}]({url})")
