import random

print("Welcome to the coin flipping game!")

choice=input ("Enter ur side (heads or tails): ")

num=random.randint(1,2)

if num==1:
    result="heads"
elif num==2:
    result="tails"

if choice==result:
    print("You Won it was", result)
else:
    print("You Lost it was", result)
