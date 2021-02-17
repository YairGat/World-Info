from Client import Client
from Server import Server


class Program:
    def __init__(self):
        self.server = Server()
        self.client = Client()
    def run(self):
        self.client.run()
        self.server.run()
program = Program()
program.run()