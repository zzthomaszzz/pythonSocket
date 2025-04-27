import random
import socket
import threading
import pickle
from player import Player

player_list = []

def handle_client(client, address, _id):
    print(f"Accepted connection from {address}, Player id: {_id}")
    for i in player_list:
        if i.id == _id:
            client.sendall(pickle.dumps(i))
            break
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            response = process_data(pickle.loads(data), _id)
            client.sendall(pickle.dumps(response))
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        client.close()
        for i in player_list:
            if i.id == _id:
                player_list.remove(i)
        print(f"Connection with {address} closed")

def process_data(data, _id):
    if data[0] == "position":
        for i in player_list:
            if i.id == _id:
                i.set_pos(data[1])
                break
        return player_list
    else:
        return data

def start_server():
    host = ""
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()

        new_player = Player(0, 0, random.random())
        player_list.append(new_player)

        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr, new_player.id))
        client_thread.daemon = True
        client_thread.start()

if __name__ == "__main__":
    start_server()
