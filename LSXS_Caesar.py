#!/usr/bin/python
#coding: UTF-8
__author__ = "TaQini"
__book__ = "LisanShuxue"

def createlist(char,length):
    list = []
    for i in range(length):
        list.append(chr(ord(char)+i))
    return list

def getoffset():
    offset = eval(raw_input("Please input the offset: "))
    return offset

def getmessage():
    msg = raw_input("Please input the message: ")
    return msg

def caesar(msg,offset,list):
    result = ""
    for char in msg:
        if char in list:
            tmp = list.index(char)
            tmp += offset
            tmp %= len(list)
            result += list[tmp]
        else:
            result += char
    return result

def main():
    lower = createlist('a',26)
    upper = createlist('A',26)
    #print list
    msg = getmessage()
    offset = getoffset()
    result = msg
    result = caesar(result, offset, lower)
    result = caesar(result, offset, upper)
    print "Output: " + result

main()
