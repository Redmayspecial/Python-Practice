"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Input:
"a"
""
Output:
-1
Expected:
0
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        needleLocation = -1
        haystackLength = len(haystack)
        needleLength = len(needle)

        if (haystack == needle) or (needle == ""):
            needleLocation = 0
            return needleLocation

        for x in range(haystackLength - needleLength + 1):
            sampleHaystack = ""
            print("x = ", x)
            for y in range(needleLength):
                sampleHaystack += haystack[x+y]
                print("y = ", y , "sampleHaystack =", sampleHaystack)
            if (sampleHaystack == needle) and (needleLength != 0):
                needleLocation = x
                return needleLocation
            if haystack == needle:
                needleLocation = x
        return needleLocation         

Answer = Solution()  

testHaystack = "hello"
testNeedle = "ll"
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))

testHaystack = "hello"
testNeedle = "el"
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))

testHaystack = "hello"
testNeedle = "he"
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))

testHaystack = "hello"
testNeedle = "lo"
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))

testHaystack = "hello"
testNeedle = "l7"
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))

testHaystack = "hello"
testNeedle = "l"
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))

testHaystack = ""
testNeedle = "l"
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))

testHaystack = "hello"
testNeedle = ""
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))

testHaystack = ""
testNeedle = ""
print("haystack =", testHaystack)
print("needle = ", testNeedle)
print("Solution = ", Answer.strStr(testHaystack,testNeedle))