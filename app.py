from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
# You must keep this key safe. Anyone with this key can decrypt your data.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.form['plaintext']
    encrypted_text = cipher_suite.encrypt(plaintext.encode()).decode()
    return render_template('index.html', plaintext=plaintext, encrypted_text=encrypted_text)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_text = request.form['encrypted_text']
    decrypted_text = cipher_suite.decrypt(encrypted_text.encode()).decode()
    return render_template('index.html', encrypted_text=encrypted_text, decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
