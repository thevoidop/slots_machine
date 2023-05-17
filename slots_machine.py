import random

MIN_BET = 5
MAX_BET = 100

def gameMoney():
    while True:
        balance = input("Enter the amount you want to deposit: $")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("\n[Amount must be greater than $0.]\n")
        else:
            print("\n[Please enter a valid number.]\n")
    return balance
            
def gameBet():
    while True:
        bet = input("Enter your bet amount: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"\n[Amount must be between ${MIN_BET} and ${MAX_BET}]\n")
        else:
            print("\n[Please enter a valid number.]\n")
    return bet          

def gameMechanism():
    matrixChar = "ABC"
    matrixLine1 = []
    matrixLine2 = []
    matrixLine3 = []
    for i in range (0,3):
        matrixLine1.append(random.choice(matrixChar))
        matrixLine2.append(random.choice(matrixChar))
        matrixLine3.append(random.choice(matrixChar))
        
    print("==============================")
    print("|   ", end="")
    for char in matrixLine1:
        print(char+"    |", end="    ")
    print("\n==============================")
    print("|   ", end="")
    for char in matrixLine2:
        print(char+"    |", end="    ")
    print("\n==============================")
    print("|   ", end="")
    for char in matrixLine3:
        print(char+"    |", end="    ")
    print("\n==============================")

    
    outcome = 0
    if (matrixLine1[0] == matrixLine2[0] == matrixLine3[0]):
        outcome = 1
    elif (matrixLine1[1] == matrixLine2[1] == matrixLine3[1]):
        outcome = 1
    elif (matrixLine1[2] == matrixLine2[2] == matrixLine3[2]):
        outcome = 1
    elif (matrixLine1[0] == matrixLine1[1] == matrixLine1[2]): 
        outcome = 1
    elif (matrixLine2[0] == matrixLine2[1] == matrixLine2[2]):
        outcome = 1
    elif (matrixLine3[0] == matrixLine3[1] == matrixLine3[2]):
        outcome = 1
    else:
        outcome = 0
    return outcome

def gameWinning(balance, bet, outcome):
    if outcome == 1:
        balance += bet * 2
        print("\nCongratulations! You have won")
    else:
        balance -= bet
        print("\nYou have lost.")
    print(f"\n[Your balance now is ${balance}]")
    return balance
 
balance = gameMoney() 

while balance > 0:
    bet = gameBet() 
    if bet > balance:
        print(f"\nYou do not have enough money. Your current balance is ${balance}\n")
    elif balance == 0:
        print("You do not have sufficient balance. Thank you for playing.")
        exit()
    else:
        print("\n\t\t\tRunning the Slot Machine...\n")
        outcome = gameMechanism()
        balance = gameWinning(balance, bet, outcome)