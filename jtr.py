import hashlib
import itertools
import string

# Simulated stored password
password = "hey3" 
salt = "5T9v6qfp"  #salt

# Hash the password with SHA-256
target_hash = hashlib.sha256((salt + password).encode()).hexdigest()
print("Target Hash:", target_hash)

# Wordlist for dictionary attack
wordlist = ["password", "123456", "hey3", "qwerty", "letmein"]

def brute_force_attack():
    """Simulates a brute-force attack by generating all possible passwords."""
    charset = string.ascii_lowercase + string.digits  # Lowercase letters + numbers

    for length in range(1, 5):  # Try passwords of length 1 to 4
        for guess in itertools.product(charset, repeat=length):
            guess = "".join(guess)
            guess_hash = hashlib.sha256((salt + guess).encode()).hexdigest()
            if guess_hash == target_hash:
                print(f"🔓 Password Found: {guess}")
                return

    print("❌ Password Not Found")

def dictionary_attack():
    """Attempts to crack the hash using a predefined wordlist."""
    for word in wordlist:
        guess_hash = hashlib.sha256((salt + word).encode()).hexdigest()
        if guess_hash == target_hash:
            print(f"🔓 Password Found: {word}")
            return
    
    print("❌ Password Not in Wordlist")

def mask_attack():
    """Attempts to crack the password using a specific pattern (like John the Ripper's --mask)."""
    
    # Define the mask pattern (example: "???d" → 3 letters + 1 digit)
    mask = ["?l", "?l", "?l", "?d"] 

    # Define possible character sets
    charsets = {
        "?l": string.ascii_lowercase,  
        "?d": string.digits,          
    }

    # Generate all combinations following the mask
    for guess_tuple in itertools.product(*(charsets[m] for m in mask)):
        guess = "".join(guess_tuple)
        guess_hash = hashlib.sha256((salt + guess).encode()).hexdigest()
        if guess_hash == target_hash:
            print(f"🔓 Password Found: {guess}")
            return
    
    print("❌ Password Not Found with Mask Attack")

# User chooses the attack type
try:
    attack_type = int(input("\nWhich attack do you want to simulate?\n1. Dictionary Attack\n2. Brute-force Attack\n3. Mask Attack\n> "))

    match attack_type:
        case 1:
            print("📜 Dictionary attack selected.")
            dictionary_attack()
        case 2:
            print("💥 Brute-force attack selected.")
            brute_force_attack()
        case 3:
            print("🎭 Mask attack selected.")
            mask_attack()
        case _:
            print("❌ Invalid attack type.")
except ValueError:
    print("❌ Please enter a valid number.")
