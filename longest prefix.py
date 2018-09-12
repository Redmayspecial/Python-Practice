"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # create a prefix variable
        prefix = ""
        continue2Seek = True
        
                         
        # figure out how many strs are in the array
        stringNumber = len(strs)

        if strs == []:
            return (prefix)
        else:
            indexPosition = 0
            firstWord = strs[indexPosition]
        

        # check for length of shortest word
        minWordLength = len(firstWord)

        for string in strs:
            if len(string) < minWordLength:
                minWordLength = len(string)

        # increment through each letter
        while continue2Seek & (indexPosition < minWordLength):
 
            comparisonLetter = firstWord[indexPosition]

            for string in strs :
                
                if string[indexPosition] != comparisonLetter:
                    continue2Seek = False

            indexPosition += 1

            if continue2Seek:
                prefix += comparisonLetter

        return (prefix)



print("Longest Prefix Problem")

answer = Solution()



Strings = ["cat", "catty", "catness"]

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))


Strings = ["cat", "ca", "catness"]

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))               
            
Strings = ["cat", "catty", "c"]

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))                

Strings = ["cat", "catty", ""]

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))

Strings = ["flower","flow","flight"]

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))

Strings = ["dog","racecar","car"]

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))

Strings = []

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))

"""

Strings = ["1234", "5678", "90"]

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))


Strings = []

print("longest common prefix in ",Strings, " is", answer.longestCommonPrefix(Strings))
        # store the common result in the prefix variable
        # return the variable

"""