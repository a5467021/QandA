#! /usr/bin/python3


import os
import pymysql

host = "192.168.114.128";
port = 3306;
db = "devdb";
user = "dev";
password = "dev0123";
CATEGORY_NAME = {
    1: "music", #音乐
    2: "movie", #电影
    3: "technology", #科技
    4: "reading", #阅读
    5: "game", #游戏
    6: "affair", #时事
    7: "acg", #动漫
    8: "other" #其他
    };

def connect():
    return pymysql.connect(host=host,
                           user=user,
                           passwd=password,
                           db=db,
                           port=port,
                           charset="utf8");

conn = connect();
cur = conn.cursor();
ins = 0;
for category in CATEGORY_NAME:
    if os.path.exists(CATEGORY_NAME[category] + '.txt'):
        with open(CATEGORY_NAME[category] + '.txt', 'r', encoding = 'utf-8') as f:
            print('\ncategory', CATEGORY_NAME[category], '\n');
            for line in f:
                line = line.replace('\n', '');
                if not cur.execute('select id from {0} where description=%s'.format(CATEGORY_NAME[category]), (line)):
                    cur.execute('insert into {0} (id, description) values (%s, %s)'.format(CATEGORY_NAME[category]), (cur.execute('select id from {0}'.format(CATEGORY_NAME[category])) + 1, line));
                    conn.commit();
                    ins += 1;
                    print('[added] ', end = '');
                print(line);
print(ins, 'insertions');
input("\n===============================================\nprogram finished\n");
