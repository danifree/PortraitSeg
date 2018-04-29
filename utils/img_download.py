import os
import requests
import random

proxies = {
    'https': 'https://47.252.1.133:16002',
    'http': 'http://217.61.104.140:3128'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

file_url = './data_orig/alldata_urls.txt'
file_save_dir = '../dataset/imgs'

def dl():
    with open(file_url, 'r') as f:
        lines = f.readlines()
        random.shuffle(lines)
        i = 0
        for line in lines:
            if len(line.split()) != 2 or ".jp" not in line.lower() or "http" not in line:
                print 'url:None'
                continue
            name, url = map(lambda s: s.strip(), line.split())
            file_save_name = os.path.join(file_save_dir, "raw_" + name)
            if os.path.isfile(file_save_name):
                print "exists:", file_save_name
                continue
            try:
                img_data = requests.get(url, proxies=proxies).content
                with open(file_save_name, 'wb') as handler:
                    handler.write(img_data)
                    print name, "has been saved"
            except:
                print "error:", url
        print 'all downloaded!'

def change_name():
    for filename in os.listdir(file_save_dir):
        if filename.startswith("raw_"):
            name_org =  filename.split('.')[0].split('_')[1]
            os.rename(os.path.join(file_save_dir, filename), os.path.join(file_save_dir, name_org + '_raw.jpg'))



if __name__ == '__main__':
    # dl()
    # change_name()
    pass


# download with multiprocess
# #!/usr/bin/env bash
#
# (python img_download.py &)
# (python img_download.py &)
# python img_download.py
