#! python3
# StrongCommondDetection.py Judge the commmond whether or not a strong commond

# 分别对应书中《Python编程快速上手：让繁琐工作自动化》中项目7.15

# the commond length greater than 8
# the commond include upper and lower alphabet meantime
# the commond include decimal less than one

import re,pyperclip

##text = str(pyperclip.paste())
##def detection(text):
##    print(1)
##    if len(text) <= 8:
##        return False
##    print(2)
##    upperAlphabetRegex = re.compile(r'[A-Z]+')
##    if upperAlphabetRegex.search(text) == None:
##        return False
##    print(3)
##    lowerAlphabetRegex = re.compile(r'[a-z]+')
##    if lowerAlphabetRegex.search(text) == None:
##        return False
##    print(4)
##    decimalRegex = re.compile(r'\d+')
##    if decimalRegex.search(text) == None:
##        return False
##    return True
##
##print(detection(text))

##text = str(pyperclip.paste())
##def detection(text):
##    print(1)
##    if len(text) <= 8:
##        return False
##    print(2)
##    upperAlphabetRegex = re.compile(r'[A-Z]+')
##    if len(upperAlphabetRegex.findall(text)) > 0:
##        return False
##    print(3)
##    lowerAlphabetRegex = re.compile(r'[a-z]+')
##    if lowerAlphabetRegex.search(text) == '':
##        return False
##    print(4)
##    decimalRegex = re.compile(r'\d+')
##    if len(decimalRegex.search(text)) > 0:
##        return False
##    return True
##
##print(detection(text))

##import re, pyperclip
##
##text = str(pyperclip.paste())
##def detection(text):
##    print(1)
##    if len(text) <= 8:
##        return False
##
##
##    number = re.compile(r'\d+')
##    print(2)
##    if number.search(text) == None:
##        return False
##
##    upletter = re.compile(r'[A-Z]+')
##    print(3)
##    if upletter.search(text) == None:
##        return False
##
##    lowletter = re.compile(r'[a-z]+')
##    print(4)
##    if lowletter.search(text) == None:
##        return False
##    
##    return True
##
##print(detection(text))

text = str(pyperclip.paste())
print(text)
def stripFunction(text):
    Regex = re.compile(r'\s*')
    if Regex.search(text) == None:
        return True
    return Regex.sub('',text)

print(stripFunction(text))
