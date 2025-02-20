import hashlib
import sys

def generate_hash(password):
    hashed_password = hashlib.sha512(password.encode()).hexdigest()  # No salt
    return hashed_password

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hash_generator.py <password>")
        sys.exit(1)
    
    password = sys.argv[1]
    print(generate_hash(password))
