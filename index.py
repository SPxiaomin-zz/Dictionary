# _*_ coding: utf-8 _*_
from flask import Flask, render_template, request, session
import json
import urllib

app = Flask(__name__)
app.secret_key = "\xe5'\x95^\x8e\x86\xd1A[\x80\x9dA\xf0\x85\xc26Q\xac\xb4\x13\x15\x9a\xad\xd8";

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 字典实现
        words = request.form['words'].encode('utf-8')
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
        session['words'] = words.decode('utf-8')
        session['result'] = result
        results = target["smartResult"]["entries"]
        session['results'] = results
    return render_template('dic.html')


if __name__ == '__main__':
    app.run(debug = True)
