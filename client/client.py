import socket

# Define o host e a porta a se conectar
host = '127.0.0.1'
port = 8734

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o número de pizzas
numero = int(input("Número de pizzas: "))
for a in range(numero):
# Função para específicar o tamanho da pizza
    def tamanho_func():

        # Abre o arquivo dos tamanhos
        with open("tamanhos.txt", "r") as f:

            # Lê o arquivo e guarda numa variável
            global read_1
            read_1 = f.readlines()
            td = 4

            # Escreve na tela os tamanhos disponíveis
            for index, line in enumerate(read_1):
                td += 2
                print(index+1, line.rstrip(), td, "fatias")

            # Pega o input do usuário
            try:
                # Cria a global do tamanho
                global tamanho
                tamanho = int(input("Tamanho da pizza: "))

            except:
                # Se der um erro, foi porque o usuário escreveu uma opção errada
                print("Opção inválida")
                tamanho_func()

        # Abre o arquivo de pedido
        with open("pedido.txt", "a") as f:

            # Escreve o tamanho da pizza atual
            f.write("Pizza " + str(a))
    # Função para específicar o(s) sabor da pizza
    def sabor_func():

        # Abre o arquivo dos sabores
        with open("sabores.txt", "r") as f:
            global read_2
            read_2 = f.readlines()
            global sabor

            # Escreve na tela os tamanhos disponíveis
            for index, line in enumerate(read_2):
                print(index+1, line.rstrip())

            # Pega o input do usuário
            try:
                global n_a
                n_a = int(input("0. Vários sabores ou 1. um sabor: "))

                if n_a:
                    sabor = int(input("Sabor da pizza: "))

                else:
                    global n_s
                    n_s = int(input("Número de sabores: "))

                    if n_s <= 3:
                        sabor = int(input("Sabores da pizza (separe com vírgulas. Ex.: 1, 3, 2): ")).split()
                    else:
                        print("Número muito grande")
                        sabor_func()
            except:
                print("Opção inválida")
                sabor_func()

    def bebidas_func():
        with open("bebidas.txt", "r") as f:
            global read_3
            read_3 = f.readlines()

            for index, line in enumerate(read_3):
                print(index+1, line.rstrip())

            try:
                global n
                n = int(input("Bebida: "))
                bebida = read_3[n]

            except:
                print("Opção inválida")
                bebidas_func()

    def enviar():

        # Se conecta
        s.connect_ex((host, port))

        # Envia os dados
        s.send(read_1[tamanho-1].encode())
        s.send(n_s.encode())
        if n_a:
            s.send(read_2[sabor-1].encode())

        else:
            for q in range(n_s):
                s.send(read_2[q-1].encode())
        s.send(read_3[n-1].encode())

    # Chama as funções
    tamanho_func()
    sabor_func()
    bebidas_func()
    enviar()
