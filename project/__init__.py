from flask import Flask
from flaskext.mysql import MySQL
from project.config import Config

app = Flask (__name__)

mysql = MySQL()

app.config.from_object(Config)

mysql.init_app(app)

#aparentemente esto no lo necesita (aparece como en gris mas oscurito), pero si no lo pongo no me deja correrlo (en mi entorno local)
from project import routes