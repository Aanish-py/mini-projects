import random
import json

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 100

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
FILE = 'user_balance.json'


def read_balance():

    try:
     
        with open(FILE, 'r') as f:
            data = json.load(f)
            return data.get('balance', 0.0) 
    except FileNotFoundError:
        print(f"Creating a new balance file: {FILE}")
        return 0.0
    except json.JSONDecodeError:
        print(f"Warning: Could not read balance file. Resetting to 0.")
        return 0.0
    except Exception as e:
        print(f"An unexpected error occurred while reading: {e}")
        return 0.0

def write_balance(balance):

    try:
       
        with open(FILE, 'w') as f:
            data_to_store = {'balance': balance}
            json.dump(data_to_store, f, indent=4)

        print(f"Successfully saved new balance: {balance:.2f}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")





def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
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
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def get_number_of_lines():
    while True:
        lines = 0;
        lines= input("Select the number of lines: ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                break
            else:
                print("Lines must be greater than 0")
        else:
            print("Please Enter a number")

    return lines

def get_the_bet():
    while True:
        bet = input("How much would you like to bet for each line: ")
        if bet.isdigit():
            bet=int(bet)
            if bet>0:
                break
            else:
                 print("please input bet above 0")
        else:
            print("Please enter a number")

    return bet

#Play option code is here
def main(balance):
    
    user_lines = get_number_of_lines()
    while True:
        user_bet = get_the_bet()
        total_bet = user_bet * user_lines
        if total_bet <= balance:
            break

    print(f"Spinning {user_lines} lines with a ${user_bet} bet each. Total bet: ${total_bet}")
    balance -= total_bet

    #To print The Slot 
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, user_lines, user_bet, symbol_value)#using function to identify winning lines
    balance += winnings
    print(f"You won ${winnings:.2f}.")
    if winning_lines:
        print(f"You won on lines:", *winning_lines)
    print(f"Your new balance is: ${balance:.2f}")
    print("\n------------------------------------------")

    write_balance(balance) 

    return balance
                

#Code runs From here
def main_menu():

    balance = read_balance()#To create json file
    while True:
        print("\n--- Slot Machine Main Menu ---")
        print(f"Current Balance: ${balance:.2f}")
        user_input = input("Press 1 to Play\nPress 2 to Add balance\nPress 3 to Quit\nEnter choice: ")
        #To check user input
        if user_input == '1':
            if balance <= 0:#To check if user is broke
                print("\nYou have no balance. Please deposit first.")
                continue
            main(balance)
                
        elif user_input == '2':
            try:
                amount_str = input("Enter Deposit amount: ")
                amount = float(amount_str)
                
                if amount <= 0:
                    print("Deposit must be a positive number.")
                else:
                    balance += amount
                    write_balance(balance)
                    print(f"Amount Added Successfully!\nCurrent Balance: ${balance:.2f}\n")
            except ValueError:
                print("Invalid amount. Please enter a number.\n")
            
        elif user_input == '3':
            print(f"Goodbye! You are leaving with ${balance:.2f}.")
            break 
        
        else:
            print("Invalid choice. Please press 1, 2, or 3.")

#Activating The Game
main_menu()
