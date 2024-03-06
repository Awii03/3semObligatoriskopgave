from socket import *
import random

def process_command(sentence):
    parts = sentence.split(' ')
    command = parts[0]

    try:
        num1, num2 = int(parts[1]), int(parts[2])

        if command == "1":
            result = random.randint(min(num1, num2), max(num1, num2))
        elif command == "2":
            result = num1 + num2
        elif command == "3":
            result = num1 - num2
        else:
            result = "Ukendt kommando"

        return str(result)

    except (ValueError, IndexError):
        return "Ugyldig kommandoformat"

def start_server():
    server_port = 12000
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print('Serveren er klar')

    while True:
        connection_socket, addr = server_socket.accept()
        print(f"Forbindelse fra {addr} accepteret")

        while True:
            sentence = connection_socket.recv(1024).decode()
            if not sentence or sentence.lower() == "exit":
                print("Forbindelse lukket")
                break

            response = process_command(sentence)
            connection_socket.send(response.encode())

        connection_socket.close()

if __name__ == "__main__":
    start_server()
