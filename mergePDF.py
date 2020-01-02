from PyPDF2 import PdfFileMerger
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--files",
                    help="Archivos por orden de union SEPARADOS POR COMA+ESPACIO. 'file1.pdf, file2.pdf, file3.pdf, "
                         "...'",
                    type=str)
parser.add_argument("--output",
                    help="Nombre archivo resultante CON EXTENSION .pdf. 'result_file.pdf'",
                    type=str)
args = parser.parse_args()
pdfs = args.files.split(', ')

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(args.output)
merger.close()
