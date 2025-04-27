import socket
import pickle

class Client:

    def __init__(self):
        self.host = '192.168.88.14'
        self.port = 5000
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def disconnect(self):
        self.client_socket.close()
