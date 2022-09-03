from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os

minha_senha = 'Repositorio12#'
meu_email = 'gustavofeliperepositorio@gmail.com'

BASE_DIR = os.path.dirname(os.path.realpath(__name__))

with open(f'{BASE_DIR}/class141/template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Gustavo Felipe', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Gustavo Felipe'
msg['to'] = 'gustavofelipe2730@gmail.com'  # Cliente
msg['subject'] = 'E-MAIL TESTE'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
# with open('IMAGEM.JPG', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso.')
