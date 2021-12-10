from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def shalom_olam():  # put application's code here
    return 'Shalom Olam!'


@app.route('/homepage')
def hello_home():
    return redirect('home')


@app.route('/articles')
def hello_articles():
    return 'Welcome to articles page'


@app.route('/shaypo')
def shaypo():
    return redirect(url_for('hello_articles'))


if __name__ == '__main__':
    app.run(debug=True)
