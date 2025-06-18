from flask import Flask, Blueprint
from app.routes.home import home_route
from app.processor import upload_route
from app.processor import download_image_route

app = Flask(__name__)

#registrando Blueprint
app.register_blueprint(home_route)
app.register_blueprint(upload_route)
app.register_blueprint(download_image_route)

   