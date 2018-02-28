'''
Customized RESTful api routes.
'''

import json
from flask import request, make_response
from reflector_backend.views import app
from reflector_backend.api.process import *


def pack(data = ''): # solves the access-control problem and declares the type of data
    res = make_response(data);
    res.mimetype = 'application/json';
    res.headers['Access-Control-Allow-Origin'] = '*';
    res.headers['Access-Control-Allow-Methods'] = 'GET, POST';
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'; 
    return res;

@app.route('/api/question', methods = ['GET']) # test page for post action using FORM
def api_question_test():
    return '''
           <form action="/api/question" method="post">
               <input type="checkbox" name="category" value="音乐">音乐</input>
               <input type="checkbox" name="category" value="电影">电影</input>
               <input type="checkbox" name="category" value="科技">科技</input>
               <input type="checkbox" name="category" value="阅读">阅读</input>
               <input type="checkbox" name="category" value="游戏">游戏</input>
               <input type="checkbox" name="category" value="时事">时事</input>
               <input type="checkbox" name="category" value="其他">其他</input>
               <input type="hidden" name="type" value="test"></input>
               <input type="submit" value="提交"></input>
           </form>
           ''';

@app.route('/api/question', methods = ['POST']) # post action, returns the random questions
def api_question():
    if request.form.get('type') == 'test': # use FORM for debug, 'type' as 'test' 
        category = request.form.getlist('category');
    else: # use APPLICATION/JSON to interact with front-end
        form = json.loads(request.data);
        category = form['category'];
    return pack(json.dumps(GetQuestion(category)));
