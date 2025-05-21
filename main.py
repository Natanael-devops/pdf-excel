import fitz
import pandas as pd
import re

doc = fitz.open("input/MMB-2H05K.03-E-0009_0002-C (1).pdf")
page = doc[0]

rect = fitz.Rect(x0=300, y0=50, x1=650, y1=750)

words = page.get_text("words")  # lista de tuplas: (x0, y0, x1, y1, "palavra", block_no, line_no, word_no)
# Filtra palavras que estejam dentro do retângulo
words_filtradas = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]

# Agora agrupar palavras por linha
from collections import defaultdict
linhas_dict = defaultdict(list)

for w in words_filtradas:
    block_no, line_no = w[5], w[6]
    linhas_dict[(block_no, line_no)].append(w)

linhas_texto = []
for key in sorted(linhas_dict.keys()):
    # Ordenar as palavras pela coordenada x0 para garantir ordem
    palavras = sorted(linhas_dict[key], key=lambda x: x[0])
    linha = " ".join(p[4] for p in palavras)
    linhas_texto.append(linha)

# Agora juntar linhas em registros conforme o padrão
registros = []
linha_temp = []
padrao_inicio_item = re.compile(r'^\d{8,}')

for linha in linhas_texto:
    linha = linha.strip()
    if padrao_inicio_item.match(linha):
        if linha_temp:
            registros.append(' '.join(linha_temp))
            linha_temp = []
        linha_temp.append(linha)
    elif linha_temp:
        linha_temp.append(linha)

if linha_temp:
    registros.append(' '.join(linha_temp))

df = pd.DataFrame(registros, columns=["Linha Completa"])
df.to_excel("tabela_extraida.xlsx", index=False)

doc.close()
print("Tabela extraída com sucesso.")
