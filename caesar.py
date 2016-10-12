#!/usr/bin/python 
#coding: utf-8
# Caesar cipher

import sys

try:
	if len(sys.argv[1:]) == 2:
		s = sys.argv[1]
		x = int(sys.argv[2])
	else:
		s = raw_input("String:\r\n")
		x = int(raw_input("offset:\r\n"))
except ValueError:
	print "[!]ValueErrorr\r\n"
	exit(0)

res = ""

for c in s:
	d = ord(c) + x
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
print res

# abcdefghijklmnopqrstuvwxyz