import random
import string
import os

print("PASSWORD GENERATOR PRO")
print("Advanced, Secure, Customizable\n")

# Character sets
UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Remove ambiguous characters
UPPER = UPPER.replace('I', '').replace('O', '')
LOWER = LOWER.replace('1', '')
DIGITS = DIGITS.replace('0', '').replace('1', '')

def get_char_set():
	print("Include:")
	use_upper = input(" Uppercase letters? (y/n): ").strip().lower() == 'y'
	use_lower = input(" Lowercase letters? (y/n): ").strip().lower() == 'y'
	use_digits = input(" Digits? (y/n): ").strip().lower() == 'y'
	use_symbols = input(" Symbols? (y/n): ").strip().lower() == 'y'

	chars = ""
	if use_upper: chars += UPPER
	if use_lower: chars += LOWER
	if use_digits: chars += DIGITS
	if use_symbols: chars += SYMBOLS

	if not chars:
		print("Error: Must select at least one character type!")
		return get_char_set()
	return chars

def generate_passwords(length, count, chars):
	return [''.join(random.choice(chars) for _ in range(length)) for _ in range(count)]

# === INPUT ===
while True:
	try:
		length = int(input("Password length (8-50): "))
		if 8 <= length <= 50: break
		print("Enter 8-50!")
	except: print("Numbers only!")

while True:
	try:
		count = int(input("How many passwords? (1-20): "))
		if 1 <= count <= 20: break
		print("Enter 1-20!")
	except: print("Numbers only!")

chars = get_char_set()

# === GENERATE ===
passwords = generate_passwords(length, count, chars)

# === Display ===
print("\n" + "="*50)
print(f" YOUR {count} STRONG PASSWORDS: ")
print("="*50)
for i, pwd in enumerate(passwords, 1):
	print(f" {i}. {pwd}")
print("="*50)

# === SAVE TO FILE ===
save = input("\nSave to 'passwords.txt'? (y/n): ").strip().lower() == 'y'
if save:
	with open("passwords.txt", "w") as f:
		f.write(f"Generated {count} passwords (length {length})\n")
		f.write("="*50 + "\n")
		for i, pwd in enumerate(passwords, 1):
			f.write(f"{i}. {pwd}\n")
	print("Saved to passwords.txt on Desktop!")

# === COPY TO CLIPBOARD (BONUS) ===
copy_idx = input(f"\nCopy password # to clipboard? (1-{count}, or press Enter to skip): ").strip()
if copy_idx.isdigit() and 1 <= int(copy_idx) <= count:
	import pyperclip
	pwd = passwords[int(copy_idx)-1]
	pyperclip.copy(pwd)
	print(f"Password {copy_idx} copied to clipboard!")

input("\nPress Enter to exit...")