# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 18:39:08 2023

@author: mohammad
"""

import random
rand_num=random.randint(0, 10)
guess_left=3
name=None

def check_answer(answer):
    if answer>rand_num:
        return(False,"Choose higher number")
    elif answer<rand_num:
        return(False,"Choose lower number")
    elif answer==rand_num:
        return (True,"Bingo")

name = input('Enter your name:')

while True:
    if guess_left==0:
        print(f"you ran out of guesses \nanswer was {rand_num}")
        break
    answer_input=int(input(f"{name},please enteryour guess number"))
    answer_result = check_answer(answer_input)
    if answer_result[0] == False:
        print(answer_result[1])
    else:
        print(answer_result[1])
        break
    guess_left -=1

print("end of game")