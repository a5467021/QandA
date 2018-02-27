'''Customized RESTful api routes.'''import jsonfrom flask import request, make_responsefrom reflector_backend.views import *from reflector_backend.api.process import *def pack(data = ''): # solves the access-control problem and declares the type of data    res = make_response(data);    res.mimetype = 'application/json';    res.headers['Access-Control-Allow-Origin'] = '*';    res.headers['Access-Control-Allow-Methods'] = 'GET, POST';    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type';     return res;@app.route('/api/question', methods = ['GET'])def api_quiz():    return pack(json.dumps(GetQuestion()));