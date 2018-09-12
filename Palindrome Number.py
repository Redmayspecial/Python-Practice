"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    #convert integer to string
    xString = str(x)

    #create a reverse duplicate of the new string
    xReverse = xString[::-1]

    """
    Discovered this capability of slices when looking to see if python had a reverse string function
    This is extended slice syntax. It works by doing [begin:end:step] 
    - by leaving begin and end off and specifying a step of -1, it reverses a string.
    """

    if xString == xReverse:
        return(True)
    else:
        return(False)


testInteger = 123456
print("Checking for Palindrome numbers: ", testInteger," : ", isPalindrome(testInteger))

testInteger = 12345654321
print("Checking for Palindrome numbers: ", testInteger," : ", isPalindrome(testInteger))

testInteger = 78900987
print("Checking for Palindrome numbers: ", testInteger," : ", isPalindrome(testInteger))