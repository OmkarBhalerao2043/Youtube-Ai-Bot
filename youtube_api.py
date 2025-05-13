import requests
from datetime import datetime, timedelta
import isodate

def search_youtube(query, api_key, max_results=20):
    base_url = "https://www.googleapis.com/youtube/v3/search"

    # 🔁 You can comment this out if it's too restrictive
    published_after = (datetime.utcnow() - timedelta(days=14)).isoformat("T") + "Z"

    params = {
        'part': 'snippet',
        'q': query,
        'key': api_key,
        'type': 'video',
        'maxResults': max_results,
        'publishedAfter': published_after  # Remove this line if you want older videos too
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # ✅ Debug: check for API errors or empty results
    if 'error' in data:
        print("YouTube API Error:", data['error'])
        return []

    if not data.get("items"):
        print("No videos found for this query.")
        return []

    print(f"Found {len(data['items'])} videos. Filtering now...")

    return filter_videos(data.get("items", []), api_key)

def filter_videos(items, api_key):
    video_ids = [item['id']['videoId'] for item in items if 'videoId' in item['id']]
    if not video_ids:
        print("No video IDs found.")
        return []

    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "contentDetails,snippet",
        "id": ",".join(video_ids),
        "key": api_key
    }

    res = requests.get(url, params=params)
    data = res.json()

    if 'error' in data:
        print("Error in video details fetch:", data['error'])
        return []

    filtered = []
    for item in data.get("items", []):
        duration = item['contentDetails']['duration']
        minutes = parse_duration_to_minutes(duration)

        print(f"Video: {item['snippet']['title']}, Duration: {minutes} min")  # 👀 For debug

        if 0 <= minutes <= 20:  # ✅ Adjusted duration filter
            filtered.append({
                "title": item['snippet']['title'],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "duration": minutes
            })

    if not filtered:
        print("No videos passed the duration filter.")
    return filtered

def parse_duration_to_minutes(duration):
    try:
        td = isodate.parse_duration(duration)
        return int(td.total_seconds() // 60)
    except Exception as e:
        print("Duration parsing error:", e)
        return 0