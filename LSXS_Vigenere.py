#!/usr/bin/python
#coding: UTF-8
__author__ = "TaQini"
__book__ = "LisanShuxue"

def createlist(char,length):
    list = []
    for i in range(length):
        list.append(chr(ord(char)+i))
    return list

def getmessage():
    msg = raw_input("Please input the message: ")
    return msg

def getkey():
    key = raw_input("Please input the key: ")
    return key

def vigenere(msg, key, list):
    result = ""
    count = 0
    for char in msg:
        if char in list:
            tmp = list.index(char)
            tmp += list.index(key[count % len(key)])
            tmp %= 26
            count += 1
            result += list[tmp]
        else:
            result += char
    return result

def main():
    lower = createlist('a',26)
    upper = createlist('A',26)
    #print list
    msg = getmessage()
    key = getkey()
    result = msg
    result = vigenere(result, key, lower)
    result = vigenere(result, key, upper)
    print "Output: " + result

main()