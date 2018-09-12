"""
LeetCode - Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum(nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      for x in range(len(nums)-1):
        for y in range(len(nums)-1):
          if (nums[(x] + nums[y+1]) == target) and (x != y+1): 
            return[x,y+1]



# for local debugging purposes
testNumbers = [3,2,4]
seekingSum = 6

print("Number Array: ", testNumbers)
print("Desired sum: ", seekingSum)
print(twoSum(testNumbers, seekingSum))

# for local debugging purposes
testNumbers = [2,5,5,11]
seekingSum = 10

print("Number Array: ", testNumbers)
print("Desired sum: ", seekingSum)
print(twoSum(testNumbers, seekingSum))






