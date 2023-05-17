from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import MySQLdb
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'pompy'
app.config['MYSQL_PASSWORD'] = 'Lasttry123'
app.config['MYSQL_DB'] = 'dreamscapes_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO customers(name, phone_number, email, message) VALUES (%s, %s, %s, %s)", (name, phone, email, message))
        mysql.connection.commit()
        return redirect(url_for('home'))
    return render_template('contact.html')

@app.route('/manager')
def manager():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    return render_template('manager.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)
