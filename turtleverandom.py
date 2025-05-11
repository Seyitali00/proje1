from turtle import *
import random as r

renkler = ["red","blue","purple"]
print(r.random())
print(r.randint(50,100))
print(r.choice(renkler))

speed(10)
for ddd in range (10):
    kenaruz = r.randint(50,200)
    color(r.choice(renkler))
    aa=(r.randint(-200,300))
    bb=(r.randint(-200,300))
    penup()
    goto(aa,bb)
    pendown()
    for a in range(6):
        forward(kenaruz); right(60)
      
    

input()
