#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // shuffle() function
#include <random> // random variables
#include <cstdlib> // rand() and srand()
#include <ctime> // time()

using namespace std;

int main()
{
	cout << "Password Generator" << endl;
	
	// vectors of available character types and their characters that can be used in the password
	vector<char> upper_letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
	vector<char> lower_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	vector<char> symbols = {'!', '#', '$', '%', '^', '&', '-', '(', ')', '*', '+'};
	vector<char> numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
	
	// used to hold the user's input
    string user_choice;
	cout << "Do you want to choose how many letters, symbols, and numbers are in your password? Type y for yes and n for no: ";
	cin >> user_choice;
	
	// correct input
	if (user_choice == "y" || user_choice == "yes" || user_choice == "n" || user_choice == "no")
	{
		// used to hold characters in password that will be shuffled
		vector<char> password_list;
		
		// random number generaor for index positions
		srand(time(0));
		
		// used to hold a random index position
		int ran_pos;
		
		// user wants to select the number of each character
		if (user_choice == "y" || user_choice == "yes")
		{
			// used to hold the amount of a certain character type the user wants
			int num_upper_letters;
			int num_lower_letters;
			int num_symbols;
			int num_numbers;
			
			// user inserts the amount of each character type for the password
			cout << "How many upper case letters would you like in your password: ";
			cin >> num_upper_letters;
			cout << "How many lower case letters would you like in your password: ";
			cin >> num_lower_letters;
			cout << "How many symbols would you like in your password: ";
			cin >> num_symbols;
			cout << "How many numbers would you like in your password: ";
			cin >> num_numbers;
			
			// generates a random index for the character type vector and pushes the element to password_list
			// this is done for every character type vector
			for (int i = 0; i < num_upper_letters; i++)
			{
				ran_pos = rand() % upper_letters.size();
				password_list.push_back(upper_letters[ran_pos]);
			}
			
			for (int i = 0; i < num_lower_letters; i++)
			{
				ran_pos = rand() % lower_letters.size();
				password_list.push_back(lower_letters[ran_pos]);
			}
			
			for (int i = 0; i < num_symbols; i++)
			{
				ran_pos = rand() % symbols.size();
				password_list.push_back(symbols[ran_pos]);
			}
			
			for (int i = 0; i < num_numbers; i++)
			{
				ran_pos = rand() % numbers.size();
				password_list.push_back(numbers[ran_pos]);
			}
		}
		
		// user doesn't want to select the number of each character
		else if (user_choice == "n" || user_choice == "no")
		{
			// used to hold all characters in each character type vector
			vector<char> char_list;
			
			// used to combine all character type vectors to one vector
			char_list.insert(char_list.end(), upper_letters.begin(), upper_letters.end());
			char_list.insert(char_list.end(), lower_letters.begin(), lower_letters.end());
			char_list.insert(char_list.end(), symbols.begin(), symbols.end());
			char_list.insert(char_list.end(), numbers.begin(), numbers.end());
			
			// used to hold the amount of characters for the password
			int num_characters;
			
			// user inserts the amount of characters for the password
			cout << "How many characters would you like in your password: ";
			cin >> num_characters;
			
			// generates a random index for the char_list vector and pushes the element to password_list
			for (int i = 0; i < num_characters; i++)
			{
				ran_pos = rand() % char_list.size();
				password_list.push_back(char_list[ran_pos]);
			}
		}
		
		// used to shuffle password_list vector randomly each time it is ran
		random_device rd;
		default_random_engine rng{rd()};
		shuffle(password_list.begin(), password_list.end(), rng);
		
		// used to hold generated password
		string password;
		
		// filling password with the elements of password_list
		for (int i = 0; i < password_list.size(); i++)
		{
			password += password_list[i];
		}
		
		cout << "Your password is: " << password;
	}
	
	// wrong input
	else
	{
		cout << "Invalid choice, try again";
	}
	
	return 0;
}