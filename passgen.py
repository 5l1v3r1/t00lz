#!/usr/bin/python
from random import randint
lentgh = int(raw_input("Length You PassWord? = "))
string = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', "'", ';', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'm', ',', '/', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', ':', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X', 'C', 'B', 'N', 'M', '<', '>', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '|']
crypt = ""
while len(crypt) <= lentgh:
	crypt = crypt + string[randint(0,76)]
	if len(crypt)==lentgh:
		print crypt