import random
roll_again = "yes"
min = 1
max = 6
while roll_again == "yes" or roll_again == "y" :
    print ("rolling dices...")
    print ("the values are...")
    print (random.randint(min,max))
    print (random.randint (min,max))
    if min == max :
        print ("you got a double ,you won!")
    else :
        print ("try again")
    roll_again = input("do you want to roll again ?")

#they should all start from the same space ot itll creat a loop ;[
# this didnt work because min = 1 and max =6 so they would never be the saeme

import random
import time 
roll_again = "yes"
while roll_again == "yes" or roll_again == "y" :
    print ("rolling dices...")
    time.sleep(1)
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print ("the values are...")
    print ("dice 1 = ", dice1,"\ndice 2 =",dice2)
    
    if dice1 == dice2 :
        print ("you got a double,you won!")
    else :
        print ("try again")
    roll_again = input("do you want to roll again ?")

#import time just gives a gap