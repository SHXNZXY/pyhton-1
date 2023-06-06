import random 
#need to insert module for random generating numbers
highrange = input("type in a number : ")
if highrange.isdigit():
    highrange=int(highrange)
    if highrange <=0:
        print('print a number higher then 0 next time')
        quit()
else: 
    print('please type in a number')
    quit()
#converting high range into a str-->num, is digit will check if its number ,then return true/false
r = random.randrange(1,highrange)
guesses = 0
#doesnt include 10 , one way to generate numbers ^^
# r = random.randint(1,9)
#this time it will print 9 using this method^^
print(r)

while True:
    guesses += 1
    #this says okay youve made one guess then goes through the bottom bit and f wrong then adds 1 = so output is okay youve made 2 guesses except it carries on
    #make sure you include a guesses = 0 varaible or there will be an error
    user_input= input("make a guess: ")
    if user_input.isdigit():
        user_input=int(user_input)
    else: 
        print('please type in a number')
        continue
    if user_input == r:
        print('you got it right')
        break
    else:
        print("you got it wroong!")

print("youve got it in", "guesses")
#links to the first code right after while true