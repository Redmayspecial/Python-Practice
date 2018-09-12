"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Input:
[-2,1]
Output:
-1
Expected:
1
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numLength = len(nums)
        x = 0

        if numLength != 0:
            highestScore = nums[0]

        else:
            return numLength                
        

        while x <= (numLength-1):
            y = x
            runningArray = []
            
            while y <= (numLength-1):
                if x == y:
                    runningTotal = nums[x]
                    runningArray.append(nums(x))

                    if nums[x] > highestScore:
                        # make x the highestScore   
                        highestScore = nums[x]
                        # add x to the array
                
                else:
                    runningTotal += nums[y]
                    runningArray.append(nums(y))

                    if runningTotal > highestScore:
                        # make x + y the highestScoreyz
                        highestScore = runningTotal
                           
                
                y += 1

            x += 1

        return highestScore






        


Answer = Solution()
"""
testArray = [-2,1,-3,4,-1,2,1,-5,4]

print("testArray =", testArray, "Largest sum = ", Answer.maxSubArray(testArray))

testArray = [-2,-3,-1,-5]

print("testArray =", testArray, "Largest sum = ", Answer.maxSubArray(testArray))
"""
testArray = [-2,1]

print("testArray =", testArray, "Largest sum = ", Answer.maxSubArray(testArray))
"""
testArray = []

print("testArray =", testArray, "Largest sum = ", Answer.maxSubArray(testArray))
"""