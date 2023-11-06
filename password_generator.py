import string
import random


def generate_password(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(len))
    return password

if __name__ == "__main__":
    password_len = int(input("Enter password length: "))
    if password_len < 1:
        print("Password length must be at least 1 character.")
    else:
        password = generate_password(password_len)
        print("Generated password:", password)
