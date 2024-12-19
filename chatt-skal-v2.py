import paho.mqtt.client as paho
import random
import threading
import queue
import base64

from cryptography.fernet import Fernet
import sys

CLIENT_ID = f'movant-mqtt-{random.randint(0, 1000)}'
USERNAME = ''
PASSWORD = ''
BROKER = 'test.mosquitto.org'
PORT = 1883

CHAT_ROOMS = {
    'python': 'movantchat/python'
}

class Chat:
    def __init__(self, username, room, passphrase):
        self.username = username
        self.room = room
        self.topic = CHAT_ROOMS[room]
        self.client = None
        self.connect_mqtt()
        self.input_queue = queue.Queue()
        self.running = True
        self.fernet = self._init_encryption(passphrase)

    def _init_encryption(self, passphrase):
        try:
            if len(passphrase) != 32:
                raise ValueError("Passphrase must be 32 characters long")
            key = base64.urlsafe_b64encode(bytes(passphrase, 'utf-8'))
            return Fernet(key)
        except Exception as e:
            print(f"Error initializing encryption: {e}")
            sys.exit(1)

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe(userdata['topic'])
        else:
            print(f"Failed to connect, return code {rc}")
            sys.exit(1)

    def connect_mqtt(self):
        try:
            self.client = paho.Client(client_id=CLIENT_ID, userdata={'topic': self.topic})
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(BROKER, PORT)
        except Exception as e:
            print(f"Error connecting to MQTT broker: {e}")
            sys.exit(1)

    def on_message(self, client, userdata, msg):
        try:
            decrypted_message = self.fernet.decrypt(msg.payload).decode()
            print(f"{decrypted_message}")
        except Exception as e:
            print(f"Error decrypting message: {e}")

    def init_client(self):
        try:
            self.client.loop_start()
        except Exception as e:
            print(f"Error starting MQTT loop: {e}")
            sys.exit(1)

    def run(self):
        self.init_client()
        
        while self.running:
            try:
                msg_to_send = input()
                if msg_to_send.lower() == "quit":
                    self.client.publish(self.topic, self.fernet.encrypt(bytes(f"{self.username} has left the chat", 'utf-8')))
                    self.running = False
                    break
                else:
                    encrypted_message = self.fernet.encrypt(bytes(f"{self.username}: {msg_to_send}", 'utf-8'))
                    self.client.publish(self.topic, encrypted_message)
            except Exception as e:
                print(f"Error sending message: {e}")

def main():
    try:
        username = input("Enter your username: ")

        print("Pick a room:")
        for room in CHAT_ROOMS:
            print(f"\t{room}")
        room = input("> ")
        
        passphrase = input("Enter a 32-character passphrase for encryption: ")
        
        if len(passphrase) != 32:
            raise ValueError("Passphrase must be 32 characters long")
        
        chat = Chat(username, room, passphrase)
        chat.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
