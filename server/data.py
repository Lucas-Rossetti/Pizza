# -*- coding: utf-8 -*-
import socket

# Define o host e a porta para rodar o servidor
host = '127.0.0.1'
port = 3333

# Pegar informações

# Tamanhos
with open("tamanhos.txt", "r") as f_tamanho:
    read_tamanho = f_tamanho.readlines()
    numero_tamanho = len(read_tamanho)

# Sabores
with open("sabores.txt", "r") as f_sabor:
    read_sabor = f_sabor.readlines()
    numero_sabor = len(read_sabor)

# Bebidas
with open("bebidas.txt", "r") as f_bebida:
    read_bebida = f_bebida.readlines()
    numero_bebida = len(read_bebida)

# Endereço do server
with open("host.txt", "r") as f_server:
    read_server = f_server.readlines()
    numero_server = len(read_server)

while 1:
    # Cria o socket e reusa o mesmo endereço
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Roda o servidor
    s.bind((host, port))
    s.listen(10)

    # Escreve "Rodando..."
    print("Rodando...")

    # Aceitar a conexão
    con, add = s.accept()

    # Enviar informações

    # Tamanhos
    con.send(str(numero_tamanho).encode('utf-8'))
    print(con.recv(1024).decode())

    for i in range(numero_tamanho):
        con.send(read_tamanho[i].encode('utf-8'))
        print(con.recv(1024).decode())

    # Sabores
    con.send(str(numero_sabor).encode('utf-8'))
    print(con.recv(1024).decode())

    for i in range(numero_sabor):
        con.send(read_sabor[i].encode('utf-8'))
        print(con.recv(1024).decode())

    # Bebidas
    con.send(str(numero_bebida).encode('utf-8'))
    print(con.recv(1024).decode())

    for i in range(numero_bebida):
        con.send(read_bebida[i].encode('utf-8'))
        print(con.recv(1024).decode())

    # Endereço do server
    for i in range(numero_server):
        con.send(read_server[i].encode('utf-8'))
        print(con.recv(1024).decode())
        
    # Fecha a conexão
    con.close()