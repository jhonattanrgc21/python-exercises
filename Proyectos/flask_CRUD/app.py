from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexion a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'agenda'
mysql = MySQL(app)

# Configuracion
app.secret_key = 'mysecretkey'

# Vista de inicio
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto')
    data = cur.fetchall()
    return render_template('index.html', contactos = data)

# Vista para crear contactos
@app.route('/add_contact', methods = {'POST'} )
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacto (nombre, telefono) VALUES (%s, %s)', (nombre, telefono))
        mysql.connection.commit()
        flash('Contacto guardado satisfactoriamente.')
        return redirect(url_for('index'))

# Vista para editar contactos
@app.route('/edit/<string:id>')
def get_contact(id):
    # Esta funcion permite obtener el id de un conacto especifico
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacto WHERE id = {0}'. format(id))
    data = cur.fetchall()
    return render_template('edit_contact.html', contacto = data[0])

@app.route('/update/<id>', methods = {'POST'})
def update_contact(id):
    # Actualiza el contacto or medio de su id
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        print(nombre, telefono)
        cur = mysql.connection.cursor()
        cur.execute(""" 
                    UPDATE contacto
                    SET nombre = %s, telefono = %s
                    WHERE id = %s
                    """, (nombre, telefono, id)
                    )
        mysql.connection.commit()
        flash('Contacto modificado satisfactoriamente.')
        return redirect(url_for('index'))

# Vista eliminar contacto
@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacto WHERE id = {0}'. format(id))
    mysql.connection.commit()
    flash('Contacto eliminado satisfactoriamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)