import socket
from datetime import datetime
import json
from urllib import request
import smtplib

pc_nome = socket.gethostname()
jsn= json.loads(request.urlopen('http://ip-api.com/json').read().decode())
ip_externo = jsn['query']
remetente = 'monitoramento@gmail.com'
passwd = 'Sua_Senha'
destinatario = 'anderson@gmail.com'
msg = '''From: <remetente>
To: <destino>
Subject: {nome} {data}

IP Atual: {ip}''' .format(nome = pc_nome, data = str(datetime.today()).split('.')[0], ip = ip_externo)

server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(remetente, passwd)
server.sendmail(remetente, destinatario, msg)
server.quit()

print('E-mail enviado')
