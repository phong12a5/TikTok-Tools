from tiktok_downloader import TikTokDownloader


def main():
    print(" ******************** STARTING ********************")
    tiktok_downloader = TikTokDownloader()
    print(tiktok_downloader.download_nwm_video(url="https://www.tiktok.com/@anquynhtrang/video/7104483677459041562", save_path="/Users/phongdang/Workspace/Python/TiktokDownloader/video.mp4"))


if __name__ == "__main__":
    main()