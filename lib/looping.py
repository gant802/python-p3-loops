#!/usr/bin/env python3
import ipdb

def happy_new_year():
    i = 10
    while i != 0:
        print(i)
        i -= 1
    print("Happy New Year!") 


def square_integers(int_list):
    doubled = [number ** 2 for number in int_list]
    return doubled

def fizzbuzz():
    
    for q in range(1, 101):
        if q % 3 == 0 and q % 5 == 0: 
            print("FizzBuzz")
        elif q % 3 == 0:
            print("Fizz")
        elif q % 5 == 0:
            print("Buzz")
        else : 
            print(q)
            
   


fizzbuzz()