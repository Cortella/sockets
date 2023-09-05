# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:59:40 2023

@author: Cortella
"""

import socket

LOCALHOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def pong(porto_pong, string_pong):
    # Cria um socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        # Liga o socket UDP ao porto_pong
        udp_socket.bind((LOCALHOST, porto_pong))
        while True:
            # Espera uma mensagem msg_de_ping no socket UDP
            msg_de_ping, addr = udp_socket.recvfrom(1024)

            # Extrai o endereço end_ping e porto_ping da mensagem
            end_ping, porto_ping = addr
        
            # Cria um socket TCP
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
            
            
                # Conecta o socket TCP com (end_ping, porto_ping)
                tcp_socket.connect((end_ping, porto_ping))

                # Monta a mensagem msg_de_pong
                msg_de_pong = f"{string_pong}\n"

                # Envia a mensagem msg_de_pong pela conexão TCP
                tcp_socket.send(msg_de_pong.encode())
            except Exception as e:
                # Lidar com exceções aqui, como imprimir o erro
                print(f"Ocorreu um erro: {str(e)}")
                break
            
            finally:
                # Fecha a conexão TCP
                tcp_socket.close()
            

string_pong = "Mensagem de Pong"

pong(PORT, string_pong)