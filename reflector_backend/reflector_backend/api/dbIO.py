'''
Functions interacting with database.
'''

import pymysql


host = "192.168.114.128"; # SQL server host
port = 3306; # SQL server port
db = "devdb"; # database name
user = "dev"; # user name used to log into the database
password = "dev0123"; # password for the user
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

def GetQuestion(question = {'category': 0, 'num': 0}):
    if question['category'] == 0 or question['num'] == 0: # if program enters this branch, end the function in an expected way
        return '';
    conn = connect(); # or else we will query the database and return the question here
    cur = conn.cursor();
    command = "select description from {0} where id=%s".format(CATEGORY_NAME[question['category']]);
    cur.execute(command, (question['num']));
    res = cur.fetchone()[0];
    cur.close();
    conn.close();
    return res;