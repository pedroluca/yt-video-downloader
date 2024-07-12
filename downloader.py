import yt_dlp as ytd
import os

url = input("Video URL: ")

# Ensure the 'downloaded_videos' directory exists
download_dir = os.path.join(os.path.dirname(__file__), 'downloaded_videos')
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

download_path = os.path.join(download_dir, '%(title)s.%(ext)s')

# Print the download path for verification
print(f"Downloading to: {download_path}")

ydl_opts = {
    'outtmpl': download_path,
}

with ytd.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")