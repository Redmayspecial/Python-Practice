"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".


Input:
"1111"
"1111"
Output:
"10000"
Expected:
"11110"

"""
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        aLength = len(a)
        bLength = len(b)
        add1toNextColumn = False
        setinthisloop = False
        override = False
        index = 0
        answerArray = []
        answer = ""

        #reverse the strings in order to be able to add from right to left effectively.
        a = a[::-1]
        b = b[::-1]


        while (index < aLength) or (index < bLength):
            
            # code for adding together numbers
            if (index < aLength) and (index < bLength):
                if add1toNextColumn:
                    override = True

                if a[index] == "1" and b[index] == "1":
                    answerArray.append("0")
                    add1toNextColumn = True
                    setinthisloop = True

                elif a[index] == "0" and b[index] == "0":
                    answerArray.append("0")

                else:
                    answerArray.append("1")

            # code for mismatching lengths
            elif (index < aLength) or (index < bLength):
                
                if index < aLength:
                    answerArray.append(a[index]) 
                else:
                    answerArray.append(b[index]) 

            # Add the carried number IF it's carried over from the previous column
            if (add1toNextColumn and not setinthisloop) or override:
                
                if answerArray[index] == "1":
                    answerArray[index] = "0"
                    if add1toNextColumn and setinthisloop:
                        # added due to override 
                        add1toNextColumn = True  
                    else:
                        add1toNextColumn = False    
                        

                elif answerArray[index] == "0":
                    answerArray[index] = "1"
                    if add1toNextColumn and setinthisloop:
                        # added due to override
                        add1toNextColumn = True
                    else:
                        add1toNextColumn = False                             
                        

            # now that we are at the end of the loop clear the looplimiter
            if setinthisloop:
                setinthisloop = False
            
            override = False
            
            index += 1
        
        #if there is an outstanding carried unit add that now.
        if add1toNextColumn:
            answerArray.append("1")
            add1toNextColumn = False   

        # reverse the answer output
        answerArray.reverse()
        for item in answerArray:
            answer += str(item)


        return(answer)                         




    def addBinary_print(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        aLength = len(a)
        bLength = len(b)
        add1toNextColumn = False
        setinthisloop = False
        index = 0
        answerArray = []
        answer = ""

        # print("alength = ", aLength)
        # print("blength = ", bLength)

        #reverse the strings in order to be able to add from right to left effectively.
        a = a[::-1]
        b = b[::-1]

        # print("answer =", answer)

        while (index < aLength) or (index < bLength):

            # if (index < aLength):
            #     print("aindex = ", a[index])
            # if (index < bLength):
            #     print("bindex = ", b[index])

            if (index < aLength) and (index < bLength):
                if a[index] == "1" and b[index] == "1":
                    answerArray.append("0")
                    # print("adding 1 & 1 together")
                    # print("answer =", answerArray[index])
                    # print("answer =", answerArray)
                    add1toNextColumn = True
                    setinthisloop = True
                elif a[index] == "0" and b[index] == "0":
                    answerArray.append("0")
                    # print("adding 0 & 0 together")
                    # print("answer =", answerArray[index])
                    # print("answer =", answerArray)
                else:
                    answerArray.append("1")
                    # print("adding 1 & 0 together")
                    # print("answer =", answerArray[index])
                    # print("answer =", answerArray)

            # code for mismatching lengths
            elif (index < aLength) or (index < bLength):
                if index < aLength:
                    answerArray.append(a[index]) 
                    # print("adding a's value of ", a[index])
                    # print("answer =", answerArray[index])
                    # print("answer =", answerArray)
                else:
                    answerArray.append(b[index]) 
                    # print("adding a's value of ", b[index])
                    # print("answer =", answerArray[index])
                    # print("answer =", answerArray)

            if (add1toNextColumn and not setinthisloop) or override:
                if answerArray[index] == "1":
                    answerArray[index] = "0"
                    # print("adding a carried value of ", 0)
                    # print("answer =", answerArray[index])
                    # print("answer =", answerArray)
                    #add1toNextColum remains true
                elif answerArray[index] == "0":
                    answerArray[index] = "1"
                    # print("adding a carried value of ", 1)
                    # print("answer =", answerArray[index])
                    # print("answer =", answerArray)
                    add1toNextColumn = False                              

            if setinthisloop:
                setinthisloop = False
            override = False

            index += 1
        
        #if there is an outstanding carried unit add that now.
        if add1toNextColumn:
            answerArray.append("1")
            # print("adding a carried value of ", 1)
            # print("answer =", answerArray[index])
            # print("answer =", answerArray)
            add1toNextColumn = False   

        # reverse the answer output
        answerArray.reverse()
        # print("answerArray in reverse = ",answerArray)
        for item in answerArray:
            answer += str(item)
            # print("building answer ", answer)


        return(answer)                         





answer = Solution()

testStringA = "11"
testStringB = "1"

print("Adding Strings ",testStringA," & ",testStringB,
 " yields = ",answer.addBinary(testStringA,testStringB))


testStringA = ""
testStringB = "11"

print("Adding Strings ",testStringA," & ",testStringB,
 " yields = ",answer.addBinary(testStringA,testStringB))

testStringA = "11"
testStringB = ""

print("Adding Strings ",testStringA," & ",testStringB,
 " yields = ",answer.addBinary(testStringA,testStringB))

testStringA = "0"
testStringB = "0"

print("Adding Strings ",testStringA," & ",testStringB,
 " yields = ",answer.addBinary(testStringA,testStringB)) 

testStringA = "001"
testStringB = "0000111"

print("Adding Strings ",testStringA," & ",testStringB,
 " yields = ",answer.addBinary(testStringA,testStringB)) 

testStringA = "1111"
testStringB = "1111"

print("Adding Strings ",testStringA," & ",testStringB,
 " yields = ",answer.addBinary(testStringA,testStringB)) 