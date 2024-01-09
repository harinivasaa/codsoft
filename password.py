import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_punctuation):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    
    if not any([use_lowercase, use_uppercase, use_digits, use_punctuation]):
        return "Please select at least one character type for the password."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input for password criteria
length = int(input("Enter the length of the password: "))
lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
digits = input("Include digits? (yes/no): ").lower() == 'yes'
punctuation = input("Include punctuation? (yes/no): ").lower() == 'yes'

generated_password = generate_password(length, lowercase, uppercase, digits, punctuation)
print("Generated password:", generated_password)
