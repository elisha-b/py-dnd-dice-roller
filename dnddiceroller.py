# Owner: elisha-b
# Date: 17-02-2025
# Project: D&D Dice Roller

import random
import math

def main():
    
    try:
        numSides = float(input("\nHello! How many sides does your dice have?\nYour answer: "))
    except ValueError:
        numSides = float(input("\nOops! Please use numbers. Try again!\nYour answer: "))
    except:
        print("Uh, something went wrong.")

    # Invalid number of sided dice
    while (numSides != 4 and numSides != 6 and numSides != 8 and numSides != 10 and numSides != 12 and numSides != 20):
        numSides = float(input("\nPlease enter a valid number of sides.\nYour answer: "))
    
    # Number of X-sided dice
    print(f"\nYou have selected a d{math.trunc(numSides)}!")
    try:
        numDice = float(input("\nHow many are you rolling?\nYour answer: "))
    except ValueError:
        print("\nOops! Please type a valid number!")
        numDice = float(input("\nHow many are you rolling?\nYour answer: "))
    except:
        print("Uh, something went wrong.")

    # Confirmation of dice
    print(f"\nYou are rolling {math.trunc(numDice)}d{math.trunc(numSides)}!")
    confirm = input("\nConfirm? (Y/N)\nYour answer: ")

    while ((confirm != "Y" and confirm  != "y") and (confirm != "N" and confirm !="n")):
        print("\nUh oh! Please choose between Y for YES or N for NO.")
        print(f"\nYou are rolling {math.trunc(numDice)}d{math.trunc(numSides)}!")
        confirm = input("\nConfirm? (Y/N)\nYour answer: ")
    
    if confirm == "Y" or confirm == "y":
        results = int(numDice) * int(random.randint(1, int(numSides)))
        print(f"\nYou have rolled a: {results}!")
    elif  confirm == "N" or confirm == "n":
        print("\nThank you for using D&D Dice Roller!")
    else:
        print("Uh, something went wrong.")

main()
