from flask import Blueprint, render_template
from flask import send_file
from PIL import Image
import os

home_route = Blueprint("home",__name__)

@home_route.route('/')
def home():
    return render_template('index.html')

