from flask import redirect, render_template, request, Blueprint
from interact_with_DB import interact_db

# Assignment 10 #
Message = ""

Assignment10 = Blueprint('Assignment10', __name__, static_folder='static',
                         static_url_path='/Assignment10', template_folder='templates')


@Assignment10.route("/Assignment10", methods=['GET', 'POST'])
def Assignment10_page():
    global Message
    Message = ""
    return render_template('Assignment10.html')


@Assignment10.route("/Assignment10", methods=['GET', 'POST'])
def assignment10_page():
    global Message
    Message = ""
    return render_template('Assignment10.html')


@Assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['NAME']
    email = request.form['EMAIL']
    query = "INSERT INTO users(name, email) VALUES ('%s', '%s')" % (name, email)
    interact_db(query=query, query_type='commit')
    global Message
    Message = "The user "+name+" has been inserted."
    return redirect('/user_list')


@Assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    name = request.form['name']
    query = "DELETE FROM users WHERE name='%s'" % name
    interact_db(query, query_type='commit')
    global Message
    Message = "The user "+name+" has been deleted."
    return redirect('/user_list')


@Assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    name = request.form['name']
    new_email = request.form['new_email']
    query = "update users set email = '%s', where name = '%s'" % (new_email, name)
    interact_db(query=query, query_type='commit')
    global Message
    Message = "The email of the user "+name+"has been updated."
    return redirect('/user_list')


@Assignment10.route('/user_list')
def user_list_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('Assignment10.html', user_list=query_result, Message=Message)
