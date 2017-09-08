#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def score_grade(score):

    string = "Score %s's grade is %s"

    if 90 <= score <= 100:
        print(string % (score, 'A'))

    elif 80 <= score <= 89:
        print(string % (score, 'B'))

    elif 70 <= score <= 79:
        print(string % (score, 'C'))

    elif 60 <= score <= 69:
        print(string % (score, 'D'))

    elif 0 <= score < 60:
        print(string % (score, 'F'))

    else:
        print('invalid score!')

def main():
    score = input('Please input your score: ')
    score_grade(int(score))

if __name__ == '__main__':
    main()