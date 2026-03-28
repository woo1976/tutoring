from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

# t.screen.mainloop()

# Practice
# from random import random

# for i in range(2):
#     steps = int(random() * 100)
#     print(steps)

# print(random())
# print("hello")