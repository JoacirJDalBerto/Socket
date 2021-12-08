#Chat
#Utilizando os códigos disponibilizados em python, fazer um chat, com 
# login, e quando um novo usuário se conectar ao server, replicar nos outros 
# clientes o nome deste novo usuário, permitindo iniciar uma conversa entre qualquer
#  usuário, desde que selecionem um contato para conversar.

#Permitir envio de comandos remotos, como por exemplo, criar arquivos, reiniciar
#  o computador.

#Permitir criar arquivos e colocar o conteúdo no arquivo de forma remota, permitindo 
# acesso simultâneo.

#O socket deverá ser fullduplex (ida e volta de texto simultâneo).

import socket
import random
import index
from threading import Thread
from datetime import datetime
from colorama import Fore,init, Back


# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
        Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
        Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
        Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
        ]
# choose a random color for the client
client_color = random.choice(colors)

# prompt the client for a name
arq = open('registrados.txt', 'a')
print('Olá, aqui você pode adicionar uma nova conta!')
nome_usuario = input('Digite o nome de usuário: ')
arq.write('{}\n'.format(nome_usuario))
print('Cadastro realizado com sucesso!\n')
arq.close() #O arquivo é fechado do modo de adição para ser aberto
            #posteriormente no modo de leitura

arq = open('registrados.txt') #abrindo no modo de leitura
print('Efetue o seu login')
nome_login = input('Digite o seu nome de usuario: ')

registrados = arq.readlines()
if nome_login + '\n' in registrados:
    print('Bem vindo, {}!'.format(nome_login))
else:
    print('Você deve ter digitado seu nome de usuario errado, por favor verifique.')
arq.close()


def listen_for_messages():
    while True:
        message = index.s.recv(1024).decode()
        print("\n" + message)


# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()
while True:
    # input message we want to send to the server
    to_send = input()
    # a way to exit the program
    if to_send.lower() == 'q':
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {nome_login}{index.separator_token}{to_send}{Fore.RESET}"
    # finally, send the message
    index.s.send(to_send.encode())

# close the socket
index.s.close()
open("main.py","r")
