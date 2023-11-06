import string, getpass

name = input("Enter username: ")

while True:
    password = getpass.getpass("Enter password: ")
    x = password.strip()
    if not all(char in string.printable for char in x):
        print(f"{name} use printable characters as your password!!!")
        exit(-1)
    elif len(x) < 8:
        print(f"{name} your password is too short")
        continue
    elif any(char in (string.ascii_lowercase and string.ascii_uppercase and string.digits and string.punctuation) for char in x):
        print(f"{name} your password is strong")
        break
    else:
        print(f"{name} something is wrong")
        continue
