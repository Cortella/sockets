# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:58:41 2023

@author: Cortella
"""

import socket

LOCALHOST = "127.0.0.1"  # Standard loopback interface address (localhost)

def ping(end_pong, porto_pong, porto_ping):
    try:
        # Cria um socket UDP e um socket TCP
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Liga o socket TCP ao porto_ping
        tcp_socket.bind(('localhost', porto_ping))

        # Prepara o socket TCP para receber conexões
        tcp_socket.listen(1)

        # Monta uma mensagem msg_de_ping
        msg_de_ping = "Mensagem de Ping"

        # Envia msg_de_ping para (end_pong, porto_pong) no socket UDP
        udp_socket.sendto(msg_de_ping.encode(), (end_pong, porto_pong))

        # Prepara para aceitar a conexão TCP vinda de pong
        conn, addr = tcp_socket.accept()

        # Espera pela msg_de_pong no socket da conexão
        msg_de_pong = conn.recv(1024).decode()

        # Exibe o conteúdo da string_pong na saída
        print("Conteúdo da mensagem de Pong:", msg_de_pong)

        # Fecha a conexão TCP
        conn.close()
    except Exception as e:
        print("Ocorreu um erro:", str(e))

if __name__ == "__main__":
    end_pong = LOCALHOST  # Endereço do servidor Pong
    porto_pong = 65432  # Porta do servidor Pong
    porto_ping = 54321  # Porta local para receber conexões TCP

    ping(end_pong, porto_pong, porto_ping)