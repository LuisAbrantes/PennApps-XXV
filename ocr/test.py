from PIL import Image
import pytesseract
import pdfplumber
import docx
import os
import glob

def read_image(file_path):
    img = Image.open(file_path)
    return pytesseract.image_to_string(img)

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text

def read_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def process_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()

    if ext in ['.png', '.jpg', '.jpeg']:
        return read_image(file_path)
    elif ext == '.pdf':
        return read_pdf(file_path)
    elif ext == '.docx':
        return read_docx(file_path)
    else:
        return "Format don't supported."


def buscar_arquivos():
    # Extensões de arquivos a serem buscados
    extensoes = ['*.png', '*.jpg', '*.jpeg', '*.pdf', '*.docx']
    
    # Lista para armazenar os arquivos encontrados
    arquivos_encontrados = []
    
    # Buscar arquivos com as extensões especificadas
    for extensao in extensoes:
        arquivos_encontrados.extend(glob.glob(extensao))
    
    # Processar cada arquivo encontrado
    for arquivo in arquivos_encontrados:
        resultado = process_file(arquivo)
        print(f"Arquivo: {arquivo}, Resultado: {resultado}")        
        print('-' * 20)

# Chamar a função para buscar e processar os arquivos
buscar_arquivos()
