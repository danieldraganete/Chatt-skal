# Encrypted Chat Application with MQTT and Symmetric Encryption

## Overview

This project implements a secure chat application using the MQTT protocol for real-time messaging and symmetric encryption to ensure confidentiality. The application allows users to join chat rooms, send encrypted messages, and receive decrypted messages via a simple command-line interface.


---


## Features

1. **Encryption**:
   - Symmetric encryption using a 32-character key derived from a user-defined passphrase.
   - Secure implementation using the `cryptography` library with Fernet encryption.

2. **MQTT Integration**:
   - Utilizes a public MQTT broker for efficient and scalable message distribution.

3. **Command-Line Interface**:
   - User-friendly interface for sending and receiving messages in real time.

4. **Robust Programming**:
   - Defensive programming practices to handle errors such as invalid passphrases, decryption failures, and network issues.


---


## Installation

### Requirements

- Python 3.x
- Required libraries: `cryptography` and `paho-mqtt`

Install the required libraries using the following command:

```bash
pip install cryptography paho-mqtt
```

Clone the Repository
```git
git clone <repository-url>
cd <repository-folder>
```
Run the Application
```bash
python chatt-skal-v2.py
```


---


## Usage

Start the Application
	•	Provide your username, chat room, and a passphrase when prompted.

Send Messages
	•	Type a message in the command line. The message is encrypted and sent via MQTT.

Receive Messages
	•	Incoming messages are decrypted and displayed in the command line.


---


## Security Considerations
   
   ### Key Management
   
   The encryption key is derived from the user-defined passphrase, which should be managed securely.
   
   ### Error Handling
   
   Robust error handling ensures the application remains stable and secure in the face of decryption or network failures.


---


## Future Improvements
1.	Implement a secure key management system.
2.	Add a graphical user interface for better user experience.
3.	Expand to support multiple encryption methods.


---

## Authors

- Daniel Draganete - Student, Movant Yh
- Patryk Robakowski - Student, Movant Yh
 
 
 ---
 

## License

This project is licensed under the MIT License. See the LICENSE file for details.

This version uses Markdown formatting for headings, lists, code blocks, and structure, making it suitable for a `README.md` file. Let me know if you need additional adjustments!
