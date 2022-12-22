# import pymysql
# from flask import render_template, redirect, session, request
#
# from main import app
#
# connection = pymysql.connect(host="localhost", user="root", password="", database="RestaurantDB")
# print("connected successfully")
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user_email = request.form['email']
#         user_password = request.form['pswd']
#
#         cursor = connection.cursor()
#         sql = 'SELECT * FROM users WHERE user_email=%s AND user_password=%s'
#         cursor.execute(sql, (user_email, user_password))
#
#         if cursor.rowcount == 0:
#             return render_template('login_signup.html', error="Invalid Credential Try Again")
#         elif cursor.rowcount == 1:
#             row = cursor.fetchone()
#             session['key'] = row[1]  # user_name
#             session['email'] = row[2]  # Email
#             return redirect('/cart')
#         else:
#             return render_template('login_signup.html', error="Something Wrong with your Credentials")
#
#
# @app.route('/register')
# def register():
#     if request.method == 'POST':
#         user_name = request.form['name']
#         user_email = request.form['password']
#         user_password = request.form['phone']
#
#         cursor = connection.cursor()
#         sql = 'insert into'
#         cursor.execute(sql, (user_name, user_email, user_password))
#         return render_template('register.html', msg='Registered successfully')
#     else:
#         return render_template('register.html')
#
#
#
# # @app.route('reservation')
# # def reservation():
