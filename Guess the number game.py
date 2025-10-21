import random
number=random.randint(1,100)
while True:
    userNum=input("Enter choice or Ouit(Q): ")
    if(userNum=="Q"):
        break
    userNum=int(userNum)
    if(userNum==number):
        print("Congratulations! You have guessed the correct number.")
        break
    elif(userNum>number):
        print("Your number is greater. Guess again!")
    else:
        print("Your number is smaller. Guess again!")
print("------GAME OVER------")