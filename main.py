import random , time

print()
print("Welcome to the Number Guessing Game.")
print("I am thinking of the number between 1 to 100.")
print("You have 3 types of difficulties to guess the number.","\n")

print("Please select the difficulty level 1 , 2 or 3")
print("1 . Easy (7 chances)")
print("2 . Medium (5 chances)")
print("3 . Hard (3 chances)" ,  "\n")

User_Difficulty_choose = int(input("Select Your Difficulty : "))

Computer_Guess = random.randint(1 , 100)

if User_Difficulty_choose==1:
    n = 7
elif User_Difficulty_choose==2:
    n = 5
else :
    n = 3

for turn in range(1 , n+1):
    chance = int(input("Guess your number: "))
    
    if chance == Computer_Guess:
        print("Congratulations! You guess the correct Number in attempt:",turn,"\n")
    elif chance > Computer_Guess:
        print("Your guessing number is greater than computer guessing number.", "\n")
    elif chance < Computer_Guess:
        print("Your guessing number is smaller than computer guessing number.", "\n")

    if turn == n:
        if chance != Computer_Guess:
            print("Better luck next time...." , "\n")