#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python3

def score_grade(score):

    string = "Average score %s's grade is %s"

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
    scores = [89, 60, 69, 91, 100]
    print('all score is: ', scores)
    avg_score = sum(scores) / len(scores)

    score_grade(avg_score)

if __name__ == '__main__':
    main()