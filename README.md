Password Cracking with John the Ripper and Custom Python Implementation

Overview

This project demonstrates three password-cracking techniques using John the Ripper (JtR) and a custom Python script:

Dictionary Attack

Brute-Force Attack

Mask Attack

Both JtR and a Python-based approach were used to hash and crack passwords efficiently.

Steps Performed

1️⃣ Hashing Passwords

A Python script (generator.py) was created to hash passwords using SHA-512.
a smaller version of rockyou.txt was used as wordlist.

Example usage:

python hash_generator.py <password> > hash.txt

The hash.txt file stores the hashed password.

2️⃣ Dictionary Attack

Used a precompiled wordlist (rockyousmall.txt) to attempt cracking.

Commands executed:

john --format=Raw-SHA512 --wordlist=rockyousmall.txt hash.txt
john --format=Raw-SHA512 --show hash.txt

Implemented a custom dictionary attack in Python using a predefined wordlist.

3️⃣ Brute-Force Attack

JtR brute-force mode used to test all possible character combinations:

john --format=Raw-SHA512 --incremental=Lower hash.txt
john --format=Raw-SHA512 --show hash.txt

Custom Python brute-force attack implemented using itertools.product() to generate password candidates.

4️⃣ Mask Attack

Targeted attack with a known pattern (e.g., 5 lowercase letters):

john --format=Raw-SHA512 --mask=?l?l?l?l?l hash.txt
john --format=Raw-SHA512 --show hash.txt

Custom Python version was added to attempt cracking passwords following a specific pattern.
