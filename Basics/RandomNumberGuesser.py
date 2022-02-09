# Write a program that asks the user to  enter two integers representing the start and end of a range.
# Then ask the user to enter an integer value.
# The program should tell the user if the value is in the range or not.  
# Your program should handle any other errors that may occur, like the user entering non-numeric values.
# You can assume the start will not be negative 
# and the end will not be less than the start.


# Smaple Output:
# Enter the start of the range: 1
# Enter the end of the range: 10
# Guess a number: 5
# Guess a number: 6
# You guessed the number in 2 attempts!

import random # inputting this module because we have to a genetrate a random number 

start = input("Enter the start of the range: ") # Asking the  user to input a valid range 

# This loop will repeat unitl the user inputs a valid integer
while not start.isdigit(): # Check if the user input a valid integer 
    print("Enter a valid number.")  # If the user failed to input a valid number, ask again for a valid integer. 
    start = input("Enter the start of the range: ") 
    
end = input("Enter the end of the range: ")
while not end.isdigit() or int(end) < int(start): # Placing a condition where end number has to be smaller than the start number 
    #If the user fails to input a digit or an end number smaller than start number, the system will ask to print a valid number 
    print("Enter a valid number.")
    end = input("Enter the end of the range: ")

# Generating a random number 

random_number = random.randint(int(start),int(end)) # Generating a random number between the start and end number

guess = None # Initializing the guess variable
attempts = 0 # How many attempts the user has 

while guess != random_number:  # This loop will repeat until the user guesses the random number
    guessed_number =input("Guess a number: ") # Asking the user to input a number
    if not guessed_number.isdigit(): # Checking if the user input a valid number
        print("Please enter a valid number.") # If the user fails to input a valid number, the system will ask to print a valid number
        continue # This will continue the loop and ask the user to input a valid number

    attempts += 1 # This will add 1 to the attempts variable
    guess = int(guessed_number) # This will convert the user input to an integer

suffix = "" # Initializing the suffix variable
if attempts > 1: # This will check if the user has made more than one attempt
    suffix = "5" # If the user has made more than one attempt, the suffix will be "5"

print(f"you guessed the number in {attempts} attempt {suffix}") # This will print the number of attempts the user has made