import os

import flask
from werkzeug.utils import redirect

import utils

USERNAME = 'tomsradio'
PASSWORD = 'tFrss42%2o@safa#1'
SONGS_PATH = '/Users/sakkeerhussain/Downloads'


app = flask.Flask(__name__)
app.secret_key = 'ssadSSAEt32AdFG5!@$Asfaf'
app.config['SESSION_TYPE'] = 'filesystem'


iteration_test = 0

@app.route("/next")
def next_track():
    global iteration_test
    if iteration_test == 0:
        resp = './test-files-server-flask/music/Gunda-Gunda-Gundajayan-Shabareesh-Varma.mp3'
    elif iteration_test == 1:
        resp = './test-files-server-flask/music/Kannamma--From-Veyil--Pradeep-Kumar.mp3'
    else:
        resp = './test-files-server-flask/music/sample-3s.mp3'

    iteration_test = (iteration_test + 1) % 3
    return resp
    # return 'annotate:title="Chamakay",artist="Blood Orange",album="Cupid Deluxe":http://localhost:5000/music/sample-3s.mp3'

@app.route("/")
def home_page():
    if flask.session.get("username") != USERNAME:
        flask.session["username"] = None
        return redirect(flask.url_for('auth_login'))

    files = utils.get_files(SONGS_PATH)
    return flask.render_template('files-list.html', files=files)


@app.route("/file/delete")
def file_delete():
    if flask.session.get("username") != USERNAME:
        flask.session["username"] = None
        return redirect(flask.url_for('auth_login'))

    path = flask.request.args['path']
    utils.delete_file(SONGS_PATH, path)
    return redirect(flask.url_for('home_page'))


@app.route("/file/upload", methods=['POST'])
def file_upload():
    if flask.session.get("username") != USERNAME:
        flask.session["username"] = None
        return redirect(flask.url_for('auth_login'))

    file = flask.request.files['file']
    if not utils.create_file(SONGS_PATH, file):
        flask.flash('Failed to upload file!')
    return redirect(flask.url_for('home_page'))


@app.route("/auth/login", methods=['POST', 'GET'])
def auth_login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']

        if username == USERNAME or password == PASSWORD:
            flask.session["username"] = username
            return redirect(flask.url_for('home_page'))

        flask.flash('Invalid credentials!')
        return redirect(flask.url_for('auth_login'))
    else:
        return flask.render_template('auth/login.html')


@app.route("/auth/logout")
def auth_logout():
    flask.session["username"] = None
    return redirect(flask.url_for('auth_login'))


app.run(host='0.0.0.0', port=5000, debug=True)
