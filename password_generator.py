import random

print("Password Generator")

# lists of available character types and their characters that can be used in the password
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '^', '&', '-', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# used to hold the user's input
user_choice = input("Do you want to choose how many letters, symbols, and numbers are in your password? Type y for yes and n for no: ")
user_choice = user_choice.lower()

# correct input
if user_choice == "y" or user_choice == "yes" or user_choice == "n" or user_choice == "no":
    # used to hold characters in password that will be shuffled
    password_list = []
    
    # user wants to select the number of each character
    if user_choice == "y" or user_choice == "yes":
        # used to hold the amount of a certain character type the user wants
        num_upper_letters = int(input("How many upper case letters would you like in your password: "))
        num_lower_letters = int(input("How many lower case letters would you like in your password: "))
        num_symbols = int(input("How many symbols would you like in your password: "))
        num_numbers = int(input("How many numbers would you like in your password: "))
        
        # gets a random element from the character type list and pushes the element to password_list
        # this is done for every character type list
        for letter in range(num_upper_letters):
            password_list.append(random.choice(upper_letters))
        
        for letter in range(num_lower_letters):
            password_list.append(random.choice(lower_letters))

        for symbol in range(num_symbols):
            password_list.append(random.choice(symbols))

        for number in range(num_numbers):
            password_list.append(random.choice(numbers))
    
    # user doesn't want to select the number of each character
    elif user_choice == "n" or user_choice == "no":
        # used to hold all characters in each character type list
        char_list = lower_letters + upper_letters + symbols + numbers
        
        # user inserts the amount of characters for the password
        num_characters = int(input("How many characters would you like in your password: "))
        
        for char in range(num_characters):
            password_list.append(random.choice(char_list))
    
    # used to shuffle password_list list randomly each time it is ran
    random.shuffle(password_list)
    
    # used to hold generated password
    password = ""
    
    # filling password with the elements of password_list
    for char in password_list:
        password += char
    
    print(f"Your password is: {password}")

# wrong input
else:
    print("Invalid choice, try again")
