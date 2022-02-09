# write a program that asks the user to enter a word "q" or "quit" and then prints the average length of the words entered before the user enters "q" or "quit"


word_count = 0 # Initialize the word count to 0
word_list = [] # Initialize the word list to an empty list
while True:  
    word = input("Enter a word: ") # Get the user input
    if word == "q" or word == "quit": # If the user enters "q" or "quit", break out of the loop
        break # Break out of the loop
    word_list.append(word) # Add the word to the word list
print(f"You entered {len(word_list)} words.") # Print the number of words entered
print(f"The average length of the words is {sum(len(word) for word in word_list) / len(word_list)}") # Print the average length of the words
