from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), nullable = False)
	roll = db.Column(db.String(20), nullable = False)

@app.route('/')
@app.route('/home')
def home():
	return render_template("index.html")

@app.route('/', methods = ['POST'])
def submit():
	if request.method == "POST":
		features = request.form.copy()
		name = features['name']
		roll = features['roll']
		user = User(name = name, roll = roll)
		db.session.add(user)
		db.session.commit()
		flash(f'Added new user!', 'success')
		return redirect(url_for('home'))

@app.route('/database', methods = ['POST'])
def view_database():
	if request.method == "POST":
		database = r"C:\Users\SHREENATH BHARADWAJ\Desktop\Exercises\web-dev-projects\User-input-database\site.db"
		conn = sqlite3.connect(database)
		cur = conn.cursor()
		cur.execute("SELECT * FROM user")
		rows = cur.fetchall()
		records = []
		for row in rows:
			records.append(row)
		return render_template('database.html', message = records)

if __name__ == '__main__':
	app.run(debug = True)