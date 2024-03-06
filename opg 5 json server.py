from socket import *
import json
import random

def process_json(json_data):
    try:
        method = json_data.get("method")
        tal1 = json_data.get("Tal1")
        tal2 = json_data.get("Tal2")

        if method == "1":
            result = random.randint(min(tal1, tal2), max(tal1, tal2))
        elif method == "2":
            result = tal1 + tal2
        elif method == "3":
            result = tal1 - tal2
        else:
            result = "Unknown command"

        return {"result": result}

    except (ValueError, TypeError):
        return {"error": "Invalid command format"}

def start_server():
    server_port = 12000
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print('Server is ready')

    while True:
        connection_socket, addr = server_socket.accept()
        print(f"Connection from {addr} accepted")

        while True:
            data = connection_socket.recv(1024).decode()
            if not data or data.lower() == "exit":
                print("Connection closed")
                break

            try:
                json_data = json.loads(data)
                response = process_json(json_data)

                json_response = json.dumps(response)

                connection_socket.send(json_response.encode())

            except json.JSONDecodeError:
                error_response = {"error": "Invalid JSON format"}
                connection_socket.send(json.dumps(error_response).encode())

        connection_socket.close()

if __name__ == "__main__":
    start_server()
