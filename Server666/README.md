# TCP Port Listener - Porta 666  

## 📌 Descrição  

Este é um **servidor TCP simples** que escuta conexões na **porta 666**. Ele foi desenvolvido para testes de cibersegurança e monitoramento de conexões de rede, permitindo validar se uma porta está aberta e acessível.  

O programa pode ser utilizado para:  
- **Testar conexões de entrada** em uma porta específica.  
- **Monitorar acessos remotos** à porta 666.  
- **Simular um serviço escutando conexões** para testes de firewall, IDS/IPS e análise de tráfego.  

## ⚠️ Aviso  

Este script deve ser utilizado **apenas para fins educacionais e de testes em ambientes controlados**. O uso indevido em redes sem autorização pode ser considerado **atividade ilegal**.  

---

## 🚀 Como Funciona?  

O script cria um **servidor TCP** que:  
1. **Abre a porta 666** e entra no modo de escuta.  
2. **Aceita conexões de clientes** e exibe o IP e porta do remetente.  
3. **Envia uma mensagem de boas-vindas ao cliente** conectado.  
4. **Fecha a conexão** logo após a resposta.  

---

## 🛠️ Como Executar  

### **1️⃣ Clonar o Repositório**  
```bash
git clone https://github.com/seuusuario/CyberTestTools.git
cd CyberTestTools/servidor666
python servidor.py
