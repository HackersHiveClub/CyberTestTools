import socket

# Define a porta a ser usada
PORT = 666

# Cria um socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permite a reutilização do endereço para evitar erros ao reiniciar o script
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associa o socket ao endereço local na porta 666
server_socket.bind(("0.0.0.0", PORT))

# Coloca o socket no modo de escuta, aceitando conexões
server_socket.listen(5)

print(f"[*] Servidor escutando na porta {PORT}...")

while True:
    # Aceita conexões de clientes
    client_socket, addr = server_socket.accept()
    print(f"[+] Conexão recebida de {addr[0]}:{addr[1]}")

    # Envia uma resposta para o cliente
    client_socket.send(b"Bem-vindo ao servidor na porta 666!\n")

    # Fecha a conexão com o cliente
    client_socket.close()
