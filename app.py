from flask import Flask, redirect, url_for, render_template, session, request
from pages.Assignment10.Assignment10 import Assignment10


app = Flask(__name__)
app.secret_key = '123'


@app.route('/home')
def shalom_olam():  # put application's code here
    return render_template('cv1.html')


@app.route('/homepage')
def hello_home():
    return render_template('cv1.html')


@app.route('/shay')
def shaypo():
    return redirect(url_for('hello_home'))


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
    hobbies = ('Basketball', 'Pilates`', 'Napping')
    return render_template('assignment8.html', first_name=first_name, last_name=last_name,
                           hobbies=hobbies)


users = {'user1': {'name': 'Shay', 'email': 'shaypo@gmail.com'},
         'user2': {'name': 'Gal', 'email': 'galbi@gmail.com'},
         'user3': {'name': 'Alex', 'email': 'alexya@gmail.com'},
         'user4': {'name': 'Mark', 'email': 'markfi@gmail.com'},
         'user5': {'name': 'Jeremy', 'email': 'jbloom@gmail.com'},
         'user6': {'name': 'Gad', 'email': 'gadha@gmail.com'},
         'user7': {'name': 'Valeriya', 'email': 'valer@gmail.com'}}


@app.route('/sign', methods=['GET', 'POST'])
def search_reg_func():
    if request.method == 'GET':
        if 'email' in request.args:
            email = request.args['email']
            if 'email' == '':
                return render_template('assignment9.html', users=users)
            for key, value in users.items():
                if value.get('email') == email:
                    return render_template('assignment9.html', name=value.get('name'), email=value.get('email'))
        if request.method == "POST":
            session['name'] = request.form['name']
        return render_template('assignment9.html')


@app.route("/logout", methods=['GET', 'POST'])
def log_out_func():
    session['name'] = ''
    return render_template('assignment9.html')


app.register_blueprint(Assignment10)


if __name__ == '__main__':
    app.run(debug=True)
