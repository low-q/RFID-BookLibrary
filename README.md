# **RFID Book Management System Description**

The RFID Book Management System is a Python-based project designed for efficiently managing a library's book inventory using RFID (Radio-Frequency Identification) technology. This system leverages the Mifare RC522 RF IC RFID kit along with a Raspberry Pi 4 to enable users to easily scan RFID stickers or cards attached to books, thereby retrieving or inputting book information.

## **System Components:**

**RFID Kit - Mifare RC522 RF IC**: This RFID kit serves as the primary means of identifying books within the library inventory. It consists of RFID tags (stickers or cards) attached to each book and an RFID reader module (Mifare RC522) connected to the Raspberry Pi.

**Raspberry Pi 4**: The Raspberry Pi 4 serves as the central processing unit of the system. It runs the Python script responsible for reading RFID tags, interacting with users, and managing book information.

**Dupont Wire**: Dupont wires are used for connecting the RFID reader module to the GPIO (General Purpose Input Output) pins of the Raspberry Pi, facilitating communication between the RFID reader and the Pi.

## Connection Diagram
![RC522-RFID-Raspberry-Pi-Pico-Connection](https://github.com/low-q/RFID-BookLibrary/assets/124109826/79124ee5-f776-4d4b-8acf-719960580096)

## Operation
1. The system waits for a RFID tag to be scanned.
2. Upon scanning, the system reads the tag's unique ID.
3. The system checks if a text file corresponding to the ID exists.
  a. If the file exists, it reads the book information and offers to search for the book online.
  b. If the file doesn't exist, it prompts the user to input the book information.
4.The user provides the book information (name, author, genre).
5.The system saves the information to a new text file named after the RFID tag's ID.
6.Steps 1-5 repeat until terminated by the user (KeyboardInterrupt).
## Conclusion
The RFID Book Management System provides a user-friendly and efficient solution for managing library book inventories using RFID technology. By leveraging the Raspberry Pi and RFID reader module, it streamlines the process of accessing and updating book information, enhancing the overall library management experience.
