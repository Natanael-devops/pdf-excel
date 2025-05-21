from os import listdir
from pathlib import Path

import tabula


lista_pdfs = listdir(Path(__file__).parent/'input')
caminho_input = Path(__file__).parent/'input'/lista_pdfs[0]
caminho_output = Path(__file__).parent/'output'


tabelas = tabula.read_pdf(Path(__file__).parent/'input'/lista_pdfs[0], pages='all')

print(lista_pdfs)
print(caminho_input)
print(caminho_output)
print(tabelas)
