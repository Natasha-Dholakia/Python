#program needs to take the bill amount as input and output the tip as a float


bill = int(input("What is the bill amount? "))
tip = float(input("What is the tip percentage? "))


def tip_calculator(bill, tip):
    tip_amount = bill / tip
    total_bill = bill + tip_amount
    return total_bill


print("The tip is $" + str(tip_calculator(bill, tip)))
print("The total is $" + str(tip_calculator(bill, tip)))
