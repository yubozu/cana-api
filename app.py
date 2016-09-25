import os
import configparser

import pymysql

from flask import Flask, jsonify, request, redirect, url_for
from werkzeug import secure_filename

from models.history import History
from utils.dbhelper import DBHelper
from utils.upload import allowed_file, get_allowed_extensions

app = Flask(__name__)

# load config.
cf = configparser.ConfigParser()
cf.read('configs/dev.ini')

connect_string = {}
for option in cf.options('mysqld'):
    connect_string[option] = cf.get('mysqld', option)
connect_string['port'] = int(connect_string['port'])

# TODO: mkdir uploads.
UPLOAD_FOLDER = 'uploads'
dbhelper = DBHelper()

@app.before_request
def prepare():
    dbhelper.prepare_database()

@app.route('/cana-api/')
def index():
    return jsonify(status='Flask is running!'), 200

@app.route('/cana-api/upload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        file = request.files['data']
        # history_id = request.form['id']
        if file and allowed_file(file.filename):

            history = History(request.form, file.filename)
            history.insert()

            filename = secure_filename(file.filename)
            print(os.path.join(UPLOAD_FOLDER, filename))
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            
            return jsonify(filename=filename, id=history_id)
        return jsonify(status='error', id=history_id), 500
    # show upload page.
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="/cana-api/upload" method=post enctype=multipart/form-data>
      <p><input type=file name=data>
         <input type=submit value=Upload>
    </form>
    <p>%s</p>
    """ % "<br>".join(os.listdir(UPLOAD_FOLDER))

if __name__ == '__main__':
    app.run(debug=True, port=8000)