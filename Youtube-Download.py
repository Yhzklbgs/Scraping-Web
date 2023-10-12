import yt_dlp

def download_youtube_video(url, resolution='720'):
    RESES = ['144', '240', '360', '480', '720', '1080', '1440', '2160']
    if resolution not in RESES:
        resolution = '720'

    ydl_opts = {
        'format': f'bestvideo[ext=mp4][height<={resolution}]+bestaudio[ext=m4a]/best[ext=mp4][height<={resolution}]',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        if info['filesize_approx'] > 50 * 1024 * 1024:  # Check if the video size is larger than 50MB
            return "Video size exceeds the 50MB limit."

        if info['availability'] != 'public':
            return f"This video is {info['availability'].replace('_', ' ')}."

        ydl.download([url])
        return f"Video '{info['title']}' downloaded successfully."

# Example usage:
video_url = 'YOUTUBE LINK'
resolution = '720'  # Change to your desired resolution
result = download_youtube_video(video_url, resolution)
print(result)
