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

    # Aceitar a conexão
    con, add = s.accept()

    # Receber dados
    numero = con.recv(1024).decode()
    tamanho = con.recv(1024).decode()
    sabor = con.recv(1024).decode()
    bebida = con.recv(1024).decode()
    obs = con.recv(1024).decode()

    # Avisa que alguém mandou
    print("Ip: " + add[0] + " conectou")

    # Verifica se o pedido é válido
    print(numero)
    print(tamanho)
    print(sabor)
    print(bebida)
    print(obs)

    # Escreve o pedido
    with open("Pedidos.txt", "a") as f:
        f.write("Ip: " + add[0] + "\n" + tamanho + "\n" + sabor + "\n" + bebida + "\n" + obs + "\n\n")

    # Fecha a conexão
    con.close()
