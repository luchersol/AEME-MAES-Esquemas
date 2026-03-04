# md_to_pdf.py
import argparse
import markdown
from xhtml2pdf import pisa
import os
from bs4 import BeautifulSoup


def numerar_h2(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    contador = 1
    for h2 in soup.find_all("h2"):
        h2.string = f"Actividad {contador}"
        contador += 1
    return str(soup)

def md_to_pdf(input_md: str, output_pdf: str = None):
    """Convierte un archivo Markdown a PDF usando xhtml2pdf.

    Si no se proporciona output_pdf, se genera en la misma carpeta que input_md.
    """
    if not os.path.isfile(input_md):
        raise FileNotFoundError(f"El archivo {input_md} no existe.")

    # Determinar ruta de salida
    if output_pdf is None:
        base, _ = os.path.splitext(input_md)
        output_pdf = f"{base}.pdf"

    with open(input_md, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_text = markdown.markdown(md_text, extensions=['extra', 'toc', 'tables'])
    html_text = numerar_h2(html_text)

    with open(output_pdf, "wb") as f:
        pisa.CreatePDF(html_text, dest=f)

    print(f"PDF generado correctamente: {output_pdf}")


def main():
    parser = argparse.ArgumentParser(description="Convertir Markdown a PDF")
    parser.add_argument("--input", "-i", help="Ruta del archivo Markdown de entrada")
    parser.add_argument("--output", "-o", help="Ruta del archivo PDF de salida (opcional)")
    args = parser.parse_args()

    md_to_pdf(args.input, args.output)


if __name__ == "__main__":
    main()