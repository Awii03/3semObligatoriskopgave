from socket import *
import json

def get_user_input(command):
    num1 = input(f"Enter the first number for {command}: ")
    num2 = input(f"Enter the second number for {command}: ")
    return {"method": command, "Tal1": float(num1), "Tal2": float(num2)}

def display_menu():
    print("\nChoose an operation:")
    print("1. Random")
    print("2. Add")
    print("3. Subtract")

server_address = 'localhost'
server_port = 12000

with socket(AF_INET, SOCK_STREAM) as client_socket:
    client_socket.connect((server_address, server_port))

    while True:
        display_menu()
        user_choice = input("Enter the number of your choice (1-3), or 'q' to quit: ")

        if user_choice.lower() == 'q':
            print("Closing the client...")
            break
        elif user_choice in ['1', '2', '3']:
            operation = get_user_input(user_choice)

            # Convert the operation dictionary to a JSON string
            json_operation = json.dumps(operation)

            client_socket.send(json_operation.encode())
            result = client_socket.recv(1024).decode()

            # Parse the JSON result
            json_result = json.loads(result)

            if 'result' in json_result:
                print(f'Result from server: {json_result["result"]}')
            elif 'error' in json_result:
                print(f'Error from server: {json_result["error"]}')
        else:
            print("Invalid choice. Please choose a number from 1 to 3, or 'q' to quit.")
