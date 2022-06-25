import os
import threading
from typing import Tuple
from urllib.parse import urlparse

import requests
from colorama import Fore, Style
from tiktok_downloader import TikTokDownloader


def generate_location(media_url: str, download_directory: str, extension: str=".mp4") -> Tuple[str, str]:
    video_filename = f"{urlparse(media_url).path.split('/')[-2]}{extension}"
    full_path = os.path.join(download_directory, video_filename)
    return (full_path, video_filename)

def download_media_url(author_id: str, video_id: str, download_directory: str) -> None:
    video_filename = video_id + ".mp4"
    full_path = os.path.join(download_directory, video_filename)

    files = set(os.listdir(download_directory))
    if video_filename in files:
        print(f"{Fore.CYAN}[=] Filename {video_filename} already downloaded{Style.RESET_ALL}")
    else:
        tiktok_downloader = TikTokDownloader()
        tiktok_downloader.download_nwm_video(author_id = author_id, video_id = video_id, save_path=full_path)

def download_video_background(author_id: str, video_id: str, download_directory: str) -> None:
    thread = threading.Thread(target=download_media_url, name="Video Downloader", args=(author_id, video_id, download_directory))
    thread.start()

def extract_tiktok_id_from_url(url:  str) -> str:
    path = urlparse(url).path
    post_id = path.split("/")[-1]
    return post_id
