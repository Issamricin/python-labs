
"""
This is a small game where you have to avoid making the bomb explode

The user is given questions to answer. But since we like to detonate the bomb, 
We can also detonate it when the answer is correct. Therefore, the user must read the source code to 
avoid detonating the bomb."""

import bomb
import random

def welcome():
    """Print a welcome screen for the game"""
    print("""
            Hello and welcome to the game Bomben!

You will be asked questions. If you answer "wrong" the bomb will explode. "Wrong" is not always the same as wrong. You have to read the source code to see what the correct answer is, for example you may be asked "what is 1+1?" and you may have to answer 3 to avoid detonating the bomb.


           Have so much fun!
        """)

def complicated_if():
    """Some questions with nested if statements"""
    float_number = float(input("Say a number between 0 and 1:"))
    if not(0 < float_number and float_number < 1):
        bomb.detonate()

    float_number = float(input("Say a number between 1 and 2:"))
    if 1 > float_number or float_number > 2:
        bomb.detonate()

    print("1 < 2 and 2 < 1 or 9 < 10, true or false?", end=" ")
    true_or_false = input()
    if true_or_false == "false":
        bomb.detonate()

    age = int(input("Name a good age? [Enter a number]"))
    if age < 30:
        bomb.detonate()
    elif age > 20 and age < 40:
        bomb.detonate()
    elif not(age < 65):
        bomb.detonate()

def recursion(n):
    """Some questions that use recursion"""
    if n < 0:
        bomb.detonate()
    elif n == 0:
        return

    random_number = random.randint(-5, 5)
    number = int(input(f"I say {random_number}, which number do you say? "))

    recursion(n-1 + random_number - number)

def main():
    """Start the bomb game"""

    welcome()

    if 2 == int(input("How much is 1+1? ")):
        bomb.detonate()

    complicated_if()

    print("""
Congratulations, you made it through the complicated if statements! Now I'm going to trick you 
with a little recursion!
        """)

    recursion(5)

    print("""

    
Congratulations, you made it through without detonating the bomb.!

Your price is that you get to choose whether you want to detonate the bomb safely.
""")
    detonate = input("Detonate, yes or no? ")
    if detonate == "yes":
        bomb.detonate()
    else:
        print("So boring ...")

main()
