
MAX_LINES = 4

def deposit():

    while True:
        amount = input("How much would you like to deposit? ")

        if amount.isdigit():
            if int(amount) > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount


def numberOfLines():

    while True:
        
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES} )")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines < MAX_LINES:
                break
            else:
                print("Enter valid lines")
        else:
            print("enter a number")
    
    return lines
        


def main():

    balance = deposit()

main()