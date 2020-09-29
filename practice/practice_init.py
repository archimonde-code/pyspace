import flask
import json

server = flask.Flask(__name__)


@server.route('/reg', methods=['post'])
def reg():
    username = flask.request.values.get('username')
    pwd = flask.request.values.get('pwd')
    if username and pwd:
        map()
