"""
Discuss 
Pick One 


Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1: 
Input: [1,3,5,6], 5
Output: 2

Example 2: 
Input: [1,3,5,6], 2
Output: 1

Example 3: 
Input: [1,3,5,6], 7
Output: 4

Example 1: 
Input: [1,3,5,6], 0
Output: 0


Input:
[1] 0
Output:
1
Expected:
0

Input:
[1] 1
Output:
1
Expected:
0

"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        x = 0

        while x < (len(nums)-1):
            if nums[x] == target:
                # we've located the existing number in the list
                return (x)
            elif nums[x] < target and nums[x+1] > target:
                # we've found the spot where the target should be insertd between a smaller and bigger number
                return (x+1)
            elif nums[x] > target:
                # we've found the spot where the target should be inserted before the next big number
                return (x)
            else:
                # the target is assumed to be larger than x and x+1 so increment our pointer
                x += 1
        # we've exhausted our number list so we need to return the last position in the list.
        if (nums[x] > target) or (nums[x] == target):
            # if the number in the array is less than target, put target before the number
            # if the number in the array equals the target report it's current position
            return(x)
        else:
            # if the number in the array is more than target, put target after the number
            return(x+1)

        

Answer = Solution()

testArray, testTarget = [1,3,5,6], 5
print("Looking for ", testTarget, " in ", testArray)
print("Location equals ", Answer.searchInsert(testArray,testTarget))

testArray, testTarget = [1,3,5,6], 2
print("Looking for ", testTarget, " in ", testArray)
print("Location equals ", Answer.searchInsert(testArray,testTarget))

testArray, testTarget = [1,3,5,6], 7
print("Looking for ", testTarget, " in ", testArray)
print("Location equals ", Answer.searchInsert(testArray,testTarget))

testArray, testTarget = [1,3,5,6], 0
print("Looking for ", testTarget, " in ", testArray)
print("Location equals ", Answer.searchInsert(testArray,testTarget))

testArray, testTarget = [1], 0
print("Looking for ", testTarget, " in ", testArray)
print("Location equals ", Answer.searchInsert(testArray,testTarget))

testArray, testTarget = [1], 1
print("Looking for ", testTarget, " in ", testArray)
print("Location equals ", Answer.searchInsert(testArray,testTarget))