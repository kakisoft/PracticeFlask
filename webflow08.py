# webflow08.py
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello/<name>/')
def hello(name):
    return render_template('webflow08.html', name='<p>{0}</p>'.format(name))

if __name__ == '__main__':
    app.run()
