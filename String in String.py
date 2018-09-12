"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        haystackPointer = 0
        needlePointer = 0
        success = -1

        print('Looking for "', needle, '" in the phrase "', haystack,'"')

        while haystackPointer <= (len(haystack)-1):
            print("hay = ", haystackPointer, haystack[haystackPointer])
            print("needle = " , needlePointer, needle[needlePointer])
            if needle[needlePointer] == haystack[haystackPointer]:
                while (haystackPointer < (len(haystack))) and (needlePointer < (len(needle))):
                    if (needle[needlePointer] == haystack[haystackPointer]):
                        print("haymatch = ", haystackPointer, haystack[haystackPointer])
                        print("needlematch = ", needlePointer, needle[needlePointer])
                        needlePointer += 1
                        haystackPointer += 1

                if needlePointer == len(needle):
                    success = haystackPointer - len(needle)
                    return (success)
            else:
                needlePointer = 0
                haystackPointer += 1

        return (success) 


comparison = Solution()

haystack = "helpmefindtheneedleintthehaystack"
needle = "the"


answer = comparison.strStr(haystack,needle)

if answer == -1:
    print('Sorry, "', needle, '" not found')
else:
    print("'", needle, '" found at position ', answer, ' in \n"', haystack, '"')         

haystack = "theeeeee"
needle = "the"

answer = comparison.strStr(haystack,needle)

if answer == -1:
    print('Sorry, "',needle,'" not found')
else:
    print("'", needle,'" found at position ', answer, ' in \n"', haystack,'"') 

haystack = "ttttttthe"
needle = "the"

answer = comparison.strStr(haystack,needle)

if answer == -1:
    print('Sorry, "', needle, '" not found')
else:
    print("'", needle, '" found at position ', answer, ' in \n"', haystack,'"') 
    
haystack = "mypantsareonbackwards"
needle = "the"

answer = comparison.strStr(haystack,needle)

if answer == -1:
    print('Sorry, "',needle,'" not found')
else:
    print("'",needle,'" found at position ',answer, ' in \n"',haystack,'"') 






