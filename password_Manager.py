from cgitb import text
from json import load
import re
from symbol import with_item
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)

# key + passw + text to encrpt =  random text
# randm text + key + passw =  text to encrpt


def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open("password.txt", 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("user:", user, "pass:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a password or view existing one ( add and view q to quit? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print(" Invalid mode.")
        continue
