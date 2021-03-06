#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python2

from time import *

db = {}
last_time = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    db[name] = pwd
    
def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    lt = last_time.get(name)
    if passwd == pwd:
        if lt != None and mktime(localtime()) - mktime(lt) <= 14400:
            print 'You already logged in at:', asctime(lt)
        print 'welcome back', name
        last_time[name] = localtime()
    else:
        print 'login incorrect'
        
def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()
    
if __name__ == '__main__':
    showmenu()