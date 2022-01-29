#esta linea se requiere cuando se pasa la SECRET_KEY y la DATA_BASE_URI como variable de entorno
import os

# entorno de produccion
class Config():
    MYSQL_DATABASE_HOST=os.environ.get('MYSQL_DATABASE_HOST')
    MYSQL_DATABASE_USER=os.environ.get('MYSQL_DATABASE_USER')
    MYSQL_DATABASE_PASSWORD=os.environ.get('MYSQL_DATABASE_PASSWORD')
    MYSQL_DATABASE_DB=os.environ.get('MYSQL_DATABASE_DB')

# entorno de desarrollo, falta crear





# esto iba en el archivo __init__.py en la linea 9 en donde ahora dice: app.config.from_object(Config)
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'patasarriba'