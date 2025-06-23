import os
from dotenv import load_dotenv
from pathlib import Path

# Pega o caminho absoluto do arquivo .env na pasta raiz (uma pasta acima de app/)
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

print(os.getenv('SECRET_KEY'))
