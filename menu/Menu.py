
import os
from services.Like import Like
from services.ReTweet import ReTweet
from services.Follow import Follow
from utils.ext import Ext
import json
from config.Config import Config

class Menu:
    options = [
        '1, Buff like bài viết',
        '2, Đăng lại bài viết',
        '3, Follow trang cá nhân',
        '4, Thay đổi đường dẫn tệp proxy',
        '5, Thoát (q hoặc quit)'
    ]
    close = ('q','quit',5,'5')
    def printMenu(self):
        print('\n'.join(self.options))
    def control_option(self,option):
        if int(option) == 1:
            tw_id = input('Bước 1, Nhập id bài viết : ')
            print('Bước 2, Chọn file chứa cookie: ')
            fname = Ext.openFileDialog()
            print(fname)
            time_spacing = int(input('Bước 3, Chọn thời gian giãn cách (số giây): '))
            proxy = int(input('Bước 4, Bật tắt proxy (bật: 1, tắt: 0): '))
            task = Like(
                tw_id=tw_id,
                cookie_fname=fname,
                time_spacing=time_spacing,
                proxy=proxy
            )
            run = task.run_thread()
            os.system('cls')
            print(run['message']+'\n')
        elif int(option) == 2:
            tw_id = input('Bước 1, Nhập id bài viết : ')
            print('Bước 2, Chọn file chứa cookie: ')
            fname = Ext.openFileDialog()
            print(fname)
            time_spacing = int(input('Bước 3, Chọn thời gian giãn cách (số giây): '))
            proxy = int(input('Bước 4, Bật tắt proxy (bật: 1, tắt: 0): '))
            task = ReTweet(
                tw_id=tw_id,
                cookie_fname=fname,
                time_spacing=time_spacing,
                proxy=proxy
            )
            run = task.run_thread()
            os.system('cls')
            print(run['message']+'\n')
        elif int(option) == 3:
            print('Bước 1, Chọn file chứa cookie: ')
            cookie_fname = Ext.openFileDialog()
            print(cookie_fname)
            print('Bước 2, Chọn file chứa user id: ')
            user_fname = Ext.openFileDialog()
            print(user_fname)
            amount = int(input('Bước 3, Chọn số lượng follow cho mỗi user: '))
            time_spacing = int(input('Bước 4, Chọn thời gian giãn cách (số giây): '))
            proxy = int(input('Bước 5, Bật tắt proxy (bật: 1, tắt: 0): '))
            task = Follow(
                cookie_fname=cookie_fname,
                user_fname=user_fname,
                amount=amount,
                time_spacing=time_spacing,
                proxy=proxy
            )
            run = task.run_thread()
        elif int(option) == 4:
            try:
                proxy_fname = Ext.openFileDialog()
                Config.change_proxy_file(proxy_fname)
                print('Thay đổi đường dẫn proxy thành công: '+ proxy_fname)
            except:
                print('Có lỗi xảy ra vui lòng thử lại')
        else :
            print('Vui lòng chọn trong menu 1 -> 5')