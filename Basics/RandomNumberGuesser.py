import random # inputting this module because we have to a genetrate a random number 

start = input("Enter the start of the range: ") # Asking the  user to input a valid range 
while not start.isdigit():
    print("Enter a valid number.")
    start = input("Enter the start of the range: ") 
    
end = input("Enter the end of the range: ")
while not end.isdigit() or int(end) < int(start):
    print("Enter the end of the range: ")

random_number = random.randint(int(start),int(end))

guess = None 
attempts = 0

while guess != random_number:
    guessed_number =input("Guess a number: ")
    if not guessed_number.isdigit():
        print("Please enter a valid number.")
        continue 

    attempts += 1 
    guess = int(guessed_number)

suffix = ""
if attempts > 1:
    suffis = "5"

print(f"you guessed the number in {attempts} attempt {suffix}")