"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    def isValid(self, s):
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





answer = Solution()

testString = "(((())))"
print("Checking the following brackets: ", testString)


if answer.isValid(testString):
    print("Correct formation")
else:
    print("Incorrect formation")    


testString = "({[]})"
print("Checking the following brackets: ", testString)

if answer.isValid(testString):
    print("Correct formation")
else:
    print("Incorrect formation")    

testString = "({[])}"
print("Checking the following brackets: ", testString)

if answer.isValid(testString):
    print("Correct formation")
else:
    print("Incorrect formation") 

testString = "]"
print("Checking the following brackets: ", testString)

if answer.isValid(testString):
    print("Correct formation")

if not answer.isValid(testString):
    print("Incorrect formation")  

testString = "["
print("Checking the following brackets: ", testString)

if answer.isValid(testString):
    print("Correct formation")

if not answer.isValid(testString):
    print("Incorrect formation") 