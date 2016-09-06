from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/cana-api/')
def index():
    return 'Flask is running!'


@app.route('/cana-api/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
