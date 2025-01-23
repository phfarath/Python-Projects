#  1. entrada de email para verificação

#  2. verificação de caracteres

#  3. validação do email ( sim ou não )

#  4. caso válido, função para envio de mensagem

import re # para validação de emails 
import smtplib as sl # para envio de emails
from email.mime.text import MIMEText #capta as informações da mensagem 

# padrão de verificação dos caracteres do email
padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z|a-z]{2,7}\b'

# função para validação do email
def validarEmail(email):
    if re.match(padrao, email):
        print('Email Válido')
        return True
    else:
        print('Email Inválido')
        return False
    
# função para enviar mensagens 
def enviarmsg(mensagem, email, destinatario, tema, senha):

    # abrindo o servidor para GMAIL 
    servidor = sl.SMTP('smtp.gmail.com',587)
    servidor.starttls()
    servidor.login(email, senha) # xhei glln usrl aiug

    # pegando a mensagem para envio 
    msg = MIMEText(mensagem)
    msg['Subject'] = (tema)
    msg['From'] = (email)
    msg['To'] = (destinatario)

    # enviando mensagem
    servidor.sendmail(email, destinatario, msg.as_string())

    # fechando o servidor
    servidor.quit()
    
# programa principal
email = input('Digite seu email: ')
senha = input('Digite sua senha: ')
msg = input('Digite a mensagem aqui: ')
tema = input('Digite o tema da mensagem: ')
destinatario = input('Digite o email do destinatario: ')

# caso passe na validação, enviar email
if validarEmail(email) == True and validarEmail(destinatario):
    enviarmsg(msg, email, destinatario, tema, senha)
else:
    print('Email invalido, por favor tente novamente.')