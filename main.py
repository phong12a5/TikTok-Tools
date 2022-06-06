from tiktok_scraper import TikTokScraper
from video_editor import VideoEditor
import sys
import concurrent.futures
import urllib.request

def scrap(account : str):
    scraper = TikTokScraper(account = account)
    scraper.run()

def scrapMultiAccount():
    ACCOUNTS = ['ditesuna',
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(scrap, ACCOUNTS)

def main():
    print(" ******************** STARTED ********************")

    args = sys.argv
    if len(args) == 2:
        task = args[1]
        if task == "scrap":
            scrapMultiAccount()
        elif task == "video":
            editor = VideoEditor('/Users/phongdang/Temp/video.mp4')
            editor.generate()

    else: 
        print("invalid param")

    print(" ******************** DONE ********************")


if __name__ == "__main__":
    main()