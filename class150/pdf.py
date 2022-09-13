import PyPDF2
import os

''' # juntando PDFS
caminho_pdf = '/home/gustavo-pop/projetos/cursopython/class150/pdfs/'
novo_pdf = PyPDF2.PdfFileMerger()

for raiz, diretorios, arquivos in os.walk(caminho_pdf):
    for arquivo in arquivos:
        cam_completo_arq = os.path.join(raiz, arquivo)
        print(cam_completo_arq)

        with open(cam_completo_arq, 'rb') as pdf: # lendo em modo binario 
            novo_pdf.append(pdf)

with open(f'{caminho_pdf}/novo_pdf.pdf', 'wb') as pdf_gerado: # escrevendo em modo binario
    novo_pdf.write(pdf_gerado)
    '''

with open('/home/gustavo-pop/projetos/cursopython/class150/pdfs/novo_pdf.pdf', 'rb') as arq_pdf:
    leitor = PyPDF2.PdfFileReader(arq_pdf) # lendo pdf
    num_paginas = leitor.getNumPages() # obtem o numero de pages de um pdf

    for pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(pagina)
        escritor.addPage(pagina_atual)

        with open(f'/home/gustavo-pop/projetos/cursopython/class150/novos-pdfs/{pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)