import random

MAX_LINES = 4
MAX_BET = 100
MIN_BET = 1


def deposit():

    while True:
        amount = input("How much would you like to deposit? ")

        if amount.isdigit():
            amount = int(amount)
            if (amount) > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount


def numberOfLines():

    while True:
        
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES-1} )")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines < MAX_LINES:
                break
            else:
                print("Enter valid lines")
        else:
            print("enter a number")
    
    return lines

def getBet():

    while True:

        amount = input("How much would you like to bet: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount and MAX_BET >= amount:
                break
            else:
                print(f"bet is Not Between {MIN_BET} and {MAX_BET} ")
        else:
            print("Please Enter a Number")

    return amount

        
def main():

    balance = deposit()
    lines = numberOfLines()
    while True:
        bet = getBet()
        total = bet*lines

        if total > (balance):
            print("You do not have enough money")
        else:
            break
       
    print(f"You are betting {bet} on {lines} lines. Total bet = {total}")
    

main()