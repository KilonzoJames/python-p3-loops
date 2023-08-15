#!/usr/bin/env python3
'''This is a sample docstring'''
def happy_new_year():
    '''Returns'''
    i=10
    while i > 0:
        print(i)
        i-=1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    '''Returns'''
    squared_list = [int**2 for int in int_list]
    return squared_list
input_list = [2, 3, 5, 7, 10]
print(square_integers(input_list))

def fizzbuzz():
    '''Returns'''
    for num in range(1,101):
        if num % 3==0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 ==0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print (num)
fizzbuzz()

def reverse_string(string):
    '''Returns'''
    reversed_string = ""
    for char in string:
        reversed_string=char + reversed_string
    return reversed_string

print(reverse_string('uppercase'))
