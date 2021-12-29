from flask import Flask, redirect, url_for, render_template, session, request
# from  interact_with_db import interact_db


app = Flask(__name__)
app.secret_key = '123'


# # ------------- DATABASE CONNECTION --------------- #
# def interact_db(query, query_type: str):
#     return_value = False
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="0548030690Sp",
#         database='myappnewdb'
#     )
#
#     cursor = connection.cursor(named_tuple=True)
#     cursor.execute(query)
#
#     if query_type == 'commit':
#         # Use for INSERT, UPDATE, DELETE statements.
#         # Returns: The number of rows affected by the query (a non-negative int).
#         connection.commit()
#         return_value = True
#
#     if query_type == 'fetch':
#         # Use for SELECT statement.
#         # Returns: False if the query failed, or the result of the query if it succeeded.
#         query_result = cursor.fetchall()
#         return_value = query_result
#
#     connection.close()
#     cursor.close()
#     return return_value
#
#
# # ------------------------------------------------- #

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


if __name__ == '__main__':
    app.run(debug=True)
