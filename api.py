import flask
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_ventas"
)

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    cursor = db.cursor()
    cursor.execute("SELECT id, nombre, cedula FROM cliente")
    objetos = cursor.fetchall()

    resultado = []
    for objeto in objetos:
        resultado.append({
            'id': objeto[0],
            'nombre': objeto[1],
            'cedula': objeto[2]
        })

    return jsonify(resultado)

@app.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.get_json()
    nombre = data['nombre']
    cedula = data['cedula']

    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO objetos (nombre, cedula)
        VALUES (%s, %s)
    """, (nombre, cedula))

    db.commit()

    return jsonify({'message': 'Cliente creado correctamente'})

@app.route('/categoria', methods=['GET'])
def obtener_categoria():
    cursor = db.cursor()
    cursor.execute("SELECT id, nombre, percha FROM categoria")
    categoria = cursor.fetchall()

    resultado = []
    for objeto in categoria:
        resultado.append({
            'id': objeto[0],
            'nombre': objeto[1],
            'percha': objeto[2]
        })

    return jsonify(resultado)

@app.route('/categoria', methods=['POST'])
def crear_categoria():
    data = request.get_json()
    nombre = data['nombre']
    percha = data['percha']

    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO categoria (nombre, percha)
        VALUES (%s, %s)
    """, (nombre, percha))

    db.commit()

    return jsonify({'message': 'Categoria creada correctamente'})

if __name__ == '__main__':
    app.run()