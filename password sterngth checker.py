import re
import random
import string
def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_character(password):
    return bool(re.search(r'[@_!#$%^&*()<>?/\|}{~:]', password))

def check_repeated_patterns(password):
    return not any(password[i] == password[i+1] == password[i+2] or \
                   ord(password[i]) == ord(password[i+1])-1 == ord(password[i+2])-2 \
                   for i in range(len(password)-2))
def generate_password():
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
        if check_length(password) and check_digit(password) and check_special_character(password):
            return password
def check_common_password(password, common_passwords):
    return password not in common_passwords

def password_strength(password):
    common_passwords = {"password", "123456", "12345678", "1234", "qwerty", "12345", 
                        "dragon", "baseball", "football", "letmein", "monkey", 
                        "696969", "abc123", "mustang", "michael", "shadow", 
                        "master", "jennifer", "111111", "2000", "jordan", 
                        "superman", "harley", "1234567", "1234567890","asdfghjk"}
    
    criteria = {
        "Length": check_length(password),
        "Uppercase": check_uppercase(password),
        "Lowercase": check_lowercase(password),
        "Digit": check_digit(password),
        "Special Character": check_special_character(password),
        "No Repeated Patterns": check_repeated_patterns(password),
        "Not Common Password": check_common_password(password, common_passwords)
    }
    return criteria

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)

    print("\nPassword Strength Assessment:")
    for criterion, meets_requirement in strength.items():
        if criterion in a:
            print(f"{criterion}: {'SATISFIED' if meets_requirement else '❌'}")

    if all(strength.values()):
        print("\nCongratulations! Your password meets all criteria for strong security.")
        exit()
    else:
        print("\nYour password does not meet all criteria for strong security. Please consider strengthening it.")
        print("Suggested Password:",generate_password())

if __name__ == "__main__":
    while True:
        a=["Special Character","Digit","Lowercase","Uppercase"]
        main()
