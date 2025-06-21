from flask import Flask, Blueprint
from app.routes.home import home_route
from app.processor import upload_route
from app.processor import download_image_route
from app.routes.cadastro.criar_conta import sing_up_route, email_confirm_route

app = Flask(__name__)
app.secret_key = '182128'

#registrando Blueprint
app.register_blueprint(home_route)
app.register_blueprint(upload_route)
app.register_blueprint(download_image_route)
app.register_blueprint(sing_up_route)
app.register_blueprint(email_confirm_route)

   