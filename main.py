from pickle import FALSE
from tiktok_scraper import TikTokScraper
from video_editor import VideoEditor
import sys
import os
import concurrent.futures
import requests
import json

ACCOUNTS = [
        'ditesuna',
        'doodi_zone',
        'kauut30',
        'endrileka633',
        'guoervictoria0212',
        'janice_yy',
        'nyxinhlamne1212',
        'nana_omake1',
        'herher408',
        'pjlquzl6gpqr',
        'haquy1996',
        'quinteramms',
        'phuongmaii_95',
        'thutrang20023',
        'nabi15100',
        'mytay.955'
        ]

def scrap(account : str):
    scraper = TikTokScraper(account = account)
    scraper.run()

def scrapMultiAccount():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            executor.map(scrap, ACCOUNTS)


def genVideo():
    rootVideoFolder = "/Users/phongdang/autofarmer Dropbox/Auto Farmer/TikTokVideos"
    files = set(os.listdir(rootVideoFolder))
    for author in files:
        if author in ACCOUNTS:
            print(f"generating video in folder {author} ...")
            authorDir = os.path.join(rootVideoFolder,author)
            
            videos = set(os.listdir(authorDir))
            for video in videos:
                if video == ".DS_Store":
                    continue

                video_id = os.path.splitext(video)[0]
                regen_video = video_id + "_regen.mp4"
                if video_id.endswith("_regen"):
                    print("ignore .... ", video_id)
                    continue
                elif regen_video in videos:
                    print("ignore .... ", video_id)
                    continue
                elif video.endswith(".mp4") == FALSE:
                    print(f"{video} is not video file .... ")
                    continue
                
                needed_gen_video = os.path.join(authorDir,video)
                editor = VideoEditor(needed_gen_video)
                editor.generate()
                submitVideo(video_id, author, f"/TikTokVideos/{author}/{regen_video}")


def submitVideo(video_id: str, author: str, video_path : str):
    url = "https://dangbaphong.com/api/tiktok/mm-tiktok-api.php"

    payload = json.dumps({
    "api": "add_new_video",
    "video_id": video_id,
    "author": author,
    "video_path": video_path
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload) 
    print(response)

    

def main():
    print(" ******************** STARTED ********************")

    args = sys.argv
    if len(args) == 2:
        task = args[1]
        if task == "scrap":
            scrapMultiAccount()
        elif task == "video":
            # editor = VideoEditor('/Users/dangphong/autofarmer Dropbox/Auto Farmer/TikTokVideos/ting728118/7045338603110583598.mp4')
            # editor.generate()
            genVideo()

    else: 
        print("invalid param")

    print(" ******************** DONE ********************")


if __name__ == "__main__":
    main()