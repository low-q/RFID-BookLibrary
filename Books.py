#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import urllib.parse
import webbrowser
import os.path

reader = SimpleMFRC522()

def get_book_info():
    print("Please enter the following information:")
    book_name = input("Book name: ")
    author = input("Author: ")
    genre = input("Genre: ")
    return book_name, author, genre

def save_book_info(filename, book_name, author, genre):
    with open(filename, 'w') as f:
        f.write(book_name + '\n')
        f.write(author + '\n')
        f.write(genre + '\n')

def read_book_info(filename):
    with open(filename, 'r') as f:
        book_name = f.readline().strip()
        author = f.readline().strip()
        genre = f.readline().strip()
        return book_name, author, genre

def search_book_on_google(book_name, author):
    query = book_name + " " + author
    query = urllib.parse.quote_plus(query)
    webbrowser.open("https://www.google.com/search?q=" + query)

try:
    while True:
        print("Waiting for you to scan an RFID sticker/card")
        id = reader.read()[0]
        print("The ID for this card is:", id)

        filename = str(id) + ".txt"
        if os.path.isfile(filename):
            # The book info is already saved, so read it from the file
            book_name, author, genre = read_book_info(filename)
            print("The book is already registered.")
            search_book_on_google(book_name, author)
        else:
            # The book is new, so prompt the user to enter the info
            book_name, author, genre = get_book_info()
            save_book_info(filename, book_name, author, genre)
            print("The book info has been saved.")
except KeyboardInterrupt:
    GPIO.cleanup()