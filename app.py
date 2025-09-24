from flask import Flask, render_template, request, jsonify
import secrets
import string

app = Flask(__name__)

def generate_password(length=12, include_uppercase=True, include_lowercase=True, 
                     include_numbers=True, include_symbols=True):
    """
    Genera una contraseña segura basada en los parámetros especificados
    """
    characters = ""
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not characters:
        return "Error: Debe seleccionar al menos un tipo de carácter"
    
    # Usar secrets para mayor seguridad criptográfica
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        
        length = int(data.get('length', 12))
        include_uppercase = data.get('uppercase', True)
        include_lowercase = data.get('lowercase', True)
        include_numbers = data.get('numbers', True)
        include_symbols = data.get('symbols', True)
        
        # Validaciones
        if length < 4:
            return jsonify({'error': 'La longitud mínima es 4 caracteres'}), 400
        if length > 128:
            return jsonify({'error': 'La longitud máxima es 128 caracteres'}), 400
        
        password = generate_password(
            length=length,
            include_uppercase=include_uppercase,
            include_lowercase=include_lowercase,
            include_numbers=include_numbers,
            include_symbols=include_symbols
        )
        
        if password.startswith('Error:'):
            return jsonify({'error': password}), 400
        
        return jsonify({'password': password})
        
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'OK', 'message': 'Password Generator is running'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)