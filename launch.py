from tiktok_api import TikTok_Api


def main():
    print(" ******************** STARTING ********************")
    tiktok_api = TikTok_Api()
    print(tiktok_api.download_nwm_video(videoId="https://www.tiktok.com/@anquynhtrang/video/7104483677459041562", save_path="/Users/phongdang/Workspace/Python/TiktokDownloader/video.mp4"))


if __name__ == "__main__":
    main()