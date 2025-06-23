import EnviarEmail
import random
from flask import Blueprint, render_template, request, session, redirect
from werkzeug.security import generate_password_hash
from conexao import conectar

sing_up_route = Blueprint('sing-up',__name__)
email_confirm_route= Blueprint('email_confirm', __name__)

@sing_up_route.route('/sing_up', methods =['GET', 'POST'])
def sing_up():

    try:

        conn = conectar()
        cur = conn.cursor()

        # gera codigo de verificação
        codigo_verificacao = random.randint(1000, 9999)

        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            if len(senha) < 6:
                return render_template('sing_up.html', erro_lenMIN = 'Senha muito curta. No mínimo 6 caracteres.')
            elif len(senha) > 20:
                return render_template('sing_up.html', erro_lenMAX = 'senha muito longa, tamanho maximo: 20 caracteres')
            else:
                senha_hash = generate_password_hash(senha)

            session['codigo_verificacao'] = codigo_verificacao
            session['email'] = email
            session['senha_hash'] = senha_hash

            cur.execute("SELECT email FROM contas WHERE email = %s;", (email,))
            if cur.fetchone():
                return render_template("account/sing_up.html", erro="O email usado ja esta cadastrado, use outro ou tente novamente")

            # ===== Enviando E-mail de verificação ===== #
            EnviarEmail.enviar_email(email, "codigo de verificaçãp", "seu codigo de verificação e: {0}".format(codigo_verificacao))

            return render_template('account/confirm_email.html')
        
        return render_template('account/sing_up.html')
    
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro durante a verificação"
    
    finally:
        if 'cur' in locals():
            cur.close()
        
        if 'conn' in locals():
            conn.close

@email_confirm_route.route("/email_confirm", methods =['GET','POST'])
def email_confirm():
    
    try:
        conn = conectar()
        cur = conn.cursor()
        
        if request.method == 'POST':
            codigo_real = str(session.get('codigo_verificacao'))
            codigo = request.form['confirm_email'].strip()

            email = session.get('email')
            senha = session.get('senha_hash')

            if codigo_real == codigo:
                cur.execute("""
                    INSERT INTO contas (email, senha) 
                    VALUES (%s, %s);
                """, (email, senha))
                conn.commit()
                return redirect('/')
            else:
                return render_template("account/confirm_email.html", erro= "Codigo de verificação incorreto, tente novamente")
            
    except Exception as e:
        print(f"Erro: {e}")
        return("Ocorreu um erro durante a verificação")
    
    finally:
        if 'cur' in locals():
            cur.close()
        
        if 'conn' in locals():
            conn.close()

    

    
   
