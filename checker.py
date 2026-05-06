import re

password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if re.search(r"[A-Z]", password):
    strength += 1

if re.search(r"[a-z]", password):
    strength += 1

if re.search(r"[0-9]", password):
    strength += 1

if re.search(r"[!@#$%^&*]", password):
    strength += 1

if strength == 5:
    print("Strong Password")
elif strength >= 3:
    print("Moderate Password")
else:
    print("Weak Password")
