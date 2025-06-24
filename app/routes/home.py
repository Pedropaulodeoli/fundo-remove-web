from flask import Blueprint, render_template, session

home_route = Blueprint("home",__name__)

@home_route.route('/')
def home():

    id_user = session.get('user_tipo')
    tipo_user = session.get('user_id')
    email = session.get('email')

    if email:
        return render_template('index.html', id_user=id_user, tipo_user=tipo_user, email=email)
    else:
        return render_template('index.html', id_user=None, tipo_user=None, email=None)

