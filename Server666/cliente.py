import socket

# Configuração do servidor (localhost e porta 666)
SERVER_IP = "127.0.0.1"  # Ou substitua pelo IP do servidor remoto
PORT = 666

# Cria um socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conecta ao servidor
    client_socket.connect((SERVER_IP, PORT))
    print(f"[+] Conectado ao servidor {SERVER_IP}:{PORT}")

    # Recebe a resposta do servidor
    response = client_socket.recv(1024)  # Recebe até 1024 bytes
    print("[+] Mensagem do servidor:", response.decode())

except ConnectionRefusedError:
    print("[-] Não foi possível conectar ao servidor. Verifique se ele está rodando.")

finally:
    # Fecha a conexão
    client_socket.close()
    print("[+] Conexão encerrada.")
