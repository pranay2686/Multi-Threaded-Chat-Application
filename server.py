import socket
import threading

class ChatServer:
    def __init__(self, host='0.0.0.0', port=12341):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = {} 
        
    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            
            local_ip = socket.gethostbyname(socket.gethostname())
            print("Server started!")
            print(f"IP: {local_ip}")
            print(f"Port: {self.port}")
            print("\nWaiting for clients.....")
            
            while True:
                client_socket, client_address = self.server_socket.accept()
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_handler.daemon = True
                client_handler.start()
                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.server_socket.close()
    
    def handle_client(self, client_socket, client_address):
        try:
            nickname = client_socket.recv(1024).decode('utf-8')
            self.clients[nickname] = (client_socket, client_address[0], client_address[1])            
            print(f"{nickname} , ('{client_address[0]}', {client_address[1]}) joined....")            
            self.broadcast(f"{nickname.upper()} is online now", None)       
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    raise Exception("Client disconnected")
                
                if message.startswith("@"):
                    parts = message.split(":", 1)
                    if len(parts) == 2:
                        target_nick = parts[0][1:].strip()
                        msg_content = parts[1].strip()
                        self.send_private_message(nickname, target_nick, msg_content)
                else:
                    self.broadcast(f"Message from {nickname}: {message}", nickname)
                    
        except Exception as e:
            print(f"exception occured")
            print(f"exception occured")
            # Remove client from the list and close connection
            if nickname in self.clients:
                del self.clients[nickname]
                print(f"{nickname} went offline.")
                self.broadcast(f"{nickname} is offline now", None)
            client_socket.close()
    
    def broadcast(self, message, sender):
        for nick, (client_socket, _, _) in self.clients.items():
            try:
                if nick != sender: 
                    client_socket.send(message.encode('utf-8'))
            except:
                pass
    
    def send_private_message(self, sender, target, message):
        if target in self.clients:
            target_socket = self.clients[target][0]
            try:
                target_socket.send(f"Message from {sender}: {message}".encode('utf-8'))
            except:
                pass

if __name__ == "__main__":
    server = ChatServer()
    server.start()