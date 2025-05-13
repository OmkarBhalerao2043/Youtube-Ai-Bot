def extract_titles(video_list):
    return [video['title'] for video in video_list]

def extract_urls(video_list):
    return [video['url'] for video in video_list]