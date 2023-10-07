import pyodbc
from flask import Flask, render_template, request, redirect, url_for
from config import config

app = Flask(__name__)

# Cargar la configuración correspondiente según el entorno
environment = 'development'  
app.config.from_object(config[environment])

# Establecer la conexión a la base de datos utilizando la configuración
conn = pyodbc.connect(app.config['DATABASE_CONNECTION_STRING'])
cursor = conn.cursor()

# ## APP CÓDIGO
@app.route('/')
def mostrar_tareas():
    cursor.execute('SELECT * FROM Tareas')
    tareas = cursor.fetchall()
    return render_template('mostrar_tareas.html', tareas=tareas)



## ACCIONES DE LA APP

## Agregar tarea

@app.route('/agregar_tarea', methods=['POST'])
def agregar_tarea():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        estado = 'No Completado'  
        cursor.execute("INSERT INTO Tareas (descripcion, estado) VALUES (?, ?)", (descripcion, estado))
        conn.commit()
    return redirect(url_for('mostrar_tareas'))

# Marcar una tarea como completada

@app.route('/completar_tarea/<int:id>')
def completar_tarea(id):
    cursor.execute("UPDATE Tareas SET estado='Completado' WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for('mostrar_tareas'))

# Eliminar una tarea
@app.route('/eliminar_tarea/<int:id>')
def eliminar_tarea(id):
    cursor.execute("DELETE FROM Tareas WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for('mostrar_tareas'))

if __name__ == '__main__':
    app.run(debug=True)


