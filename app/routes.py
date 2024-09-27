import os
from flask import render_template, request, redirect, url_for, send_from_directory
from .converters import convert_jpg_to_png, convert_docx_to_pdf

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            file = request.files['file']
            output_name = request.form['output_name']  # Captura o nome do arquivo convertido
            file_ext = os.path.splitext(file.filename)[1].lower()
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Se for JPG, converte para PNG
            if file_ext == '.jpg':
                output_filename = f"{output_name}.png"  # Adiciona a extensão
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                convert_jpg_to_png(file_path, output_path)
                return redirect(url_for('download_file', filename=output_filename))

            # Se for DOCX, converte para PDF
            elif file_ext == '.docx':
                output_filename = f"{output_name}.pdf"  # Adiciona a extensão
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                convert_docx_to_pdf(file_path, output_path)
                return redirect(url_for('download_file', filename=output_filename))

        return render_template('upload.html')

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
