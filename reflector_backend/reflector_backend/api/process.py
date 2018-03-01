'''
Functions of the application.
'''

import json
import random
from reflector_backend.api import dbIO

CATEGORIES_AMOUNT = 8;
QUESTIONS_AMOUNT = {
    1: 20,
    2: 23,
    3: 14,
    4: 19,
    5: 16,
    6: 9,
    7: 20,
    8: 20
    };
IMAGES_AMOUNT = {
    1: 22,
    2: 25,
    3: 19,
    4: 23,
    5: 21,
    6: 15,
    7: 0,
    8: 23
    };
CATEGORY_NAME = {
    1: "音乐", #music
    2: "电影", #movie
    3: "科技", #technology
    4: "阅读", #reading
    5: "游戏", #game
    6: "时事", #affair
    7: "动漫", #acg
    8: "其他" #other
    };
CATEGORY_NUMBER = {
    "音乐": 1, #music
    "电影": 2, #movie
    "科技": 3, #technology
    "阅读": 4, #reading
    "游戏": 5, #game
    "时事": 6, #affair
    "动漫": 7, #acg
    "其他": 8 #other
    };


def GetQuestion(categories = []):
    amount = len(categories);
    if categories == []: # empty categories implies a new user
        for n in range(0,4): # so we random questions of different categories
            t = random.randint(1, CATEGORIES_AMOUNT);
            while t in categories:
                t = random.randint(1, CATEGORIES_AMOUNT);
            categories.append(t);
    else:
        for i in range(0, amount):
            categories[i] = CATEGORY_NUMBER[categories[i]];
        if amount > 4: # when user's interests are more than 4
            cat = categories[:]; # we randomly generate 4 questions of different categories
            categories.clear();
            for n in range(0, 4):
                t = random.randint(1, amount);
                while t in categories:
                    t = random.randint(1, amount);
                categories.append(cat[t - 1]);
        elif len(categories) < 4: # when user's interests are less than 4
            while len(categories) < 4: # we randomly generate questions in his interests to make questions 4
                categories.append(categories[random.randint(1, len(categories)) - 1]);
    question = {};
    n = 1;
    for category in categories:
        title = 'ques{0}'.format(n); # make the response structure
        question[title] = {};
        num = random.randint(1, QUESTIONS_AMOUNT[category]); # random a picture
        question[title]['description'] = dbIO.GetQuestion({'category': category, 'num': num}); # get the question from database
        if IMAGES_AMOUNT[category] < 1:
            question[title]['image'] = '/static/reflector/default.jpg';
        else:
            question[title]['image'] = '/static/reflector/' + CATEGORY_NAME[category] + '/' + str(random.randint(1, IMAGES_AMOUNT[category])) + '.jpg';
        question[title]['category'] = CATEGORY_NAME[category];
        n += 1;
    return question;
