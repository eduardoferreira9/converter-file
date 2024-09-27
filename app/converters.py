from docx import Document
from reportlab.pdfgen import canvas

def convert_docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    pdf = canvas.Canvas(pdf_path)
    width, height = 595, 842  # Tamanho de uma página A4
    pdf.setPageSize((width, height))
    
    # Escreve o conteúdo do DOCX no PDF
    for para in doc.paragraphs:
        pdf.drawString(100, height - 50, para.text)
        height -= 50  # Move o texto para baixo
        
        if height < 100:  # Se chegar ao fim da página, cria uma nova
            pdf.showPage()
            height = 842

    pdf.save()

from PIL import Image

def convert_jpg_to_png(jpg_path, png_path):
    img = Image.open(jpg_path)
    img.save(png_path, 'PNG')
