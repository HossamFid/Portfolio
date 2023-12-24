""" 
Code Wars 

https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python

Problem: Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

Examples:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
""" 

import math

def litres(time):
    time = math.floor(time)
    init = 0
    #print(f" initalization: {init} ")
    for i in range(1,time+1):
        print(f" time: {i}")
        init+=0.5
        print(f"loop initalization: {init} ")
        
    return math.floor(init)


litres(3)



#return time // 2 

#int(time /2)

