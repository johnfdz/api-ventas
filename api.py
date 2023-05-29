from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_ventas"
    )
except mysql.connector.Error as error:
    print("Error al conectar a la base de datos:", error)
    exit(1)

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    try:
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
    except mysql.connector.Error as error:
        print("Error al obtener los clientes:", error)
        return jsonify({'message': 'Error al obtener los clientes'}), 500

@app.route('/clientes', methods=['POST'])
def crear_cliente():
    try:
        data = request.get_json()
        nombre = data['nombre']
        cedula = data['cedula']

        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO cliente (nombre, cedula)
            VALUES (%s, %s)
        """, (nombre, cedula))

        db.commit()

        return jsonify({'message': 'Cliente creado correctamente'})
    except mysql.connector.Error as error:
        print("Error al crear el cliente:", error)
        return jsonify({'message': 'Error al crear el cliente'}), 500

@app.route('/categorias', methods=['GET'])
def obtener_categoria():
    try:
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
    except mysql.connector.Error as error:
        print("Error al obtener las categorías:", error)
        return jsonify({'message': 'Error al obtener las categorías'}), 500

@app.route('/categorias', methods=['POST'])
def crear_categoria():
    try:
        data = request.get_json()
        nombre = data['nombre']
        percha = data['percha']

        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO categoria (nombre, percha)
            VALUES (%s, %s)
        """, (nombre, percha))

        db.commit()

        return jsonify({'message': 'Categoría creada correctamente'})
    except mysql.connector.Error as error:
        print("Error al crear la categoría:", error)
        return jsonify({'message': 'Error al crear la categoría'}), 500

@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT id, nombre, marca, categoria_id FROM producto")
        productos = cursor.fetchall()

        resultado = []
        for objeto in productos:
            resultado.append({
                'id': objeto[0],
                'nombre': objeto[1],
                'marca': objeto[2],
                'categoria_id': objeto[3]
            })

        return jsonify(resultado)
    except mysql.connector.Error as error:
        print("Error al obtener los productos:", error)
        return jsonify({'message': 'Error al obtener los productos'}), 500

@app.route('/productos', methods=['POST'])
def crear_producto():
    try:
        data = request.get_json()
        nombre = data['nombre']
        marca = data['marca']
        categoria_id = data['categoria_id']

        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO producto (nombre, marca, categoria_id)
            VALUES (%s, %s, %s)
        """, (nombre, marca, categoria_id))

        db.commit()

        return jsonify({'message': 'Producto creado correctamente'})
    except mysql.connector.Error as error:
        print("Error al crear el producto:", error)
        return jsonify({'message': 'Error al crear el producto'}), 500
    

app.debug = True

if __name__ == '__main__':
    app.run()
