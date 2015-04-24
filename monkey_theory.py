#!/usr/bin/env python
import string
import random

answer = 'methinks it is like a weasel'
master_score = 0
best_try = ''
amiright= False




mylist = []
[mylist.append(x) for x in string.ascii_lowercase]
mylist.append(' ')

def generate():
    attemptit = ''
    for k in answer:
        attemptit += mylist[random.randint(0,len(mylist)-1)]
    return attemptit

def scoreit(poop):
    score = 0
    for x in range(len(poop)-1):
        if poop[x] == answer[x]:
            """
            print(poop[x])
            print(answer[x])
            """
            score += 1
    return (score, poop)


def runit():
    global master_score
    global best_try
    i=0
    while i <=1000000000:
        my_score, my_poop = scoreit(generate())

        if my_score > master_score:
            master_score = my_score
            best_try = my_poop
            mytry = i
        i += 1
    print('Score of:',master_score,'out of',len(answer),'correct characters')
    print('Your best try:',best_try)
    print('Try number',mytry, 'out of', i-1)



runit()