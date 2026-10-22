class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        binaryStr = bin(n) # get binary as string
        for i in binaryStr: # iterate through number
            if (i == "1"):
                count += 1
        return count