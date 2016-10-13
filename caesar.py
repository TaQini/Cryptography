#!/usr/bin/python 
#coding: utf-8
# Caesar cipher
# more: https://www.nayuki.io/page/automatic-caesar-cipher-breaker-javascript

import sys

s = ""
x = 13

def usage():
    print "Usage: " + str(sys.argv[0]) + "string offset/list"
    
def get():
    global s
    global x
    if len(sys.argv[1:]) != 0:
        s = sys.argv[1]
        x = sys.argv[2]		
    else :
        s = raw_input("String:\r\n")
        x = raw_input("offset:\r\n")    
def caesar(s,x):
    res = ""		
    for c in s:
        d = ord(c) + int(x)
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            if d > ord('z'):
                d -= 26
            elif d < ord('a'):
                d += 26
            res += chr(d)
        elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
            if d > ord('Z'):
                d -= 26
            elif d < ord('a'):
                d += 26
            res += chr(d)
        else:
            res += c
    return res

def ls(s):
    for i in range(0,26):
        print "rot" + str(i) + ": " + caesar(s,str(i))

def main():
    get()    
    try:
        if x == "l":
            ls(s)
        else:
            print caesar(s,x)		
    except ValueError:
        print "[!]ValueErrorr\r\n"
        exit(0)    
        
main()
# abcdefghijklmnopqrstuvwxyz
