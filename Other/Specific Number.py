# Write a program that continually asks the uses to enter a number until they enter the number 5, at which point the program should print how many numbers the user has entered 

number_of_entries = 0 # Initialize the number of entries to 0


while True :  
    number = int(input("Enter a number: ")) #`int` converts the input to an integer
    number_of_entries += 1 # Increment the number of entries by 1 each time the loop runs

    if number == 5:  # If the number is 5, break out of the loop
        break 

print(f"You entered {number_of_entries} numbers.") # Print the number of entries