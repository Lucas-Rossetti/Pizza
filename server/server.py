# -*- coding: utf-8 -*-
import socket

# Define o host e a porta para rodar o servidor
host = '127.0.0.1'
port = 8734


while 1:
    # Cria o socket e reusa o mesmo endereço
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Roda o servidor
    s.bind((host, port))
    s.listen(10)

    # Escreve que está rodando
    print("Rodando...")

    # Aceitar a conexão
    con, add = s.accept()

    # Escreve quem se conectou
    print(add[0], "se conectou")

    # Recebe e escreve dados
    numero = int(con.recv(1024).decode())
    print(numero, "Número")
    with open("Pedidos.txt", "a") as f:
        f.write("Ip: " + add[0] + "\n")
        for i in range(numero*4):
            print("Chegou no loop")
            data = con.recv(1024).decode()
            print(data)
            f.write(data)
            con.send("recebido".encode('utf-8'))
        print("Terminou o loop")
    # Fecha a conexão
    con.close()