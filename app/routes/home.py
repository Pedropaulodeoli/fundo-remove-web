from flask import Flask, Blueprint, render_template

home_route = Blueprint("home",__name__)

@home_route.route('/')
def home():
    return render_template('index.html')