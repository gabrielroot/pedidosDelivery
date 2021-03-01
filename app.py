from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():

    data = {
      'message': 'Delivery api'
    }

    return jsonify(data)


@app.route('/usr')
def usr():

    data = {
      'message': 'Delivery api on [USR]'
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run()
