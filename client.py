
import socket
import threading

class ChatClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = ""
        self.running = True
        
    def connect(self, host, port):
        try:
            self.client_socket.connect((host, port))
            self.display_welcome()            
            self.nickname = input("Specify a nick name: ")
            self.client_socket.send(self.nickname.encode('utf-8'))

            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()
            
            self.send_messages()
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.client_socket.close()
    
    def display_welcome(self):
        print("\n--------------------")
        print("Welcome to Chatbox!")
        print("--------------------")
        print("\nPlease Use the Following Message format:")
        print("\n@nick name: \"Your message\"")
        print("\nPress 'Ctrl+C' to disconnect from the server")
        print("--------------------")
    
    def receive_messages(self):
        try:
            while self.running:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(message)
        except:
            pass
    
    def send_messages(self):
        try:
            while self.running:
                message = input(">> ")
                if message.lower() == 'exit':
                    break
                self.client_socket.send(message.encode('utf-8'))
        except KeyboardInterrupt:
            print("Successfully disconnected from chat server")
            self.running = False
        except Exception as e:
            print(f"Error sending message: {e}")
    
    def disconnect(self):
        print("Successfully disconnected from chat server")
        self.running = False
        self.client_socket.close()

if __name__ == "__main__":
    client = ChatClient()
    
    print("Enter Server's IP:", end=" ")
    host = input().strip()
    
    print("Enter Connecting Port:", end=" ")
    port = int(input().strip())
    
    client.connect(host, port)