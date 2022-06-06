from tiktok_scraper import TikTokScraper
import concurrent.futures
import urllib.request

def scrap(account : str):
    scraper = TikTokScraper(account = account)
    scraper.run()

def main():
    print(" ******************** STARTED ********************")

    # scraper = TikTokScraper(account = "ditesuna")
    # scraper.run()

    ACCOUNTS = ['ditesuna',
            'anquynhtrang',
            'kauut30',
            'endrileka633',
            'guoervictoria0212,
            'rollerming',
            'janice_yy',
            'nyxinhlamne1212'
            'o___o988',
            'nana_omake1',
            'herher408',
            'ngoctuyen_09',
            'pjlquzl6gpqr',
            'haquy1996',
            'ting728118']

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(scrap, ACCOUNTS)

    print(" ******************** DONE ********************")


if __name__ == "__main__":
    main()