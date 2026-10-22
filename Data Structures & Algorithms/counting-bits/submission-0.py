class Solution:
    def countBits(self, n: int) -> List[int]:
        
        countList = []

        for i in range(0, n + 1):
            binStr = bin(i)
            count = 0
            for j in binStr:
                if (j == "1"):
                    count += 1
            countList.append(count)

        return countList