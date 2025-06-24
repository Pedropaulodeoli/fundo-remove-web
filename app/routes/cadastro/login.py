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

            cur.execute('SELECT email FROM contas WHERE email = %s;', (email_login,))
            if cur.fetchone():

                session['email'] = email_login

                cur.execute('SELECT senha FROM contas WHERE email = %s;', (email_login,))
                senha_bd = cur.fetchone()

                cur.execute('SELECT tipo FROM contas WHERE email = %s;', (email_login,) )
                tipo_user = cur.fetchone()
                cur.execute('SELECT id FROM contas WHERE email = %s;', (email_login,))
                id_user = cur.fetchone()

                if tipo_user:
                    session['user_tipo'] = tipo_user
                else:
                    return 'Erro na busca do tipo de usuário'
                
                if id_user:
                    session['user_id'] = id_user
                else:
                    return 'Erro na busca do id do usuário'

                if senha_bd and check_password_hash(senha_bd[0], senha_login):
                    session['usuario'] = email_login
                    return redirect('/')
                else:
                    return "Email ou senha incorretos"
            else:
                return render_template('login.html', erro_email = 'O email digitado nao existe, ou está errado')

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
