class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for i in nums:
            if i in visited:
                visited[i] += 1
            else:
                visited[i] = 1
        
        for j in visited:
            if visited[j] > 1:
                return True
            
        return False