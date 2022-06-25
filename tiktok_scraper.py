import argparse
import collections
import json
import os
import time
import getpass
from typing import Dict

from bs4 import BeautifulSoup

from playwright.sync_api import Page
from playwright.sync_api import Response
from playwright.sync_api import Route
from playwright.sync_api import sync_playwright

from constants import DOCUMENT_JSON_SCRIPT_CSS_SELECTOR
from constants import EXCLUDED_RESOURCE_TYPES
from constants import JAVASCRIPT_BOTTOM_PAGE_CHECKER
from constants import SCROLL_DELAY
from constants import SCROLLING_DELTA_Y

from utils import download_video_background
from utils import download_media_url


class TikTokScraper:

    def __init__(self, account: str, headless: bool = True) -> None:
        self.account = account
        self._videos_ids = set()
        self._headless = headless
        self._base_video_folder_name = f"/Users/{getpass.getuser()}/autofarmer Dropbox/Auto Farmer/TikTokVideos"
        self._full_path_directory = os.path.join(self._base_video_folder_name, account)

        self._create_downloaded_videos_directory_if_not_exists()

    def _generate_tiktok_url(self, lang: str = "vn") -> str:
        return f"https://www.tiktok.com/@{self.account}"

    def _create_downloaded_videos_directory_if_not_exists(self):
        if not os.path.exists(self._full_path_directory):
            os.makedirs(self._full_path_directory)

    def _extract_video_download_addr_from_item(self, item: Dict) -> None:
        self._extract_comments_from_tiktok_item(item)
        video_id = item["video"]["id"]
        author_id = item["author"]
        print(len(self._videos_ids))
        if video_id not in self._videos_ids:
            self._videos_ids.add(video_id)

    def _extract_comments_from_tiktok_item(self, item: Dict) -> None:
        tiktok_id = item["id"]
        print(f"Tiktok video_id:", tiktok_id)

    def handle_request(self, response: Response) -> None:
        print(f"handle_request-> url: {response.url}")
        try:
            if response.request.resource_type == "document":
                content = response.text()
                soup = BeautifulSoup(content, "html.parser")
                json_data = soup.select_one(DOCUMENT_JSON_SCRIPT_CSS_SELECTOR).text
                data = json.loads(json_data)

                for key, item in data["ItemModule"].items():
                    self._extract_video_download_addr_from_item(item)
            elif "tiktok.com/api/post/item_list" in response.url:
                data = response.json()
                items = data["itemList"]
                for item in items:
                    self._extract_video_download_addr_from_item(item)

        except Exception as e:
            print("handle_request error: ", e)

    def block_unnecessary_resources(self, route: Route) -> None:
        if (route.request.resource_type in EXCLUDED_RESOURCE_TYPES):
            route.abort()
        elif route.request.url == "https://mon-va.byteoversea.com/monitor_browser/collect/batch/":
            route.abort()
        else:
            route.continue_()

    def _has_bot_reached_bottom_of_the_page(self, page: Page) -> bool:
        return page.evaluate(JAVASCRIPT_BOTTOM_PAGE_CHECKER)

    def _scroll_to_bottom(self, page: Page) -> None:
        positions_y_deque_size = 200
        last_y_positions = collections.deque(maxlen=positions_y_deque_size)

        has_reached = False
        while not has_reached:
            page.mouse.wheel(delta_x=0, delta_y=75)
            # page.keyboard.press('ArrowDown')
            page.wait_for_load_state("domcontentloaded")

            value = page.evaluate("window.scrollY")
            last_y_positions.append(value)

            if len(last_y_positions) == positions_y_deque_size and len(set(last_y_positions)) == 1:
                has_reached = True
                        

    def run(self):
        with sync_playwright() as p:
            url = self._generate_tiktok_url()
            browser = p.firefox.launch(headless=self._headless)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()
            page.on("response", self.handle_request)
            page.route("**/*", self.block_unnecessary_resources)
            page.goto(self._generate_tiktok_url())

            self._scroll_to_bottom(page)
            page.close()

            for video_id in self._videos_ids:
                download_media_url(self.account, video_id, self._full_path_directory)
