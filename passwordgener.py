import string
import secrets

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    try:
        n = int(input("Enter password length (e.g. 8): "))
        if n <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    pwd = generate_password(n)
    print("Generated password:", pwd)

if __name__ == "__main__":
    main()