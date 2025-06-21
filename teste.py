from werkzeug.security import generate_password_hash

senha = 'minhasenha123'

senha_hash = generate_password_hash(senha)

print(senha_hash)