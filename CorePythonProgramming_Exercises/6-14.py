#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

from random import choice

def compete(uc, cc):

    print('Your choice:', uc)
    print("Computer's choice", cc)
    compete_result = {
        'Rock-Paper': 'Lose...',
        'Rock-Scissors': 'Win!!!',
        'Paper-Scissors': 'Lose...',
        'Paper-Rock': 'Win!!!',
        'Scissors-Paper': 'Win!!!',
        'Scissors-Rock': 'Lose...'
    }

    if uc == cc:
        return 'Draw.'
    else:
        str = uc + '-' + cc
        return compete_result[str]

def rock_paper_scissors_game():

    menu = '''
**********************************
**** Rock-Paper-Scissors Game ****
**********************************
           (R)ock
           (P)aper
           (S)cissors
**********************************
           (Q)uit Game
**********************************
Your choice:
'''

    com_tuple = ('Rock', 'Paper', 'Scissors')

    while True:
        user_choice = in_choice = input(menu)
        com_choice = choice(com_tuple)
        if in_choice.lower() == 'r':
            user_choice = 'Rock'
            print(compete(user_choice, com_choice))
        elif in_choice.lower() == 'p':
            user_choice = 'Paper'
            print(compete(user_choice, com_choice))
        elif in_choice.lower() == 's':
            user_choice = 'Scissors'
            print(compete(user_choice, com_choice))
        elif in_choice.lower() == 'q':
            print('Quit Game...')
            break
        else:
            print('Invalid choice, please choose again!')

if __name__ == '__main__':
    rock_paper_scissors_game()