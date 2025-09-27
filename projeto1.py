import PyPDF2  # Importa a biblioteca PyPDF2 para manipulação de arquivos PDF
import os  # Importa a biblioteca os para interagir com o sistema de arquivos

# Cria um objeto PdfMerger para mesclar arquivos PDF
merger = PyPDF2.PdfMerger()

# Lista todos os arquivos dentro da pasta 'arquivos'
lista_arquivos = os.listdir('arquivos')

# Ordena a lista de arquivos em ordem alfabética
lista_arquivos.sort()

# Exibe a lista de arquivos encontrados na pasta
print(lista_arquivos)

# Percorre cada arquivo na lista
for arquivo in lista_arquivos:
    # Verifica se o arquivo tem a extensão '.pdf'
    if arquivo.endswith('.pdf'):
        # Adiciona o arquivo PDF ao objeto merger
        merger.append(f'arquivos/{arquivo}')

# Salva o arquivo PDF mesclado com o nome 'merged.pdf' na pasta 'arquivos'
merger.write('arquivos/merged.pdf')

# Fecha o objeto merger para liberar recursos
merger.close()

# Exibe uma mensagem indicando que os PDFs foram mesclados com sucesso
print('PDFs mesclados com sucesso em "arquivos/merged.pdf"')