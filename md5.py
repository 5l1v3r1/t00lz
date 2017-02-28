#!/usr/bin/python
try:
	import hashlib
except:
	print "you not have hashlib"
	print "Pleas install with pip install hashlib"

inp0t = str(raw_input("Enter Text = "))
value = hashlib.md5()
value.update(inp0t)
print value.hexdigest()
