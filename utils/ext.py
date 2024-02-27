import  win32gui, win32con, os
import random
from config.Config import Config
# id = JSON.parse(
# document.evaluate(
#     '//script[@type="application/ld+json"]', 
#     document.lastChild, 
#     null,
#     XPathResult.ANY_TYPE, null).iterateNext().textContent
# ).author.identifier;

class Ext:
    def get_proxy():
        proxy_list = Ext.read_file(Config.proxy_file)['data']
        return random.choice(proxy_list)
    def read_file(file_name):
        with open(file_name,encoding='utf-8') as f:
            data = f.readlines()
            return {
                "amount":len(data),
                "data": data
            }    
    def paginate(items, per_page):
        pages = [items[i:i+per_page] for i in range(0, len(items), per_page)]
        return pages
    def openFileDialog():
        filter='Text files\0*.txt\0'
        customfilter='Other file types\0*.*\0'
        fname, customfilter, flags=win32gui.GetOpenFileNameW(
            InitialDir=os.environ['temp'],
            Flags=win32con.OFN_EXPLORER,
            File='somefilename', DefExt='txt',
            Title='GetOpenFileNameW',
            Filter=filter,
            CustomFilter=customfilter,
            FilterIndex=0)
        return fname