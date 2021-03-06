# webflow10.py
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def form_index():
    if request.method == "GET":
        if 'text1' in request.args:
            return render_template(
                'webflow10.html',
                text1=request.args['text1']
            )
    return render_template('webflow10.html')

if __name__ == '__main__':
    app.run(debug=True)
