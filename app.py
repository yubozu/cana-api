import os
import configparser

from flask import Flask, jsonify, request, redirect, url_for
from werkzeug import secure_filename

from db.database import Database
from utils.upload import allowed_file, get_allowed_extensions

app = Flask(__name__)

# load config.
cf = configparser.ConfigParser()
cf.read('configs/dev.ini')

connect_string = {}
for option in cf.options('mysqld'):
	connect_string[option] = cf.get('mysqld', option)
connect_string['port'] = int(connect_string['port'])

db = Database(connect_string)

UPLOAD_FOLDER = 'uploads'

@app.route('/cana-api/')
def index():
    return 'Flask is running!'

@app.route('/cana-api/upload', methods=['GET', 'POST'])
def upload_files():
	if request.method == 'POST':
		file = request.files['data']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			print(os.path.join(UPLOAD_FOLDER, filename))
			file.save(os.path.join(UPLOAD_FOLDER, filename))
			return jsonify(filename)
		return jsonify('error'), 500
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


