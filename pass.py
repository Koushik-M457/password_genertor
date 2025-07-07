import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    pwd = generate_password(16)
    print("Generated Password:", pwd)

