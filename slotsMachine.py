# Project A: A Gambling Machine asking how much to bet and how many lines. Displays what the results are and
# whether the player wins or not

import random  # Imports random module

MAX_LINES = 3  # CONSTANT VALUE FOR LINES
MAX_BET = 100  # CONSTANT VALUE FOR MAXIMUM BETTING
MIN_BET = 1  # CONSTANT VALUE FOR MINIMUM BETTING
ROWS = 3  # CONSTANT VALUE FOR ROWS
COLS = 3  # CONSTANT VALUE FOR COLUMNS

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {  # Multiplier for bets
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):   # CHECKS VALUES TO SEE IF PLAYER WINS
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  # Looks at first value within column
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):  # _ is used to go through loop
            all_symbols.append(symbol)
    columns = []  # Define column list
    for col in range(cols):  # creates columns for each column
        column = []
        current_symbols = all_symbols[:]  # Makes current symbols store the same stuff as all_symbols has
        for _ in range(rows):  # Loop
            value = random.choice(current_symbols)  # Selects random value from current_symbols
            current_symbols.remove(value)  # Removes from current_symbols list
            column.append(value)  # Adds to column list

        columns.append(column)

    return columns


def print_slot_machine(columns):  # Prints out our slot machine in a 3x3 format
    for row in range(len(columns[0])):  # This creates a row per column
        for i, column in enumerate(columns):  # Loop for each column
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Creates a divider for the length
            else:
                print(column[row], end="")  # Pipe symbol creates section for it

        print()  # Outputs the value and the lines until it caps the length for columns


def deposit():  # Function to see deposit value
    while True:  # While loop based on situation being valid
        amount = input("What would you like to deposit? $")  # Question
        if amount.isdigit():  # If response is a numerical value
            amount = int(amount)  # This creates the new amount variable into an integer dataType
            if amount > 0:  # If amount is higher than 0, breaks out of loop
                break
            else:  # If not, repeats until condition is satisfied
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number: $")
    return amount  # Returns "amount" variable to shell to be seen


def get_num_of_lines():  # Function asking how many lines the user wants to bet on
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():  # Checking to see if response is a numerical value
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # If it is within 1 and 3, breaks out of loop
                break
            else:  # If not, repeats loop
                print("Enter a valid number of lines: ")
        else:  # Repeats loops if the response was NOT a numerical value
            print("Please enter a number: ")
    return lines


def get_bet():  # Function to see bet value
    while True:
        amount = input("What would you like to bet on each line? $")  # Question
        if amount.isdigit():  # If response is a numerical value
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:  # If amount is higher than 0, breaks out of loop
                break
            else:  # If not, repeats until condition is satisfied
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number: $")
    return amount  # Returns "amount" variable to shell to be seen


def spin(balance):
    lines = get_num_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Sorry, you do not have enough to make that bet. Your current balance is: ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet:}. Good luck!")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():  # Main function; will call functions!
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to spin! (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Current balance is ${balance}.")


main()
