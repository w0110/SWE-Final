import uuid
from flask import Flask, jsonify, request
from flask import Flask, render_template
from flask_cors import CORS

DATAS = [
    {
        'id': uuid.uuid4().hex,
        'title': '2020/11/16 8:19:39',
        'author': '薦購系統E-mail自動通知功能暫停公告',
        'link': 'http://recommend.lib.fcu.edu.tw/weblink/scripts/weblink/news.aspx?num=47&displaylang=',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': '2020/3/17 16:28:33',
        'author': '簡體書延遲到貨公告',
        'link': 'http://recommend.lib.fcu.edu.tw/weblink/scripts/weblink/news.aspx?num=45&displaylang=',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': '2020/3/17 16:23:06',
        'author': '各類資源薦購額度與作業方式一覽表',
        'link': 'http://recommend.lib.fcu.edu.tw/weblink/scripts/weblink/news.aspx?num=10&displaylang=',
        'read': True
    }
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def remove_book(book_id):
    for book in DATAS:
        if book['id'] == book_id:
            DATAS.remove(book)
            return True
    return False

@app.route('/new', methods=['GET', 'POST'])
def all_datas():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        DATAS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'link':  post_data.get('link'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Data added!'
    else:
        response_object['datas'] = DATAS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
