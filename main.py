from tiktok_scraper import TikTokScraper


def main():
    print(" ******************** STARTED ********************")

    scraper = TikTokScraper("doodi_zone")
    scraper.run()
    
    print(" ******************** DONE ********************")


if __name__ == "__main__":
    main()