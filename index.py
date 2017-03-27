from flask import Flask
from flask import render_template
from flask import Flask, request, send_from_directory


app = Flask(__name__,static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('./static/css', path)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
