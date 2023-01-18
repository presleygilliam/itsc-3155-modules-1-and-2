# Module 1 - Exercise 1
# Presley Gilliam - pgillia3@uncc.edu


# declare vars
backwardsStr = ''
backwardsLst = []

# prompts user to input string
strInput = input('Enter a string: ')

# add each character in string to list
for eachChar in strInput:
    backwardsLst.append(eachChar)

# reverse list
backwardsLst.reverse()

# loop through reverse list and add to result string
for each in backwardsLst:
    backwardsStr = backwardsStr + each

# prints result to user
print(backwardsStr)
