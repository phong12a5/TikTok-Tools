from tiktok_scraper import TikTokScraper
from video_editor import VideoEditor
import sys
import os
import concurrent.futures
import urllib.request

ACCOUNTS = ['ditesuna',
        'doodi_zone',
        'kauut30',
        'endrileka633',
        'guoervictoria0212',
        'rollerming',
        'janice_yy',
        'nyxinhlamne1212',
        'o___o988',
        'nana_omake1',
        'herher408',
        'ngoctuyen_09',
        'pjlquzl6gpqr',
        'haquy1996',
        'ting728118',
        'quinteramms',
        'phuongmaii_95']

def scrap(account : str):
    scraper = TikTokScraper(account = account)
    scraper.run()

def scrapMultiAccount():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(scrap, ACCOUNTS)


def genVideo():
    rootVideoFolder = "/Users/dangphong/autofarmer Dropbox/Auto Farmer/TikTokVideos"
    files = set(os.listdir(rootVideoFolder))
    for author in files:
        if author in ACCOUNTS:
            print(f"generating video in folder {author} ...")
            authorDir = os.path.join(rootVideoFolder,author)
            
            videos = set(os.listdir(authorDir))
            for video in videos:
                video_id = os.path.splitext(video)[0]
                if video_id.endswith("_regen"):
                    print(video_id)
                    continue
                elif (video_id + "_regen.mp4") in videos:
                    print(video_id)
                    continue
                
                needed_gen_video = os.path.join(authorDir,video)
                editor = VideoEditor(needed_gen_video)
                editor.generate()



    

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