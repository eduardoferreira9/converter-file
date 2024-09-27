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
            file_ext = os.path.splitext(file.filename)[1].lower()
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Se for JPG, converte para PNG
            if file_ext == '.jpg':
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
                convert_jpg_to_png(file_path, output_path)
                return redirect(url_for('download_file', filename='output.png'))

            # Se for DOCX, converte para PDF
            elif file_ext == '.docx':
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.pdf')
                convert_docx_to_pdf(file_path, output_path)
                return redirect(url_for('download_file', filename='output.pdf'))

        return render_template('upload.html')

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
