#webflow03.py
from flask import Flask
app = Flask(__name__)

books_15h = dict(java15h='Javaで学ぶ', python15h='Pythonで学ぶ', ruby15h='Rubyで学ぶ')

@app.route('/books/<book_title>/')
def hello_15h(book_title):
    return books_15h.get(book_title, '何かで学ぶ')

if __name__ == '__main__':
    app.run()
