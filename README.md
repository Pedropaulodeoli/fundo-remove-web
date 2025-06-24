## Desenvolvimento pausado
# Site Fundo-Remover

Este projeto é um site para remoção de fundo de imagens automaticamente. O sistema permite cadastro de usuários, verificação de e-mail, login, upload de imagens e download da imagem processada. Além disso, utiliza banco de dados PostgreSQL para gerenciamento de contas, imagens, pagamentos e planos.

## Funcionalidades

- Sistema de cadastro e login
- Verificação de e-mail com código
- Upload de imagens
- Remoção de fundo automaticamente
- Download da imagem processada
- Sistema de envio de e-mails para verificação
- Armazenamento de dados em PostgreSQL
- Hash de senha para segurança
- Estrutura modular com Flask Blueprints

## Tecnologias Usadas

- Python 3
- Flask
- PostgreSQL
- Rembg (remoção de fundo)
- Psycopg2 (integração com PostgreSQL)
- Werkzeug (hash de senha)
- HTML, CSS e JavaScript

## Como Executar Localmente

1. Clone o repositório: https://github.com/Pedropaulodeoli/fundo-remove-web.git

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   
-No Windows: venv\Scripts\activate

-No Linux/macOS: source venv/bin/activate

3. Instale as dependências: pip install -r requirements.txt

4. Execute o projeto: python main.py

5. Acesse no navegador: http://127.0.0.1:5000

## Banco de Dados

- Banco utilizado: PostgreSQL
- As tabelas e tipos ENUM são criados diretamente no banco utilizando scripts SQL preparados no desenvolvimento.

## Próximas Funcionalidades

- Ferramenta de pincel para edição manual
- Sistema de pagamento (Pix, Cartão, Débito)
- Dashboard administrativo
- Armazenamento de imagens em nuvem
- Otimizações de segurança e performance










