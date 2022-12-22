import pymysql

from flask import *

from datetime import date


def check_date():
    today = date.today()
    print(today)
    str(today)
    print(type(today))

app = Flask(__name__)

app.secret_key = 'staff'


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password']

        connection = pymysql.connect(host="localhost", user="root", password="", database="RestaurantDB")
        print("connected successfully")

        cursor = connection.cursor()
        sql = 'insert into staff (staff_name, staff_email, staff_password) values(%s,%s,%s)'
        cursor.execute(sql, (user_name, user_email, user_password))

        connection.commit()
        return render_template('register.html', msg='Registered successfully')
    else:
        return render_template('register.html')


# @app.route('/search', method=['POST'])
# def search():
#     if request.method == 'POST':
#         return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        connection = pymysql.connect(host="localhost", user="root", password="", database="RestaurantDB")
        print("connected successfully")

        cursor = connection.cursor()
        sql = 'SELECT * FROM staff WHERE staff_email = %s and staff_password  = %s'
        cursor.execute(sql, (user_email, user_password))

        if cursor.rowcount == 0:
            return render_template('login.html', error="Invalid Credential Try Again")
        elif cursor.rowcount == 1:
            row = cursor.fetchone()
            session['key'] = row[1]  # user_name
            return redirect('/view_reservation')


        else:
            return render_template('login.html', error="Something Wrong with your Credentials")

    else:
        return render_template('login.html')


# @app.route('/register')
# def login():
#     return render_template('register.html')
#
#
# @app.route('/login')
# def login():
#     return render_template('login.html')
#

@app.route('/reservation', methods=['POST', 'GET'])
def reservation():
    if request.method == 'POST':

        client_email = request.form['email']
        client_phone = request.form['phone']
        no_of_people = request.form['people']
        reservation_date = request.form['date']
        reservation_time = request.form['time']

        connection = pymysql.connect(host="localhost", user="root", password="", database="RestaurantDB")
        print("connected successfully")

        cursor1 = connection.cursor()
        sql = 'SELECT * FROM reservations'
        cursor1.execute(sql)

        if cursor1.rowcount > 12:
            return render_template('index.html', message='Reservations full')

        else:

            cursor = connection.cursor()
            sql = 'insert into reservations (client_email,client_phone,no_of_people,reservation_date,reservation_time) values(%s,%s,%s,%s,%s)'
            cursor.execute(sql, (client_email, client_phone, no_of_people, reservation_date, reservation_time))

            connection.commit()

            return render_template('index.html', message='Booked Successfully')

    else:
        return render_template('index.html')


@app.route('/view_reservation')
def view():
    if 'key' in session:

        connection = pymysql.connect(host="localhost", user="root", password="", database="RestaurantDB")
        print("connected successfully")
        cursor = connection.cursor()
        sql = 'SELECT * FROM reservations'
        cursor.execute(sql)

        data = cursor.fetchall()
        today = check_date()

        return render_template('reservations.html', reservations=data, today=today)

    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    if 'key' in session:
        session.clear()
        return redirect('/login')


@app.route('/delete/<client_email>')
def delete(client_email):
    connection = pymysql.connect(host="localhost", user="root", password="", database="RestaurantDB")
    cursor = connection.cursor()

    sql = 'delete from reservations where client_email = %s'
    cursor.execute(sql, client_email)

    connection.commit()
    return render_template('reservations.html', msg='Deleted Successfully')
    # return 'Deleted Successfully'


app.run(debug=True)
