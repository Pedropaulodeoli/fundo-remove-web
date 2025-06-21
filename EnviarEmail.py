import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    # Configurações do servidor do e-mail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    remetente = "fundoremover.web@gmail.com"
    senha = 'acuw ylyi gtih ckvm'

    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adicionando o corpo da mensagem
    msg.attach(MIMEText(mensagem, 'plain'))

    try:
        # Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() # Usa TLS para segurança
        server.login(remetente, senha) # Login no servidor SMTP

        # Envia o e-mail
        server.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

    finally:
        server.quit() # Encerra a conexão com o servidor SMTP

