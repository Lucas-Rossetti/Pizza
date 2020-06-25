# -*- coding: utf-8 -*-
import socket

def tudo():
    # Define o host e a porta a se conectar
    host = '127.0.0.1'
    port = 3333

    # Cria o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Pega todas as informações necessárias

    # Se conecta
    s.connect((host, port))

    # Escreve as informações

    # Tamanhos
    numero_tamanho = int(s.recv(1024).decode())
    s.send("recebido".encode('utf-8'))

    with open("tamanhos.txt", "w+") as f:
        for t in range(numero_tamanho):
            f.write(s.recv(1024).decode())
            s.send("recebido".encode('utf-8'))

    # Sabores
    numero_sabor = int(s.recv(1024).decode())
    s.send("recebido".encode('utf-8'))

    with open("sabores.txt", "w+") as f:
        for t in range(numero_sabor):
            f.write(s.recv(1024).decode())
            s.send("recebido".encode('utf-8'))

    # Bebidas
    numero_bebida = int(s.recv(1024).decode())
    s.send("recebido".encode('utf-8'))

    with open("bebidas.txt", "w+") as f:
        for t in range(numero_bebida):
            f.write(s.recv(1024).decode())
            s.send("recebido".encode('utf-8'))

    # Endereço do server
    host_s = s.recv(1024).decode().rstrip()
    s.send("recebido".encode('utf-8'))
    port_s = int(s.recv(1024).decode().rstrip())
    s.send("recebido".encode('utf-8'))

    s.close()

    # Limpa os pedidos anteriores
    limpa = open("pedido.txt", "w+")
    limpa.close()

    # Lê todos os arquivos

    # Abre o arquivo dos tamanhos
    with open("tamanhos.txt", "r") as f:
        # Lê o arquivo e guarda numa variável
        read_1 = f.readlines()
        td = 4

    # Abre o arquivo dos sabores
    with open("sabores.txt", "r") as f:
        # Lê o arquivo e guarda numa variável
        read_2 = f.readlines()

    # Abre o arquivo das bebidas
    with open("bebidas.txt", "r") as f:
        # Lê o arquivo e guarda numa variável
        read_3 = f.readlines()

    # Pedido

    # Função para específicar o tamanho da pizza
    def tamanho_func():
        td = 4
        # Escreve na tela os tamanhos disponíveis
        for index, line in enumerate(read_1):
            td += 2
            print(index+1, "-", line.rstrip(), td, "fatias")

        # Pega o input do usuário
        try:
            # Cria a global do tamanho
            tamanho = int(input("Tamanho da pizza: "))
            with open("pedido.txt", "a") as write_tamanho:
                write_tamanho.write(read_1[tamanho-1])

        except:
            # Se der um erro, foi porque o usuário escreveu uma opção errada
            print("Opção inválida")
            tamanho_func()

    # Função para específicar o(s) sabor(es) da pizza
    def sabor_func():
        # Escreve na tela os tamanhos disponíveis
        for index, line in enumerate(read_2):
            print(index+1, line.rstrip())

        # Pega o input do usuário
        try:
            n_a = int(input("0. Vários sabores ou 1. um sabor: "))

            if n_a:
                sabor = int(input("Sabor da pizza: "))
                with open("pedido.txt", "a") as write_sabor:
                    write_sabor.write(read_2[sabor-1]) 
                
            else:
                n_s = int(input("Número de sabores: "))

                if n_s <= 3:
                    sabor = int(input("Sabores da pizza (separe com espaços. Ex.: 1 3 5): ")).split()
                else:
                    print("Número muito grande")
                    sabor_func()
        except:
            print("Opção inválida")
            sabor_func()

    # Função para específicar a(s) bebida(s)
    def bebidas_func():
        # Escreve na tela as bebidas disponíveis
        for index, line in enumerate(read_3):
            print(index+1, line.rstrip())

        # Pega o input do usuário
        try:
            bebida = int(input("Bebida: "))
            with open("pedido.txt", "a") as write_bebida:
                    write_bebida.write(read_3[bebida-1])

        except:
            print("Opção inválida")
            bebidas_func()

    # Função que envia os dados do pedido
    def enviar():

        # Cria o socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Se conecta
        s.connect_ex((host_s, port_s))

        # Envia os dados
        s.send(str(numero).encode())
        with open("pedido.txt", "r") as f:
            read = f.readlines()
            for line in read:
                s.send(line.encode('utf-8'))
                print(s.recv(1024).decode())
        exit()
        
    # Confirma o pedido
    def confirmar():
        with open("pedido.txt", "r") as f:
            read = f.readlines()

            for line in read:
                print(line.rstrip())

            print("\n1. O pedido está correto")
            print("0. Refazer pedido")

            #try:
            confirm = int(input("Confirmar: "))
            if confirm:
                enviar()
            else:
                tudo()

            #except:
                #print("Opção inválida")
                #confirmar()


    # Define o número de pizzas
    def n():
        try:
            global numero
            numero = int(input("Número de pizzas: "))
            # Vê se o número é válido
            if numero > 0:
                pass

            else:
                print("Número inválido")
                n()
        except:
            print("Número inválido")
            n()
            
    # Chama a função do número
    n()
    # Chama as funções
    for main_number in range(numero):
        # Abre o arquivo de pedido
        with open("pedido.txt", "a") as f:
            # Escreve o tamanho da pizza atual
            f.write("Pizza " + str(main_number + 1) + "\n")
        tamanho_func()
        sabor_func()
        bebidas_func()
        if main_number+1 == numero:
            confirmar()
            enviar()
        
        else:
            pass

tudo()