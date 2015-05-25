# _*_ coding: utf-8 _*_
from flask import Flask, render_template, request
import json
import urllib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dictionary/', methods=['POST'])
def dic():

    # 字典实现
    words = request.form['words']
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {}
    data['type'] = 'AUTO'
    data['i'] = words
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'true'
    data = urllib.urlencode(data)
    response = urllib.urlopen(url, data)
    html = response.read()
    target = json.loads(html)
    result = target["translateResult"][0][0]['tgt']

    return result

if __name__ == '__main__':
    app.run(debug = True)
