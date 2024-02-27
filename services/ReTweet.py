import requests
from config.Config import Config
from time import sleep
import os
from utils.ext import Ext

class ReTweet:
    def __init__(self,tw_id=None,cookie_fname=None,time_spacing=0,proxy=0):
        self.tw_id = tw_id
        self.cookie_fname = cookie_fname
        self.time_spacing = time_spacing
        self.proxy = proxy
        self.s = requests.Session()
        if (self.proxy) :
            proxy_data = Ext.get_proxy().split(":")
            proxies = {
                'http': f'http://{proxy_data[2]}:{proxy_data[-1]}@{proxy_data[0]}:{proxy_data[1]}',
            }
            self.s.proxies = proxies
            self.s.proxies.update(proxies)
            
    def run_thread(self):
        cookies = Ext.read_file(self.cookie_fname)['data']
        results = []
        for cookie in cookies:
            run = self.run(cookie=cookie.strip())
            if run:
                results.append(run)
            if self.time_spacing:
                sleep(self.time_spacing)
        return {
            'message':f'============================\nRetweet thành công \t{len(results)}\n============================\n'
        }
    def read_cookies(self):
        with open(self.cookie_fname,encoding='utf-8') as f:
            data = f.readlines()
            return {
                "amount":len(data),
                "cookies": data
            }
    def run(self,cookie):
        res = self.s.post(f'https://twitter.com/i/api/graphql/{Config.retweet_query_id}/CreateRetweet',headers={
            'cookie':cookie,
            'Authorization':f'Bearer {Config.bearer}',
            'X-Csrf-Token':cookie.split("ct0=")[-1].split(";")[0],
            'Content-Type':'application/json'
        },json={
            "variables": {
                "tweet_id": self.tw_id,
                "dark_request":False
            },
            "queryId": Config.retweet_query_id
        })
        try:
            res_json = res.json()
            if (res_json.get('errors')) :
                print(f'=>log: {res_json['errors'][0]['message']}')
                return False
            else:
                print(f'=>log: {res_json['data']['create_retweet']['retweet_results']['result']['rest_id']}')
                return True
        except:
            return False