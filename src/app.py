from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route('/')
def index():

    username = os.getenv('USER')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    print(username, email, password)

    return '<h1>Hola mundo hermoso sabroson. <br>{} <br>{} <br>{}</h1>'.format(username, email, password)

def status_404(error):
    return '<h2>PAGINA NO ENCONTRADA, ABANDONAR  LA PAGINA INMEDIATAMENTE O UN GATO SAUDI ACABARA CON TU FAMILIA</h2> <img src="https://i.pinimg.com/736x/60/72/bd/6072bd387f10105f4cca73158aadd49b.jpg">'

if __name__ == "__main__":
    app.register_error_handler(404, status_404)
    app.run()