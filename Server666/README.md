# CyberTestTools - TCP Port Listener 666

## 📌 Descrição

Este projeto contém **um servidor e um cliente TCP simples** para testes de conectividade, monitoramento de portas e experimentos de cibersegurança.

O objetivo é fornecer uma ferramenta leve para:
- **Testar conexões TCP/IP** em redes locais e remotas.
- **Simular um serviço** escutando em uma porta específica.
- **Monitorar acessos** a portas específicas, como a porta 666.
- **Validar firewall** e regras de roteamento.

Esta ferramenta faz parte da **plataforma Hackers Hive** e foi desenvolvida para fins educacionais e de pesquisa em segurança cibernética.

---

## 🚀 Como Funciona?

O projeto inclui dois scripts principais:

### 1️⃣ Servidor TCP (`port_listener.py`)
- Abre uma **porta TCP (666)** e entra no **modo de escuta**.
- Aceita conexões de clientes e **exibe o IP e a porta do remetente**.
- Envia uma **mensagem de boas-vindas** ao cliente conectado.
- Fecha a conexão logo após o envio da resposta.

### 2️⃣ Cliente TCP (`cliente.py`)
- Se conecta ao **servidor na porta 666**.
- Aguarda a resposta do servidor e a exibe no terminal.
- Fecha a conexão após receber a mensagem.

O servidor pode ser rodado **em qualquer máquina**, e o cliente pode se conectar a ele **de outro dispositivo ou da mesma máquina**.

---

## 🛠️ Como Usar

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seuusuario/CyberTestTools.git
cd CyberTestTools/tcp_listener
```

### 2️⃣ Iniciar o Servidor
Execute o seguinte comando para iniciar o servidor e escutar na porta **666**:
```bash
python3 port_listener.py
```
**Saída esperada:**
```
[*] Servidor escutando na porta 666...
```

### 3️⃣ Executar o Cliente
Abra um novo terminal e execute:
```bash
python3 cliente.py
```
Se a conexão for bem-sucedida, a saída será:
```
[+] Conectado ao servidor 127.0.0.1:666
[+] Mensagem do servidor: Bem-vindo ao servidor na porta 666!
[+] Conexão encerrada.
```

### 4️⃣ Testar a Conexão com Netcat
Se preferir, você pode testar o servidor com o **Netcat** (`nc`):
```bash
nc localhost 666
```
Isso simula um cliente TCP e permite interagir manualmente com o servidor.

---

## 📂 Estrutura do Repositório

```
CyberTestTools/
│── README.md         # Documentação do projeto
│── port_listener.py  # Servidor TCP - Escuta conexões na porta 666
│── cliente.py        # Cliente TCP - Conecta ao servidor e recebe resposta
│── docs/             # Documentação adicional
```

---

## 🛡️ Casos de Uso

✔ **Testes de firewall** – Verifique se a porta 666 está acessível na rede.  
✔ **Simulação de serviços** – Execute o servidor para testar conexões remotas.  
✔ **Análise de tráfego de rede** – Utilize ferramentas como **Wireshark** para capturar pacotes.  
✔ **Validação de regras de bloqueio** – Teste permissões de entrada e saída na rede.  

---

## ⚠️ Aviso

Este projeto deve ser utilizado **somente para fins educacionais e testes autorizados**.  
O uso indevido em redes sem permissão pode ser considerado **atividade ilegal**.  

---

## 📢 Contribuições

Quer contribuir?
- Relate **bugs** e envie sugestões na aba **Issues**.
- Faça um **fork** do repositório e envie um **Pull Request**.

---

## 🔗 Referências

- [Documentação do Python Socket](https://docs.python.org/3/library/socket.html)  
- [Uso do Netcat para Testes de Conexão](https://www.redhat.com/sysadmin/netcat-cheat-sheet)  
- [Hackers Hive - Plataforma de Segurança Cibernética](https://hackershive.io/)  

Criado para fins de pesquisa e aprendizado dentro da **Hackers Hive**. Utilize com responsabilidade.
