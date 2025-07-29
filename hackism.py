import bcrypt
from colorama import Fore, Style
from cryptography.fernet import Fernet
from datetime import datetime
import os
import platform
import random
import shutil
import subprocess
import sys
import time

system = platform.system()

if system == "Windows":
    passwordfilepath = "hackism_data/password.txt"
    logfilepath = "hackism_data/log.log"
    filesfilepath = "hackism_data/files.txt"
    data_path = os.path.join(os.path.dirname(__file__), "hackism_data")
    os.makedirs(data_path, exist_ok=True)
    subprocess.run(["attrib", "+h", data_path])
    if not os.path.exists(logfilepath):
        open(logfilepath, "w").close()
        os.system(f'attrib +h {logfilepath}')
    if not os.path.exists(filesfilepath):
        open(filesfilepath, "w").close()
elif system == "Linux" or system == "Darwin":
    passwordfilepath = ".hackism_data/password.txt"
    logfilepath = ".hackism_data/.log.log"
    filesfilepath = ".hackism_data/files.txt"
    data_path = os.path.join(os.path.dirname(__file__), ".hackism_data")
    os.makedirs(data_path, exist_ok=True)
    if not os.path.exists(logfilepath):
        open(logfilepath, "w").close
    if not os.path.exists(filesfilepath):
        open(filesfilepath, "w").close()

commands = "help, scan, access, ls, clear, crypter, setrngseed, clearlog, deletefiles, reset, shutdown"
commands2 = "help, ls, download, exit"

with open(filesfilepath, "r") as f:
    files = [line.strip() for line in f]

def log(message: str):
    time = datetime.now()
    time_f = time.strftime("%Y-%m-%d %H:%M:%S")
    logcontent = f"[{time_f}] {message}"
    with open(logfilepath, "a") as f:
        f.write(f"{logcontent}\n")

def reset():
    shutil.rmtree(data_path)

def pass_hash(password: str):
    password_bytes = password.encode()
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_bytes, salt)
    return password_hash

def random_letters(length: int):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(letters) for _ in range(length))

def progress(delay: float = random.uniform(0.01, 0.1), numbers: int = 20):
    for i in range(101):
        binary = ""
        for j in range(numbers):
            binary = str(binary) + str(random.randint(0, 1))
        print(f"\rProgress: {i}% {binary}", end="", flush=True)
        time.sleep(delay)
    print()

def typewriter(text: str, delay: float = 0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hackism():
    ips = []
    global files
    clear()
    print("Hackism | 'help' for command list.")
    while __name__ == '__main__':
        command = input("> ")
        if command == "help":
            print(commands)
        elif command == "scan":
            ips = []
            for ip in range(random.randint(1, 5)):
                ips.append(random.randint(1, 4096))
                ips = list(set(ips))
            print(ips)
        elif command == "access":
            accessip = int(input("IP: "))
            if accessip in ips:
                clear()
                log(f"Connecting {accessip}...")
                typewriter("Creating encrypted tunnel...")
                progress(delay=0.02)
                typewriter("Spoofing MAC adress...")
                progress(delay=0.005)
                typewriter(f"Connecting {accessip}")
                progress(delay=0.005)
                typewriter("Decrypting...")
                progress(numbers=35)
                time.sleep(0.5)
                clear()
                log(f"Connected {accessip}")
                print("Succesfully connected.")
                time.sleep(0.02)
                while True:
                    command2 = input(f"{accessip} > ")
                    if command2 == "help":
                        print(commands2)
                    elif command2 == "ls":
                        try:
                            downfiles
                        except NameError:
                            downfiles = []
                            for file in range(random.randint(1, 5)):
                                randomfilename = random.randint(1, 5)
                                if randomfilename == 1:
                                    filename = "secret.txt"
                                elif randomfilename == 2:
                                    filename = "topsecret.zip"
                                elif randomfilename == 3:
                                    filename = "passwords.zip"
                                elif randomfilename == 4:
                                    filename = "secret_recipe.txt"
                                else:
                                    filename = f"{random_letters(random.randint(5, 8))}.bin"
                                downfiles.append(filename)
                                downfiles = list(set(downfiles))
                        else:
                            pass
                        for file2 in downfiles:
                            print(file2)
                    elif command2 == "download":
                        downloadfilename = input("File: ")
                        if downloadfilename in downfiles:
                            log(f"Downloading {downloadfilename}...")
                            typewriter(f"Downloading {downloadfilename}")
                            progress(delay=random.uniform(0.02, 0.08))
                            log(f"Downloaded {downloadfilename}")
                            print("Download succesfull!")
                            downfiles.remove(downloadfilename)
                            files.append(f"[{accessip}] {downloadfilename} {random.randint(10000, 99999)}")
                            with open(filesfilepath, "w") as f:
                                for item in files:
                                    f.write(f"{item}\n")
                        else:
                            print(f"{Fore.RED}This file doesn't exist.{Style.RESET_ALL}")
                    elif command2 == "exit":
                        log("Launched exiting protocol...")
                        typewriter("Erasing traces...")
                        progress(0.005)
                        log(f"Exiting from {accessip}...")
                        typewriter("Exiting...")
                        progress(0.001)
                        log(f"Exited from {accessip}")
                        clear()
                        print("Hackism | 'help' for command list.")
                        hackism()
                    elif command2 == "":
                        pass
                    elif command2 not in commands2:
                        print(f"{Fore.RED}{command2} is not a valid command. Try 'help'.{Style.RESET_ALL}")
            else:
                print("Unavailable IP.")
        elif command == "ls":
            for lsfile in files:
                print(lsfile)
        elif command == "clear":
            hackism()
        elif command == "crypter":
            cmode = input("[E] - encrypt | [D] - decrypt: ").lower()
            if cmode == "e":
                key = Fernet.generate_key()
                f = Fernet(key)

                text = input("Text: ").encode()
                token = f.encrypt(text).decode()

                log(f"Encrypted text. Result = {token}")

                print(f"Encrypted: {token}")
                print(f"Key: {key.decode()}")
            elif cmode == "d":
                key = input("Key: ").encode()
                f = Fernet(key)

                text = input("Text: ").encode()
                token = f.decrypt(text).decode()

                log(f"Decrypted text. Result = {token}")

                print(f"Decrypted: {token}")
            else:
                print(f"{Fore.RED}Invalid mode {cmode}!{Style.RESET_ALL}")
        elif command == "setrngseed":
            seed = input("Seed: ")
            random.seed(seed)
            log(f"Changed RNG seed to {seed}")
        elif command == "clearlog":
            try:
                os.remove(logfilepath)
            except:
                pass
        elif command == "deletefiles":
            try:
                os.remove(filesfilepath)
            except:
                pass
        elif command == "shutdown":
            log("Shutting down...")
            typewriter("Shutting down...")
            progress(0.001)
            log("Shutted down\n")
            sys.exit()
        elif command == "reset":
            reset()
        elif command == "":
            pass
        else:
            print(f"{Fore.RED}{command} is not a valid command. Try 'help'.{Style.RESET_ALL}")

clear()
log("Booting Hackism...")
typewriter("Booting Hackism...")
progress(delay=0.001)
typewriter("Loading files...")
progress(delay=0.001)
typewriter("Encrypting...")
progress(delay=0.001, numbers=35)
log("Booted Hackism")
time.sleep(0.5)
clear()

if os.path.exists(passwordfilepath):
    with open(passwordfilepath, "rb") as f:
        correct_password = f.read()
else:
    correct_password = None

if correct_password == None:
    new_password = input("Set a password: ")
    with open(passwordfilepath, "wb") as f:
        f.write(pass_hash(new_password))
    log("Logging as admin...")
    typewriter("Wait...")
    progress(delay=0.005)
    log("Logged as admin")
    hackism()
elif correct_password != None:
    password = input("Admin password: ")
    clear()
    if bcrypt.checkpw(password.encode(), correct_password):
        log("Logging as admin...")
        typewriter("Wait...")
        progress(delay=0.005)
        log("Logged as admin")
        hackism()
    else:
        reset()
        typewriter("Access denied.")
        typewriter("Reseted your data.")
        new_password = input("Reset your password: ")
        os.makedirs(data_path, exist_ok=True)
        if not os.path.exists(filesfilepath):
            open(filesfilepath, "w").close()
        with open(passwordfilepath, "wb") as f:
            f.write(pass_hash(new_password))
        log("Logging as admin...")
        typewriter("Wait...")
        progress(delay=0.005)
        log("Logged as admin")
        hackism()
