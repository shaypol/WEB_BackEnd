from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


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

@app.route('/')
def home():
    return render_template('cv1.html')


@app.route('/contact')
def contact():
    return render_template('cv2.html')


@app.route('/assignment8')
def assignment8():
    first_name = 'Shay'
    last_name = 'Poleg'
    return render_template('assignment8.html', first_name=first_name, last_name=last_name,
                           hobbies=('Basketball', 'Pilates`', 'Napping'))


if __name__ == '__main__':
    app.run(debug=True)
