import random
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()"
b = capital + lowercase + symbols
length = int(input("enter your password length: "))
a = "".join (random.sample(b,length))
print (f"your password is {a}")