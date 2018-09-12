"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    xString = str(x)
    print(xString)
    xReverse = ""
    stringLength = len(xString)-1
    pointer = stringLength

    

    while pointer >= 0:
        if xString[pointer] == "-":
            xReverse = "-" + xReverse
        else:
            xReverse += xString[pointer]
        pointer -= 1
    
    if (int(xReverse) > 2147483647) or (int(xReverse) < -2147483647):
        xReverse = 0
    
    return(int(xReverse))

#Set test variable
testNumber = 321

print(reverse(testNumber))

testNumber = -411

print(reverse(testNumber))

testNumber = 2147483647

print(reverse(testNumber))

testNumber = 2147483648

print(reverse(testNumber))

testNumber = -2147483648

print(reverse(testNumber))