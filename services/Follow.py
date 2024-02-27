import requests
from config.Config import Config
from time import sleep
import os
from utils.ext import Ext


class Follow:
    def __init__(self,
            cookie_fname=None,
            user_fname=None,
            amount=0,
            time_spacing=0,
            proxy=0
        ):
        self.user_fname = user_fname
        self.cookie_fname = cookie_fname
        self.time_spacing = time_spacing
        self.amount = amount
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
        users = Ext.read_file(self.user_fname)['data']
        cookies = Ext.paginate(Ext.read_file(self.cookie_fname)['data'],self.amount)
        for page,user in enumerate(users):
            try:
                paginate_cookies = cookies[page]
                for cookie in paginate_cookies:
                    run = self.run(cookie=cookie.strip(),user_id=user.strip())
                    print(run)
                    sleep(self.time_spacing)
            except:
                print('Số lượng cookie không đủ: ' + user)
   
    def run(self,cookie,user_id):
        res = self.s.post(f'https://twitter.com/i/api/1.1/friendships/create.json',headers={
            'cookie':cookie,
            'Authorization':f'Bearer {Config.bearer}',
            'X-Csrf-Token':cookie.split("ct0=")[-1].split(";")[0],
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            "Referer":f"https://twitter.com/i/user/{user_id}"
        },data={
            "user_id": int(user_id)
        })
        try:
            res_json = res.json()
            if (res_json.get('errors')) :
                return f'=>log: {user_id} - {res_json['errors'][0]['message']} -'
            else:
                return f'=>log:Following {res_json['name']}'
        except:
            return 'Có lỗi xảy ra, '+ user_id