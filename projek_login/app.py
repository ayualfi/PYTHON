from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# koneksi database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lpba"
)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM tb_user WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    if user:
        if user['level'] == 'Dosen':
            return redirect('/dosen')
        else:
            return redirect('/Mahasiswi')
    else:
        return "Login gagal"

@app.route('/dosen')
def dosen():
    return "<h1>Halaman Dosen</h1>"

@app.route('/Mahasiswi')
def mahasiswa():
    return "<h1>Halaman Mahasiswa</h1>"

app.run(debug=True)
