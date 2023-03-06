import sqlite3
import csv

#Abrimos el archivo CSV
f=open('C:\\PYTHON\\Trabajo_curso\\.venv\\empleados.csv','r') 
#Omitimos la linea de encabezado
#next(f, None)
reader = csv.reader(f, delimiter=',')

#Crea la BD en la carpeta donde se encuentra el script
sql = sqlite3.connect('C:\\PYTHON\\Trabajo_curso\\.venv\\empleados.db')
cur = sql.cursor()

#Creamos la tabla si no existe
cur.execute('CREATE TABLE IF NOT EXISTS trabajador(id INT(3), nombre VARCHAR(10), apellido VARCHAR(10), sueldo INT(6))')

#Llenamos la BD con los datos del CSV
for row in reader:
    cur.execute("INSERT INTO trabajador VALUES (?,?,?,?)", (row[0], row[1], row[2], row[3]))

#Muestro las filas guardadas en la tabla
for row in cur.execute("SELECT * FROM trabajador where nombre LIKE 'A%'"):
    print(row)

#Cerramos el archivo y la conexion a la bd
f.close()
sql.commit()
sql.close()
