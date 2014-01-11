import itertools
import string
import re
import json, os
import time

str = 'Hello there.'
str2 = 'Hello there .'
str3 = 'Hello there:)'
str4 = 'Hello there :)'

#print str.split(), str2.split(), str3.split(), str4.split()

#print re.split('(\W+)', str), re.split('(\W+)', str2), re.split('(\W+)', str3), re.split('(\W+)', str4)


print re.split('(\W+)', str4)
#removes empty string
result = filter(None, re.split('(\W+)', str4)) #use None or bool? they gave me the same thing..
print result
result2 = [s.strip() for s in result]
print result2

#need to figure out a way to keep removing empty strings 
#is whitespace counted as its own punctuation?

'''
list = re.split('(\W+)', str4)
print list
#removes empty string
result =[s.strip() for s in list]
print result
result2 = filter(bool, re.split('(\W+)', str4))
print result2
'''
