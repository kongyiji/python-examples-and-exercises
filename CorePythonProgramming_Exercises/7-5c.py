#!/usr/bin/env python
# -*- coding: utf-8 -*-
# platform: python2

from time import *
from hashlib import md5

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
    # pwd = raw_input('passwd: ')
    pwd = encrpytpwd(raw_input('passwd: '))
    db[name] = pwd
    
def olduser():
    name = raw_input('login: ')
    # pwd = raw_input('passwd: ')
    pwd = encrpytpwd(raw_input('passwd: '))
    passwd = db.get(name)
    lt = last_time.get(name)
    if passwd == pwd:
        if lt != None and mktime(localtime()) - mktime(lt) <= 14400:
            print 'You already logged in at:', asctime(lt)
        print 'welcome back', name
        last_time[name] = localtime()
    else:
        print 'login incorrect'

def deluser():
    name = raw_input('user name: ')
    if name not in db.keys():
        print 'not exist'
    else:
        del db[name]
        print 'user', name, 'deleted'

def showuser():
    for name in db.keys():
        print name, ':', db[name]

def encrpytpwd(password):
    return md5(password).hexdigest()

def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(M)anager
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
            if choice not in 'mneq':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()
        if choice == 'm':
            managemenu()

def managemenu():
    prompt = """
(1) Delete User
(2) Show all user's name and password
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
            if choice not in '12q':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'q':
            done = True
        if choice == '1':
            deluser()
        if choice == '2':
            showuser()
    
if __name__ == '__main__':
    showmenu()