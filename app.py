import os
from flask import Flask
from app.routes import init_routes

# Definindo os caminhos absolutos conforme informado
UPLOAD_FOLDER = r'C:\Users\Eduardo\converter-file\converter-file\uploads'
TEMPLATE_FOLDER = r'C:\Users\Eduardo\converter-file\converter-file\app\templates'

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)  # Especifica o caminho dos templates
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Pasta para upload dos arquivos

# Cria a pasta de upload se não existir
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Inicializa as rotas
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
