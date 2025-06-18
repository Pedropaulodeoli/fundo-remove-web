import os
from flask import request, render_template, send_file, Blueprint
from rembg import remove
from PIL import Image

upload_route = Blueprint('upload',__name__)
download_image_route = Blueprint("download",__name__)

@upload_route.route('/upload', methods=['POST'])
def upload():
    if 'imagem' not in request.files:
        return 'Nenhuma imagem enviada'
    
    image = request.files['imagem']
    if image.filename == '':
        return 'Nenhuma imagem selecionada'
    
    # Abrir a imagem
    input_image = Image.open(image) # Image.open --> item da lib PIL

    # Remover fundo
    output_image = remove(input_image) # remove() remove o fundo da imagem passada como parametro (lib:rembg)

    # Criar pasta se não existir
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join('app', 'static', 'uploads') # criando o caminho usando os.path.join() e armazenado da variavel 
    os.makedirs(output_folder, exist_ok=True) # exist_ok=True -> verifica se a pasta existe, caso nao, ele cria, caso sim ele ignora

    # Caminho do arquivo salvo
    output_path = os.path.join(output_folder, 'resultado_Fundo-Remove.png')

    # Salvar imagem
    output_image.save(output_path)

    # Mostrar o resultado
    return render_template('result.html', imagem_resultado='static/uploads/resultado_Fundo-Remove.png')


@download_image_route.route('/download')
def download():
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        uploads_dir = os.path.join(BASE_DIR, 'static', 'uploads')
        file_path = os.path.join(uploads_dir, 'resultado_Fundo-Remove.png')
        
        # verifica se a pasta exista
        if not os.path.exists(file_path):
            return "Nenhuma imagem processada encontrada", 404
            
        return send_file(
            file_path,
            as_attachment=True,  # Para exibir no navegador
            download_name='Imagem_sem_fundo_FUNDO_REMOVE.png',    # Não força download
            mimetype='image/png'
        )
        
    except Exception as e:
        return f"Erro: {str(e)}", 500
