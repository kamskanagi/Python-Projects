MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def  deposit():
    while True:
        amount= input("what will you like to deposit? $ ")
        if amount.isdigit(): # check if its a digit
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines= input("Enter the number of lines to bet on (1- " + str(MAX_LINES) + ")?" )
        if lines.isdigit(): # check if its a digit
            lines = int(lines)
            if 1 <= lines <=  MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("please enter a number.")

    return lines



def get_bet():
    while True:
        amount_bet= input("what would you like to bet on each line? ")
        if amount_bet.isdigit(): # check if its a digit
            amount_bet= int(amount_bet)
            if MIN_BET <= amount_bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number.")

    return amount_bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet =  lines * bet

    print(f" you are betting ${bet} on ${lines} lines.  Total bet is equal to ${total_bet}")


    print(balance, lines)

main()