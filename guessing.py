import random

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("You entered a string instead of an integer. Please try again.")

low = get_integer_input("What is the lowest number you want to guess from: ")
high = get_integer_input("What is the highest number you want to guess from: ")


while( high < low):
   print("invalid input")
   low=int(input("What is the lowest number you want"))
   high=int(input("what is the highests number you want to guess from"))

print(f"You have chosen a range from {low} to {high}.")

r=random.randrange(low,high + 1)
count=0
def guessing(r,count):
   while True:
        try:
            userguess=int(input("What is your guess"))

            if( userguess < r):
                print("Your number is lower than the target number")
                count+=1
                guessing(r,count)
    
            elif userguess > r:
                print("your number is greater than the target number")
                count+=1
                guessing(r,count)
            else:
                count+=1
                print("You got it right")
                print("It took you " + str(count) + " guess")
                quit()
        except ValueError:
                print("You entered a string instead of an integer. Please try again.")



guessing(r,count)