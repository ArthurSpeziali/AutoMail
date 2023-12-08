#Importando as bibliotecas:
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cred import usuario, senha

#Criando uma função da documentação do smtplib, que manda o Email.
#Ele retorna se o destinatário tiver incorreto, e se as credenciais tiverem, ele so para o programa:
def send_email(usuario, senha, destinatario, assunto, corpo):
    error = False
    
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(usuario, senha)
        
    except smtplib.SMTPAuthenticationError:
        print('\nÚsuario/Senha incorreta. Edite o arquivo "creds.py" para o seu úsuario e senha corretos!')
        print('Saindo, depois de alterar o úsuario e senha, inicie o programa!')
        exit()
        
    text = msg.as_string()
    try:
        server.sendmail(usuario, destinatario, text)
    
    except smtplib.SMTPRecipientsRefused:
        error = True 
            
    server.quit()
    return error

#Introdução:
print('Bem vindo ao AutoMail!')
print('By: Arthur Speziali\n')
sleep(1)
print('Este programa manda 1 ou vários email para varios destinatários e etc...')
print('PS: Coloque o seu e-mail e a senha dele no creds.py, funciona com Gmail. Se der algum erro de senha, consulte na conta google "Senhas de app".')
sleep(2)
print('\nDigite "M" para escrever manualmente ou "R" para selecionar arquivos .txt e escrever automaticamente:')

#Ciclo While para calcular a opção correta:
while True:
    opção1 = input().lower().strip()
    
    if opção1 != 'm' and opção1 != 'r':
        print('Opção inválida, tente novamente!')
    else:
        break            
    

#Email manual:
if opção1 == 'm':
    
    #Pedindo as informações do Email
    destinatario = input('\nQual seria o destinarário? (john.smith@gmail.com)\n').strip().lower()
    assunto = input('\nQual seria o assunto? (Problemas com a entrega)\n').strip()
    corpo = input('\nQual seria o corpo do E-mail? (Olá, John&&Tive problemas com a entrega...) [Digite "&&" para pular uma linha!] \n').strip()
    
    #Como o "\n" em um input fica como raw, por isto esta substituição, que facilita até:
    corpo = corpo.replace('&&', '\n')
    
    #Se o úsuario desejar programar o Email, ele abrira e executará o "time_send.py":
    print('\nDeseja programar o envio desde E-mail? [S/N]')
    while True:
        wait = input()
        
        if wait == 'n' or wait == 'não' or wait == 'nao':
            break
        
        elif wait == 's' or wait == 'sim' or wait == 'y':
            
            #Como o import acaba executrando o arquivo, facilita so coloca-lo:
            import time_send
            break
        
        else:
            print('Opção inválida, tente novamente!')

    #Com o erro retornado, vê se o destinatário e usuario/senha estão coretos:
    while True:

        if send_email(usuario, senha, destinatario, assunto, corpo):
            print('\nDestinátario incorreto/inexistente, Tente novamente!')
            destinatario = input('Qual seria o destinarário? (john.smith@gmail.com)\n').strip().lower()
        
        else:
            
            print('Email enviado com sucesso!')
            break
        
        
#Email automatico:
elif opção1 == 'r':
    
    #Pede o caminho, e abri o arquivo, para verificar se ele existe:
    print('\nDigite o caminho até o .txt com a mensagem pronta (Primeira linha é o assunto):')
    while True:
        path_msg = input().strip()
        
        try:
            with open(path_msg, encoding='utf-8') as v_path:
                break
                
        except:
            print('\nCaminho mal-sucedido! Tente novamente!\n')
            
    print('\nDigite o caminho até o .txt com os E-mail para mandar:')
    while True:
        path_email = input().strip()
        
        try:
            with open(path_email, encoding='utf-8') as v_path:
                break
                
        except:
            print('\nCaminho mal-sucedido! Tente novamente!\n')    
    
    #Define a 1º linha do path_msg como o assunto, usando o readline.
    #Depois, define o corpo como todo o path_msg, mas sem o assunto:
    with open(path_msg, 'r', encoding='utf-8') as emails_msg:
        email_ass = emails_msg.readline().strip()
        email_body = emails_msg.read().replace(email_ass, '')
       
    #Transforma o path_email em uma lista:
    with open(path_email, 'r') as emails_txt:
        email_list = emails_txt.read().split('\n')
    
    print('\nDeseja programar o envio desde E-mail? [S/N]')
    while True:
        wait = input()
        
        if wait == 'n' or wait == 'não' or wait == 'nao':
            break
        
        elif wait == 's' or wait == 'sim' or wait == 'y':
            import time_send
            break
        
        else:
            print('Opção inválida, tente novamente!')

    
    print('\n')
    
    #Mostra se o Email foi enviado corretamente:
    for email in email_list:
        if send_email(usuario, senha, email, email_ass, email_body):
            print(f'Email inválido: {email}')
        else:
            print(f'Email enviado: {email}')

    print('Processo finalizado!')