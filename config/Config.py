import json,os
config_fname = os.path.join(os.getcwd(),'config/config.json')
config_f = open(config_fname,encoding='utf-8').read()
config_to_json = json.loads(config_f)

class Config:
    bearer = config_to_json['bearer']
    like_query_id = config_to_json['like_query_id']
    retweet_query_id = config_to_json['retweet_query_id']
    proxy_file = config_to_json['proxy_file']
    def change_proxy_file(file_name):
        conf = json.load(open(config_fname,encoding='utf-8')) 
        conf['proxy_file'] = file_name
        with open(config_fname,'w') as json_file:
            json_file.write(json.dumps(conf, indent=4))
        Config.proxy_file = file_name