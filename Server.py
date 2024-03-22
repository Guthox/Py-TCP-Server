import socket

porta = 7777
host = "192.168.10.83"

def iniciar_servidor():
    
    # Cria um socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Vincula o socket à porta
    servidor.bind((host, porta))
    
    # Define o limite de conexões pendentes
    servidor.listen(5)
    
    print(f"Servidor TCP iniciado na porta {porta}")

    while True:
        # Aguarda a conexão de um cliente
        print("Conexão aberta")
        print("Esperando cliente")
        conexao, endereco = servidor.accept()
        conexao.settimeout(5)
        print(f"Cliente conectado: {endereco}")
        # Recebe a mensagem do cliente
        print("Esperando mensagem")
        try:
            mensagem = conexao.recv(64).decode()
            if not mensagem:
                conexao.close()
                break
            print("Mensagem recebida:", mensagem)
        except:
            print("Timeout atingido.")
                
        # Fecha a conexão com o cliente
        conexao.close()
        print("Conexão fechada")
        print("#"*20)

while True:
    try:
        iniciar_servidor()
    except:
        pass