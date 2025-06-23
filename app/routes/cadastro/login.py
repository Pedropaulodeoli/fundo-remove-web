from flask import Flask, render_template, Blueprint, request, session, redirect
from werkzeug.security import check_password_hash
from conexao import conectar
import traceback

login_route = Blueprint('login', __name__)

@login_route.route('/login', methods=['GET', 'POST'])
def login():
    try:
        conn = conectar()
        cur = conn.cursor()

        if request.method == 'POST':
            email_login = request.form['email_login']
            senha_login = request.form['senha_login']

            cur.execute('SELECT senha FROM contas WHERE email = %s;', (email_login,))
            senha_bd = cur.fetchone()

            if senha_bd and check_password_hash(senha_bd[0], senha_login):
                session['usuario'] = email_login
                return redirect('/')
            else:
                return "Email ou senha incorretos"

    except Exception as e:
        print("Erro durante a verificação:")
        traceback.print_exc()
        return "Erro durante a verificação"
    
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

    return render_template('account/login.html')
