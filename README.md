🎯 YouTube AI Video Finder Bot

Find the best YouTube video for any topic using YouTube API + OpenAI GPT.
Project GitHub Repo: https://github.com/OmkarBhalerao2043/Youtube-Ai-Bot

✅ Features

* Search YouTube videos (last 14 days)
* Filter videos by duration (4 to 20 mins)
* Use ChatGPT (GPT-4o) to choose the best video title
* Show result in simple Streamlit app

🛠️ Setup Instructions

1. Clone this repo

```bash
git clone https://github.com/OmkarBhalerao2043/Youtube-Ai-Bot.git
cd Youtube-Ai-Bot
```

2. Install required packages

```bash
pip install -r requirements.txt
```

3. Add API keys
   Create a `.env` file and paste:

```
YOUTUBE_API_KEY=your_youtube_api_key
OPENAI_API_KEY=your_openai_api_key
```

4. Run the app

```bash
streamlit run main.py
```

---

📁 Files in This Project

* `main.py` → Full Streamlit app (YouTube + GPT logic)
* `requirements.txt` → All Python packages needed
* `.env` → Your API keys (not pushed to GitHub)

---

📦 Main Requirements

* Python 3.8+
* streamlit
* openai
* requests
* isodate
* python-dotenv

Install with:

```bash
pip install streamlit openai requests isodate python-dotenv
```

---

🔍 How It Works

1. Enter a topic → YouTube API gets latest videos
2. Filters only 4–20 min videos
3. Sends all titles to GPT
4. GPT selects best one
5. App shows AI’s top pick + full video list

---

⚠️ Notes

* Keep API keys safe — don’t share them publicly
* You can use `.env` or set keys as environment variables

---

🧪 Example

Search: `Data Analyst`
App shows the most relevant video picked by AI + other video options

---

🆓 License

MIT License – free to use, modify, and share.
