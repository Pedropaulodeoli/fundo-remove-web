from flask import Flask
from app.home import home_route

app = Flask(__name__)

#registrando Blueprint
app.register_blueprint(home_route)