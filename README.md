# Pizza
Dois programas (um cliente e dois servidores) para pedir pizza

# Como utilizar
Primeiro, no computador da pizzaria, execute os dois programas python na pasta server
O data.py é um server que fornece ao cliente todas as informações sobre sabores, bebidas, etc...
O server.py é o que pega os pedidos após o cliente finalizar

Depois, é só o cliente executar o client.py (na pasta client) e deu! Pode fazer seu pedido

# Bugs e atualizações futuras
1. Colocar a opção de não pedir nenhuma bebida
2. Colocar para funcionar o pedido de pizza de mais de um sabor
3. Uma versão gráfica com tkinter

# Observações
Não é preciso copiar nenhum arquivo de texto para o cliente, o programa client automaticamente cria eles
Para mudar o cardápio, edite os arquivos de texto respectivos de cada tópico. Se quer adicionar uma bebida pepsi, coloque no arquivo "bebidas.txt", e depois de arrumas tudo do cardápio, execute o data.py. Ele lê os arquivos apenas uma vez, quando é executado. Então se ele estiver rodando e você mudar o cardápio, não mudará nada para os clientes
