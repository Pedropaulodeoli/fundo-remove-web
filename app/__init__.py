from dotenv import load_dotenv
from pathlib import Path
from flask import Flask
import os

from app.routes.home import home_route
from app.processor import upload_route
from app.processor import download_image_route
from app.routes.cadastro.criar_conta import sing_up_route, email_confirm_route
from app.routes.cadastro.login import login_route

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

#registrando Blueprint
app.register_blueprint(home_route)
app.register_blueprint(upload_route)
app.register_blueprint(download_image_route)
app.register_blueprint(sing_up_route)
app.register_blueprint(email_confirm_route)
app.register_blueprint(login_route)

   