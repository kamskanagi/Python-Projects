import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    """
    Check for winning combinations in the slot machine columns.

    Args:
        columns (list): The 2D list representing the slot machine columns.
        lines (int): The number of lines to bet on.
        bet (int): The bet amount per line.
        values (dict): A dictionary mapping symbols to their corresponding values.

    Returns:
        tuple: A tuple containing the total winnings and a list of winning lines.
    """
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random spin of the slot machine columns.

    Args:
        rows (int): The number of rows in the slot machine.
        cols (int): The number of columns in the slot machine.
        symbols (dict): A dictionary mapping symbols to their corresponding counts.

    Returns:
        list: A 2D list representing the slot machine columns.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    """
    Print the current state of the slot machine.

    Args:
        columns (list): The 2D list representing the slot machine columns.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row])
            else:
                print(column[row])
        print()

def deposit():
    """
    Prompt the user to enter the deposit amount.

    Returns:
        int: The amount deposited.
    """
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    """
    Prompt the user to enter the number of lines to bet on.

    Returns:
        int: The number of lines to bet on.
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    """
    Prompt the user to enter the bet amount per line.

    Returns:
        int: The bet amount per line.
    """
    while True:
        amount_bet = input("What would you like to bet on each line? ")
        if amount_bet.isdigit():
            amount_bet = int(amount_bet)
            if MIN_BET <= amount_bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount_bet

def main():
    """
    Main game logic and flow.
    """
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winnings_lines)

main()
