"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.
 1. 1 step + 1 step 2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.
 1. 1 step + 1 step + 1 step 2. 1 step + 2 steps 3. 2 steps + 1 step

Submission Result: Wrong Answer More Details 

Input:
6
Output:
11
Expected:
13
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        combinations = 0
        runningTotal = 0

        # check for the number of two-steps
        for x in range(n):
            
            # multiply the counter by two to account for the current value of two-steps
            runningTotal = 2 * x

            if runningTotal == n:
                # if we've reached the limit with the two-steps then add to our 
                # found combinations
                combinations += 1
           
            # check for the number of two-steps
            for y in range(n + 1):
                # set the runningTotal to the value of two-steps and current single-steps
                runningTotal = ((x * 2) + y)

                # if we've reached the limit add the occurance and the varients 
                # (same values different placement)
                if runningTotal == n:
                    if y!=0:
                        # add a found solution when y is not zero
                        combinations += 1

                    # when our x counter is not zero add the varients 
                    if (x != 0) and ((x * 2) != n):
                    # Grab all the other positions that the current solution can be 
                    # configured as, minus the one that we've already found
                        combinations += ((x + y) -1)


        return(combinations)

           
    def climbStairs_n_print(self, n):
        """
        :type n: int
        :rtype: int
        """
        combinations = 0
        runningTotal = 0
        testArray = []

        # check for the number of two-steps
        for x in range(n):
            
            # multiply the counter by two to account for the current value of two-steps
            runningTotal = 2 * x
            if x != 0:
                for i in range (x):
                    testArray.append(2)

            if runningTotal == n:
                # if we've reached the limit with the two-steps then add to our 
                # found combinations
                combinations += 1
                print("testArray",testArray)
                testArray = []
            
            # check for the number of two-steps
            for y in range(n + 1):
                # set the runningTotal to the value of two-steps and current single-steps
                runningTotal = ((x * 2) + y)
                if (y != 0) and (((x * 2) + y) <= n):
                    testArray.append(1)

                # if we've reached the limit add the occurance and the varients 
                # (same values different placement)
                if runningTotal == n:
                    if y!=0:
                        # add a found solution when y is not zero
                        combinations += 1
                        print("testArray",testArray)
                        testArray = []


                    # when our x counter is not zero add the varients 
                    if (x != 0) and ((x * 2) != n):
                    # Grab all the other positions that the current solution can be 
                    # configured as, minus the one that we've already found
                        combinations += ((x + y) -1)


        return(combinations)    

answer = Solution()

"""
testData = 2

print("testData = ", testData)
print("Combinations = ", answer.climbStairs(testData))

testData = 3

print("testData = ", testData)
print("Combinations = ", answer.climbStairs(testData))


testData = 4

print("testData = ", testData)
print("Combinations = ", answer.climbStairs(testData))



testData = 5

print("testData = ", testData)
print("Combinations = ", answer.climbStairs(testData))
"""
testData = 6

print("testData = ", testData)
print("Combinations = ", answer.climbStairs_n_print(testData))
"""
testData = 10

print("testData = ", testData)
print("Combinations = ", answer.climbStairs(testData))

testData = 100

print("testData = ", testData)
print("Combinations = ", answer.climbStairs(testData))
"""