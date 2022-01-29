#from flask import Flask
#from flaskext.mysql import MySQL
from flask import render_template, request
from project import app, mysql

@app.route("/")
def index():
    return render_template('index.html') 
    
@app.route("/create")
def create():
    return render_template('create.html') 

@app.route ('/store',methods=['POST'])
def storage():
    _name = request.form['name']
    _surname = request.form['surname']
    _birth = request.form['birth']
    _area = request.form['area']
    _user = request.form['user']
    _password = request.form['password']
    _mail = request.form['mail']
    _phone = request.form['phone']
    _mobil = request.form['mobil']

    sql = "INSERT INTO `users`(`id`, `name`, `surname`, `birth`, `area`, `user`, `password`, `mail`, `phone`, `mobil`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s);";
    datos = (_name, _surname, _birth, _area, _user, _password, _mail, _phone, _mobil)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('index.html') 
    
@app.route("/nosotros")
def nosotros():
    return render_template('/#nosotros')

@app.route("/recursos")
def recursos():
    return render_template('recursos.html')

@app.route("/contacto")
def contacto():
    return render_template('contacto.html')

