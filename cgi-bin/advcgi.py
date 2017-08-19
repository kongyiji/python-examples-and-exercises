#!/usr/bin/env python

from cgi import FieldStorage
from os import environ
from cStringIO import StringIO
from urllib import quote, unquote
from string import capwords, strip, split, join

class AdvCGI(object):

    header = 'Content-Type: SystemExitl\n\n'
    url = '/py/advcgi.py'

    formhtml = '''<HTML><HEAD><TITLE>
    Advanced CGI Demo</TITLE></HEAD>
    <BODY><H2>Advanced CGI Demo Form</H2>
    <FORM METHOD=post ACTION="%s" ENCTYPE="multipart/form-data">
    <H3>My Cookie Setting</H3>
    <LI><CODE><B>CPPuser = %s</B></CODE>
    <H3>Enter cookie value<BR>
    <INPUT NAME=cookie value="%s"> (<I>optional</I>)</H3>
    <H3>Enter your name<BR>
    <INPUT NAME=person VALUE="%s"> (<I>optional</I>)</H3>
    <H3>What languages can you program in?
    (<I>at least one required</I>)</H3>
    %s
    <H3>Enter file to upload</H3>
    <INPUT TYPE=file NAME=upfile VALUE="%s" SIZE=45>
    <P><INPUT TYPE=submit>
    </FORM></BODY></HTML>'''

    langSet = ('Python', 'PERL', 'Java', 'C++', 'PHP', 
            'C', 'JavaScript')
    langItem = \
            '<INPUT TYPE=checkbox NAME=lang VALUE="%s"%s> %s\n'

    def getCPPCookies(self): # read cookies from client
        if environ.has_key('HTTP_COOKIE'):
            for eachCookie in map(strip, \
                    split(environ['HTTP_COOKIE'], ';')):
                if len(eachCookie) > 6 and \
                        eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                    try:
                        self.cookies[tag] = \
                                eval(unquote(eachCookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = \
                                unquote(eachCookie[8:])
        else:
            self.cookies['info'] = self.cookies['user'] = ''

        if self.cookies['info'] != '':
            self.who, langStr, self.fn = \
                    split(self.cookies['info'], ':')
            self.langs = split(langStr, ',')
        else:
            self.who = self.fn = ''
            self.langs = ['Python']

    def showForm(self): # show fill-out form
        self.getCPPCookies()
        langStr = ''
        for eachLang in AdvCGI.langSet:
            if eachLang in self.langs:
                langStr += AdvCGI.langItem % \
                        (eachLang, 'CHECKED', eachLang)
            else:
                langStr += AdvCGI.langItem % \
                        (eachLang, '', eachLang)

            if not self.cookies.has_key('user') or \
                    self.cookies['user'] == '':
                cookStatus = '<I>(cookie has not been set yet)</I>'
                userCook = ''
            else:
                userCook = cookStatus = self.cookies['user']

            print AdvCGI.header + AdvCGI.formhtml % (AdvCGI.url,
                    cookStatus, userCook, self.who, langStr, self.fn)

        error
