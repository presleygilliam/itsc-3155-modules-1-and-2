# Module 1 - Exercise 2
# Presley Gilliam - pgillia3@uncc.edu


# declare vars
resultLst = []
lowercase = []
uppercase = []
resultStr = ''

# prompts user to input string
inputStr = input('Enter a string: ')

# loop through string and add to list
for eachChar in inputStr:
    if eachChar != ' ':
        if eachChar.isupper() == True:
            uppercase.append(eachChar)
        elif eachChar.islower() == True:
            lowercase.append(eachChar)

# put lists together to create result list
for eachLower in lowercase:
    resultLst.append(eachLower)
for eachUpper in uppercase:
    resultLst.append(eachUpper)

# loop through each char in result list to create result string
for each in resultLst:
    resultStr = resultStr + each

# print results to user
print(resultStr)
