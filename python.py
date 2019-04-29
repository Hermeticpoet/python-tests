def print_message(message):
    print(message)
    
print_message("Hello World!")


my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# import os

from flask import Flask

# Lottery Number Generator: 1-50 with 6 numbers
"""
def lotto_num_gen():
    numbers = []
    for number in range (1, 7):
       numbers.append(randint(1, 50))
    return numbers
"""

"""
import turtle

turtle.shape("turtle")
turtle.forward(25)
turtle.exitonclick()
"""

from random import randint

lotto_nums = ([randint(1, 50) for x in range(0,6)])
print("Numbers for the week are {}".format(lotto_nums))

    
