import os
from flask import request, render_template, send_file, Blueprint
from rembg import remove
from PIL import Image

upload_route = Blueprint('upload',__name__)

@upload_route.route('/upload', methods=['POST'])
def upload():
    if 'imagem' not in request.files:
        return 'Nenhuma imagem enviada'
    
    image = request.files['imagem']
    if image.filename == '':
        return 'Nenhuma imagem selecionada'
    
    # Abrir a imagem
    input_image = Image.open(image)

    # Remover fundo
    output_image = remove(input_image)

    # Criar pasta se não existir
    output_folder = os.path.join('app', 'static', 'uploads')
    os.makedirs(output_folder, exist_ok=True)

    # Caminho do arquivo salvo
    output_path = os.path.join(output_folder, 'resultado_Fundo-Remove.png')

    # Salvar imagem
    output_image.save(output_path)

    # Mostrar o resultado
    return render_template('result.html', imagem_resultado='static/uploads/resultado_Fundo-Remove.png')
