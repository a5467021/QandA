#! /usr/bin/python3

import os
import json
import requests


headers = {'Authorization': 'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'};
prefix = 'https://unsplash.com/napi/collections/';
infofix = '?share_key=';
suffix = '/photos?page=1&per_page=30&order_by=latest&share_key=';
collections = ['1795051', '1795048', '1795044', '1795045', '1795046', '1795043', '1795047'];

for addr in collections:
    infobot = requests.get(prefix + addr + infofix, headers = headers);
    name = json.loads(infobot.content.decode('utf-8'))['title'];
    print('running collection', addr, name);
    addr = prefix + addr + suffix;
    mainbot = requests.get(addr, headers = headers);
    pics = json.loads(mainbot.text);
    a = 1;
    if not os.path.exists(name):
        os.mkdir(name);
    for pic in pics:
        print(pic['urls']['small']);
        subot = requests.get(pic['urls']['small']);
        with open('{0}{1}{2}.jpg'.format(name, os.sep, a), 'wb') as f:
            f.write(subot.content);
        subot.close();
        a += 1;
    infobot.close();
    mainbot.close();
input();
