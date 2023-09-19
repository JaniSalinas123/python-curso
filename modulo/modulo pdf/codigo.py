# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 20:48:36 2023

@author: Janise
"""
import PyPDF2

# Reemplaza esta ruta con la ruta completa de tu archivo PDF
pdf_file_path = r'C:\Users\Janise\OneDrive\Escritorio\python curso\modulo\modulo pdf\modelo.pdf'

# Abre el archivo PDF en modo lectura binaria ('rb')
with open(pdf_file_path, 'rb') as pdf_file:
    # Crea un objeto PdfReader en lugar de PdfFileReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Obtiene el número total de páginas en el PDF
    num_pages = len(pdf_reader.pages)

    # Itera a través de cada página y extrae el texto
    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        print(f"Texto de la página {page_number + 1}:\n{text}\n")
