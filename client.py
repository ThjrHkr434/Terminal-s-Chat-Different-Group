import pyfiglet
import time
import threading
import sys
import socket
import os
import platform

os.system('cls' if os.name == 'nt' else 'clear')

try:
    while True:
        print(f'\033[32m+{"-"*100}+\n{pyfiglet.figlet_format(text="Grupo Diferente",font="bloody")}\n+{"-"*41}O chat mais brarbo{"-"*41}+\033[m')
        # Variáveis booleanas

        acc = False
        executando = True

        # Funções

        def mostrar_info():
            print(f"+{'-'*70}+\n[!] INFORMAÇÕES DO USUÁRIO:\n  > Sistema: {platform.system()}\n  > Hostname: {socket.gethostname()}\n  > Arquitetura: {platform.architecture()}\n  >  Processador: {platform.processor()}\n  > Diretório atual: {os.getcwd()}\n+{'-'*70}+\n  > Código de entrada: {num}\n  > Status - Autenticado\n+{'-'*70}+\n  > Versão do chat: v1.5\n  > Conectado em 192.168.3.49:5050\n  > Criado por @caraaleatorio456.\n+{'-'*70}+")
        
        def sobre():
            print(f"+{'-'*70}+\nSobre o Terminal's Chat:\n  > Criado por: @caraaleatorio456\n  > Missão: Proteger os membros do FBI e fornecer um chat secreto\n  > Funcionamento: Este terminal permite que membros autorizados conversem em tempo real com segurança e privacidade.\n  > Conceito: Inspirado em grupos secretos como fSociety e DedSec, o Grupo Diferente é uma rede de comunicação entre mentes brilhantes e inconformadas com João Marcus.\n+{'-'*70}+\n  > Tecnologia usada: Python\n  > Sockets(TCP/IP)\n  > Threads\n  > PyFiglet\n+{'-'*70}+\nIMPORTANTE: Código em constante atualização!\n+{'-'*70}+")
        
        def ajuda():
            print(f"╔{"═"*44}╗")
            print(f"║{" "*12}COMANDOS DISPONÍVEIS{" "*12}║")
            print(f"╠{"═"*44}╣")
            print(f"║ /ajuda         -> Mostra essa mensagem   ║")
            print(f"║ /logout        -> Sai do chat            ║")
            print(f"║ /limpar        -> Limpa a tela           ║")
            print(f"║ /sobre         -> Informações do grupo   ║")
            print(f"║ /info          -> Informações do usuário ║")
            print(f"╚{"═"*44}╝")
        def receber():
            while True:
                try:
                    msg = s.recv(1024).decode()
                    print(f'{msg}')
                except:
                    print(f"[!] Conexão encerrada pelo servidor!")
                    break


        def loader(text):
            barra = ['\\','|','/','-']
            i = 0
            while executando:
                sys.stdout.write("\r" + f"[{barra[i]}]{text}")
                sys.stdout.flush()
                i = (i + 1) % len(barra)
                time.sleep(.5)

        # Conexão com servidor
        while True:
            executando = True
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            thread = threading.Thread(target=loader,args=("Fazendo conexão com o servidor",))
            thread.start()

            conn = s.connect_ex(("192.168.3.49",5050))
            time.sleep(1)
            if conn == 0:
                executando = False
                thread.join()
                sys.stdout.write("\r" + f"\033[32m[+] Conexão feita com sucesso!{' '*30}\033[m\n")
                sys.stdout.flush()
                
                break
            else:
                executando = False
                thread.join()
                sys.stdout.write("\r" + f"\033[31m[-] Conexão não feita!{' '*30}\033[m")
                sys.stdout.flush()
                p = input("\033[1;33m\n[?] Deseja tentar novamente[S/N]? \033[m").upper()
                if p == "N":
                    raise SystemExit("Saindo..")
                
        # Código principal

        
        num = str(input(("[:)] Bem vindo cara, se vc entrou é pq vc ta no grupo diferente 2.0 e quer se proteger do FBI, para começar, identifique-se com seu número de entrada[0 para sair]: ")))
        if not num:
            raise SystemExit()
        elif num == "0":
            raise SystemExit()
        else:
            s.send(num.encode())
            acc = s.recv(1024).decode()
            
        
        if acc == "True":
            thread_recv = threading.Thread(target=receber)
            thread_recv.daemon = True
            thread_recv.start()

            while True:
                try:
                    msg = str(input(""))
                    if msg.lower() == "/logout":
                        raise SystemExit()
                    elif msg.lower() == "/ajuda":
                        ajuda()
                    elif msg.lower() == "/limpar":
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif msg.lower() == "/info":
                        mostrar_info()
                    elif msg.lower() == "/sobre":
                        sobre()
                    else:
                        s.send(msg.encode())
                except:
                    print("\n[!] Erro ao enviar mensagem. Conexão encerrada!")
                    break

        else:
            raise PermissionError("Vc n tem permissão para entrar no terminal's chat do grupo diferente!")
        
# Tratamento de erros:

except Exception as e:
    print(f'\033[1;31m[!!] Houve um erro durante a execução do código: \033[1;33m{e}\033[m')
except SystemExit:
    print('\033[31m[-] Vc saiu.\033[m')
finally:
    print("\n[+] Até mais companheiro")
    s.close()