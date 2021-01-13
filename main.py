import random
import string

while True:
    password = ''
    lower_upper_alphabet = string.ascii_letters
    numbers = "0123456789"
    symbols = string.punctuation
    choices = lower_upper_alphabet+symbols+numbers
    length = input("Type the length of your password or 0 to exit the program: ")

    if(length == '0'):
        print("Exiting...")
        exit(0)

    for _ in range(int(length)):
        password += str(random.choice(choices))
    
    print("Your Password is: " + password)

