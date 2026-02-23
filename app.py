from flask import Flask, jsonify, request
import sqlite3
import os 
app = Flask(__name__)

def obtener_conexion():
    conn = sqlite3.connect("tarjeta.db")# conecta la base de datos y si no existe la crea 
    conn.row_factory = sqlite3.Row #los resultados se convierten en un direcionario key, value 
    return conn # devuelve la conexión para usarla 

@app.route('/') # ruta principal 
def home():
    return jsonify({"Mensaje":"Bienvenidos al centro de consulta de saldos tarjeta ciudad"})

@app.route('/usuarios', methods=['GET'])# consultar usuarios 
def obtener_usuarios():
    try:
        
        conn = obtener_conexion()
        usuarios = conn.execute("SELECT * FROM usuarios").fetchall()
        conn.close()
        return jsonify([dict(u) for u in usuarios])
    except sqlite3.OperationalError:
        return jsonify({"error": "La tabla 'usuarios' no existe. Ejecuta la inicialización."}), 500

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Datos invalidos"}), 400

    cedula = str(data.get("cedula", ""))

    # Validación de formato (10 dígitos)
    if not cedula.isdigit() or len(cedula) != 10:
        return jsonify({"error": "La cedula debe tener 10 digitos"}), 400

    try:
        conn = obtener_conexion()
        
        # VALIDACIÓN: Verificar si la cédula ya existe
        usuario_existente = conn.execute(
            "SELECT cedula FROM usuarios WHERE cedula = ?", (cedula,)
        ).fetchone()

        if usuario_existente:
            conn.close()
            return jsonify({"error": "Esta cedula ya esta registrada"}), 409 # 409 Conflict

        # Si no existe, procedemos a insertar
        conn.execute("INSERT INTO usuarios (cedula, saldo) VALUES (?, ?)", 
                     (cedula, data.get("saldo", 0)))
        conn.commit()
        conn.close()
        
        return jsonify({"mensaje": "Usuario creado con exito"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/usuarios/<cedula>', methods=['GET'])
def consultar_saldo(cedula):
    # 1. Validación básica: que la cédula enviada sean solo números y tenga 10 dígitos
    if not cedula.isdigit() or len(cedula) != 10:
        return jsonify({"error": "Formato de cedula invalido. Deben ser 10 digitos numericos."}), 400

    try:
        conn = obtener_conexion()
        # 2. Buscamos al usuario por su cédula
        usuario = conn.execute(
            "SELECT saldo FROM usuarios WHERE cedula = ?", (cedula,)
        ).fetchone()
        conn.close()

        # 3. Verificamos si el usuario existe
        if usuario:
            # usuario[0] contiene el saldo porque es la primera columna seleccionada
            return jsonify({
                "cedula": cedula,
                "saldo": usuario[0]
            }), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)