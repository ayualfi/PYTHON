from flask import Flask, render_template, request, redirect, session
import mysql.connector

main = Flask(__name__)
main.secret_key='secret'

# koneksi database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lpba"
)

@main.route('/')
def home():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM tb_user WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    if user:
        session['user_id'] = user ['id_user']
        session['level'] = user['level']

        if user['level'] == 'Dosen':
            return redirect('/dosen')
        else:
            return redirect('/mahasiswi')
    else:
        return "Login gagal"

@main.route('/dosen')
def dosen():
    if session.get('level') != 'Dosen':
        return 'Akses ditolak'
    
    cursor=db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tb_nilai")
    data = cursor.fetchall()

    return render_template('dosen.html', nilai = data)

@main.route('/mahasiswi')
def mahasiswa():
    if session.get('level') != 'Mahasiswi':
        return 'Akses ditolak!'
    
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tb_nilai")
    data = cursor.fetchall()

    return render_template('mahasiswi.html', nilai=data)


@main.route('/update_nilai', methods=['POST'])
def update_nilai():
    if session.get('level') != 'Dosen':
        return "Akses ditolak"
    
    id_nilai = request.form['id']
    nilai_baru = request.form['nilai']

    cursor = db.cursor()
    query = "UPDATE tb_nilai SET nilai=%s WHERE id_nilai=%s"
    cursor.execute(query, (nilai_baru, id_nilai))
    db.commit()

    return redirect('/dosen')

main.run(debug=True)
