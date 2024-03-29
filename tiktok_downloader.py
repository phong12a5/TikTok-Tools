import json
import requests
import re 
import time
import traceback

class TikTokDownloader(object):
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }

        self.tiktok_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "authority": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Host": "www.tiktok.com",
            "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
        }

    def get_video_info(self,author_id, video_id):
        start = time.time()
        try:
            tiktok_api_link = 'https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{}%5D'.format(video_id)
            response = requests.get(url=tiktok_api_link, headers=self.headers).text
            result = json.loads(response)
            url_type = 'video'
            nwm_video_url = result["aweme_details"][0]["video"]["play_addr"]["url_list"][0]
            try:
                wm_video_url = result["aweme_details"][0]["video"]['download_addr']['url_list'][0]
            except Exception:
                wm_video_url = 'None'

            video_title = result["aweme_details"][0]["desc"]
            video_author_nickname = result["aweme_details"][0]['author']["nickname"]
            video_author_id = result["aweme_details"][0]['author']["unique_id"]
            video_create_time = result["aweme_details"][0]['create_time']
            video_aweme_id = result["aweme_details"][0]['statistics']['aweme_id']
            video_music_title = result["aweme_details"][0]['music']['title']
            video_music_author = result["aweme_details"][0]['music']['author']
            video_music_id = result["aweme_details"][0]['music']['id']
            video_music_url = result["aweme_details"][0]['music']['play_url']['url_list'][0]
            video_comment_count = result["aweme_details"][0]['statistics']['comment_count']
            video_digg_count = result["aweme_details"][0]['statistics']['digg_count']
            video_play_count = result["aweme_details"][0]['statistics']['play_count']
            video_download_count = result["aweme_details"][0]['statistics']['download_count']
            video_share_count = result["aweme_details"][0]['statistics']['share_count']
            end = time.time()
            analyze_time = format((end - start), '.4f')
            video_date = {'status': 'success',
                            'analyze_time': (analyze_time + 's'),
                            'url_type': url_type,
                            'api_url': tiktok_api_link,
                            'platform': 'tiktok',
                            'video_title': video_title,
                            'nwm_video_url': nwm_video_url,
                            'wm_video_url': wm_video_url,
                            'video_author_nickname': video_author_nickname,
                            'video_author_id': video_author_id,
                            'video_create_time': video_create_time,
                            'video_aweme_id': video_aweme_id,
                            'video_music_title': video_music_title,
                            'video_music_author': video_music_author,
                            'video_music_id': video_music_id,
                            'video_music_url': video_music_url,
                            'video_comment_count': video_comment_count,
                            'video_digg_count': video_digg_count,
                            'video_play_count': video_play_count,
                            'video_share_count': video_share_count,
                            'video_download_count': video_download_count
                            }
            return video_date
        except Exception as e:
            print(traceback.format_exc())
            return {'status': 'failed', 'reason': e, 'function': 'TikTokDownloader.get_video_info()'}

    def get_video_info2(self,author_id, video_id):
        start = time.time()
        try:
            tiktok_api_link = 'https://api-t2.tiktokv.com/aweme/v1/aweme/detail/?aweme_id={}'.format(video_id)
            response = requests.get(url=tiktok_api_link, headers=self.headers).text
            result = json.loads(response)
            url_type = 'video'
            nwm_video_url = result["aweme_detail"]["video"]["play_addr"]["url_list"][0]
            try:
                wm_video_url = result["aweme_detail"]["video"]['download_addr']['url_list'][0]
            except Exception:
                wm_video_url = 'None'

            # video_title = result["aweme_details"][0]["desc"]
            # video_author_nickname = result["aweme_details"][0]['author']["nickname"]
            # video_author_id = result["aweme_details"][0]['author']["unique_id"]
            # video_create_time = result["aweme_details"][0]['create_time']
            # video_aweme_id = result["aweme_details"][0]['statistics']['aweme_id']
            # video_music_title = result["aweme_details"][0]['music']['title']
            # video_music_author = result["aweme_details"][0]['music']['author']
            # video_music_id = result["aweme_details"][0]['music']['id']
            # video_music_url = result["aweme_details"][0]['music']['play_url']['url_list'][0]
            # video_comment_count = result["aweme_details"][0]['statistics']['comment_count']
            # video_digg_count = result["aweme_details"][0]['statistics']['digg_count']
            # video_play_count = result["aweme_details"][0]['statistics']['play_count']
            # video_download_count = result["aweme_details"][0]['statistics']['download_count']
            # video_share_count = result["aweme_details"][0]['statistics']['share_count']
            end = time.time()
            analyze_time = format((end - start), '.4f')
            video_date = {'status': 'success',
                            'analyze_time': (analyze_time + 's'),
                            'url_type': url_type,
                            'api_url': tiktok_api_link,
                            'platform': 'tiktok',
                            # 'video_title': video_title,
                            'nwm_video_url': nwm_video_url,
                            'wm_video_url': wm_video_url,
                            # 'video_author_nickname': video_author_nickname,
                            # 'video_author_id': video_author_id,
                            # 'video_create_time': video_create_time,
                            # 'video_aweme_id': video_aweme_id,
                            # 'video_music_title': video_music_title,
                            # 'video_music_author': video_music_author,
                            # 'video_music_id': video_music_id,
                            # 'video_music_url': video_music_url,
                            # 'video_comment_count': video_comment_count,
                            # 'video_digg_count': video_digg_count,
                            # 'video_play_count': video_play_count,
                            # 'video_share_count': video_share_count,
                            # 'video_download_count': video_download_count
                            }
            return video_date
        except Exception as e:
            print(traceback.format_exc())
            return {'status': 'failed', 'reason': e, 'function': 'TikTokDownloader.get_video_info2()'}

    def download_nwm_video(self,author_id, video_id, save_path):
        print(f"download_nwm_video-> author_id: {author_id} video_id: {video_id}")
        try:
            video_info = self.get_video_info2(author_id = author_id, video_id = video_id )
            if video_info.get("nwm_video_url"):
                nwm_video_url = video_info["nwm_video_url"]
                video_data = self.get_req_content(nwm_video_url, params=None, headers=self.tiktok_headers)
                with open(save_path, 'wb') as f:
                    f.write(video_data)

        except Exception as e:
            print(e)

    def get_req_content(self, url, params=None, headers=None):
        headers["Host"] = url.split("/")[2]
        r = requests.get(url, params=params, headers=headers)
        return r.content


