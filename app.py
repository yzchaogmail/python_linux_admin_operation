#!/usr/bin/python
#-*- coding : UTF-8 -*-

import redis
from flask import Flask

app = Flask(__name__)

@app.route('/user/<int:indentify>')
def get(identify):
    r = redis.StrictRedis(host='114.115.180.236',port = 6378,db = 0)
    username = r.get(identify)

    if username is None:
        return 'not found',404
    else
        return username

if __name__ == '__main__'
    app.run()
