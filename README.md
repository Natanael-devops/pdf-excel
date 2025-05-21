# Extração de Texto de PDF com Corte por Região Usando PyMuPDF
Este script Python extrai texto de uma região específica de um arquivo PDF, respeitando coordenadas horizontais (x0 e x1), para evitar que textos indesejados apareçam na extração. O texto extraído é agrupado por linhas e registros, e exportado para uma planilha Excel.

## Pré-requisitos
Python 3.x

Bibliotecas Python:

PyMuPDF (instalado via pip install pymupdf)

pandas (instalado via pip install pandas)

openpyxl (para salvar arquivos Excel, pip install openpyxl)



## Como usar
1.Coloque o arquivo PDF na pasta input (ou ajuste o caminho no código).

2. Ajuste o retângulo de recorte (rect) para a área desejada, definindo coordenadas x0, y0, x1, y1.

3. Execute o script Python.

4. O arquivo tabela_extraida.xlsx será gerado com o texto extraído da área especificada.

# Explicação do código
O PDF é aberto com PyMuPDF (fitz).

O método page.get_text("words") extrai as palavras com suas coordenadas.

São filtradas as palavras que estão dentro do retângulo definido (com base na interseção dos bounding boxes).

As palavras são agrupadas em linhas e ordenadas pela coordenada horizontal para manter a ordem do texto.

As linhas são combinadas em registros baseados no padrão regex que detecta início de um registro (números com 8 ou mais dígitos no início da linha).

O resultado é salvo em um arquivo Excel para análise e uso posterior.

# Personalização
Ajuste o valor do rect para a região da página que deseja extrair (valores em pontos, unidade padrão do PDF).

Modifique o regex padrao_inicio_item para adaptar à estrutura dos seus registros.

Altere o nome do arquivo PDF de entrada e do arquivo Excel de saída conforme necessário.


# Observações
Este método garante que apenas o texto dentro da área horizontal definida seja extraído, evitando problemas com textos que se sobrepõem fora da região desejada.

Funciona bem para PDFs onde o texto está estruturado em blocos e linhas, como tabelas ou listas.

Se precisar de ajuda para ajustar ou estender o script, é só chamar! - Natanael
