import random
import string

letters = {}
replacement_set = set()

for _ in range(5):
    while True:
        char = input("enter a lowercase character: ")
        if char in letters:
            print(f"'{char}' is already in the dictionary, write a different.")
        elif len(char) != 1 or not char.islower():
            print("invalid input, enter a single lowercase character.")
        else:
            break

    replacements = set()
    for _ in range(3):
        while True:
            replacement = input(f"enter a replacement for '{char}': ")
            if (
                len(replacement) == 1
                and replacement.isprintable()
                and replacement not in replacements
                and replacement not in replacement_set
            ):
                replacements.add(replacement)
                replacement_set.add(replacement)
                break
            else:
                print(
                    f"invalid input '{replacement}' is either already used or is not a valid single character."
                )

    letters[char] = replacements

passwords = []
for _ in range(3):
    password = "".join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

categorized_passwords = {"strong": [], "weak": []}

for password in passwords:
    replaced_password = ""
    special_count = 0
    replaced_count = 0  

    for char in password:
        if char in letters:
            replaced_char = random.choice(list(letters[char]))
            replaced_password += replaced_char
            replaced_count += 1  
            if not replaced_char.isalnum(): 
                special_count += 1
        else:
            replaced_password += char

    
    if special_count >= 4:
        categorized_passwords["strong"].append(replaced_password)
    else:
        categorized_passwords["weak"].append(replaced_password)


if not categorized_passwords["weak"] and categorized_passwords["strong"]:
    categorized_passwords["weak"].append(categorized_passwords["strong"].pop())

print("\nGenerated Passwords:")

print("\nSTRONG PASSWORDS:")
if categorized_passwords["strong"]:
    for password in categorized_passwords["strong"]:
        print(password)
else:
    print("No strong passwords generated!")

print("\nWEAK PASSWORDS:")
if categorized_passwords["weak"]:
    for password in categorized_passwords["weak"]:
        print(password)
else:
    print("No weak passwords generated!")
