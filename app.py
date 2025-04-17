# El archivo debe estar corriendo en la terminal para usar el metodo post

from flask import Flask, request, jsonify
# import re

app = Flask(__name__)

# Lista para guardar pacientes
pacientes = []

# Validaciones
def procesoval(a):
    return 10000000000 <= a <= 99999999999

def mailval(b):
    return "@" in b

# def mailval(b):
#     # Validación simple con regex
#     return re.match(r"[^@]+@[^@]+\.[^@]+", b) is not None

# Ruta para registrar un paciente
@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.get_json()

    print("Mail recibido: ", mail)

    dni = data.get('dni')
    nombre = data.get('nombre')
    mail = data.get('mail')
    tipo = data.get('tipo')  # 1 o 2

    if not dni or not procesoval(dni):
        return jsonify({'error': 'DNI inválido. Debe tener exactamente 11 dígitos.'}), 400

    if not nombre:
        return jsonify({'error': 'El nombre no puede estar vacío.'}), 400

    if not mail or not mailval(mail):
        return jsonify({'error': 'Mail inválido. Debe contener un "@".'}), 400

    if tipo not in [1, 2]:
        return jsonify({'error': 'Tipo inválido. Debe ser 1 (particular) o 2 (obra social).'}), 400

    paciente = {
        'dni': dni,
        'nombre': nombre,
        'mail': mail,
        'tipo': 'Particular' if tipo == 1 else 'Obra Social'
    }

    pacientes.append(paciente)
    return jsonify({'mensaje': 'Paciente registrado con éxito.', 'paciente': paciente}), 200

# Ruta para ver todos los pacientes
@app.route('/pacientes', methods=['GET'])
def ver_pacientes():
    return jsonify({'pacientes': pacientes})

if __name__ == '__main__':
    app.run(debug=True, port=8000)


# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "¡Flask está funcionando!"

# if __name__ == '__main__':
#     app.run(debug=True, port=8000)