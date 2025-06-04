from flask import Flask, send_from_directory
import os
app = Flask(__name__, static_folder='static',static_url_path='/static')
app.secret_key = os.urandom(30)
@app.route('/')
def home():
    return send_from_directory('D:\portfolio','index.html')
if __name__ == '__main__':
    app.run(debug=True)