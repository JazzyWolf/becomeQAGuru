import random


MAX_LINES = 3 ##global variableS, CONSTANTS
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

def deposit():
    while True:
        amount = input("What would you like to deposit? $:")
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
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line ? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between " + str(MIN_BET) + " and " + str(MAX_BET))
        else:
            print("Please enter a number.")

    return amount
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("Your balance is not equal to your deposit. Your deposit is: " + str(balance))
        else:
            break



    print("You are betting " + str(bet) + " on " + str(lines) + " lines. Total bet is equivalent to: " + str(total_bet))


main()
