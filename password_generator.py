# Password Generator
import random

print("Password Generator")

upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '^', '&', '-', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

user_choice = input("Do you want to choose how many letters, symbols, and numbers are in your password? Type y for yes and n for no: ")
user_choice = user_choice.lower()

password = ""
password_list = []

# valid choices
if user_choice == "y" or user_choice == "yes" or user_choice == "n" or user_choice == "no":
    # if user selects yes then the program will ask for the quantatities for each different character type
    if user_choice == "y" or user_choice == "yes":
        num_upper_letters = int(input("How many upper case letters would you like in your password: "))
        num_lower_letters = int(input("How many lower case letters would you like in your password: "))
        num_symbols = int(input("How many symbols would you like in your password: "))
        num_numbers = int(input("How many numbers would you like in your password: "))
        
        # adding all the characters in a list
        for letter in range(num_upper_letters):
            # random.choice() gets a random item from a list, not its index
            password_list.append(random.choice(upper_letters))
        
        for letter in range(num_lower_letters):
            password_list.append(random.choice(lower_letters))

        for symbol in range(num_symbols):
            password_list.append(random.choice(symbols))

        for number in range(num_numbers):
            password_list.append(random.choice(numbers))
    
    # if user selects no then the program will only ask for how long the password should be
    elif user_choice == "n" or user_choice == "no":
        # add all the lists into one list
        char_list = lower_letters + upper_letters + symbols + numbers
        
        num_characters = int(input("How many characters would you like in your password: "))
        
        for char in range(num_characters):
            password_list.append(random.choice(char_list))
    
    # random.shuffle() randomly shuffles the elements in a list
    random.shuffle(password_list)
    
    # add elements in the list to a string
    for char in password_list:
        password += char
    
    print(f"Your password is: {password}")

else:
    print("Invalid choice, try again")
