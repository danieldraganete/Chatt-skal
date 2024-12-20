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

1. **Requirements**:
   - Python 3.x
   - Required libraries: `cryptography` and `paho-mqtt`
   - Install dependencies using:
     ```bash
     pip install cryptography paho-mqtt
     ```

2. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>