"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    bracketDictionary = {"(":")", "[":"]", "{":"}"}
    stringLength = len(s)
    currentPosition = 0
    stringArray = []
    
    #check to see tha the first bracket is not a close bracket
    if s[currentPosition] not in bracketDictionary:
        return (False)

    while currentPosition <= stringLength-1:
        #while accumulating open brackets, store them in a list to compare later
        if s[currentPosition] in bracketDictionary:
            stringArray.append(s[currentPosition])
        else:
            #end bracket detected, now compare to see if it pairs with the last item in the list.
            if s[currentPosition] != bracketDictionary[stringArray.pop()]:
                #if it does not match, the sequence is invalid and the function can return false
                return (False)

        #move our current position down the string
        currentPosition += 1
       
    #if our list is empty, it means that all the pairs have correctly matched.
    if (stringArray == []):
        return (True)

"""
def isValid(s):


    bracketDictionary = {"(":")", "[":"]", "{":"}"}
    stringLength = len(s)
    currentPosition = 0
    stringArray = []
    
    print("stringLength: ", stringLength)
    print("currentPosition: ", currentPosition)

    #check to see tha the first bracket is not a close bracket
    if s[currentPosition] not in bracketDictionary:
        return (False)

    while currentPosition <= stringLength-1:
        if s[currentPosition] in bracketDictionary:
            stringArray.append(s[currentPosition])
            print("current position in the string", s[currentPosition])
        else:
            #print ("Popped item: ", bracketDictionary[stringArray.pop()])
            if s[currentPosition] != bracketDictionary[stringArray.pop()]:
                return (False)
        currentPosition += 1
        print(stringArray)

    if (stringArray == []):
        return (True)
"""

testString = "(((())))"
print("Checking the following brackets: ", testString)

if isValid(testString):
    print("Correct formation")
else:
    print("Incorrect formation")    


testString = "({[]})"
print("Checking the following brackets: ", testString)

if isValid(testString):
    print("Correct formation")
else:
    print("Incorrect formation")    

testString = "({[])}"
print("Checking the following brackets: ", testString)

if isValid(testString):
    print("Correct formation")
else:
    print("Incorrect formation") 

testString = "]"
print("Checking the following brackets: ", testString)

if isValid(testString):
    print("Correct formation")
if not isValid(testString):
    print("Incorrect formation")  

    testString = "["
print("Checking the following brackets: ", testString)

if isValid(testString):
    print("Correct formation")

if not isValid(testString):
    print("Incorrect formation") 