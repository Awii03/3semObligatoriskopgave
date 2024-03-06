from socket import*

def get_user_input(command):
    num1 = input ("Enter the first number for:")
    num2 = input ("Enter the second number for: ")
    return f"{command} {num1} {num2}"

def display_menu():
    print("\nChoose an operation:")
    print("1.Random")
    print("2.Add")
    print("3.Subtract")
    return input ("vælg tal mellem 1 til 4): ")

server_adresse = "localhost"
server_port = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_adresse, server_port))

with socket(AF_INET, SOCK_STREAM) as client_socket:
    client_socket.connect((server_adresse, server_port))

while True:
    user_choice = display_menu()
    
    if user_choice == '4':
        print("Lukker klienten...")
        break  
    elif user_choice in ['1', '2', '3']:
        sentence = get_user_input(user_choice)
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From server:', modifiedSentence.decode())
    else:
        print("Forkert valg. Vælg tal fra 1 til 4.")

clientSocket.close()