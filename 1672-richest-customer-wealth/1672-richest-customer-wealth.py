class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumList = []
        for i in accounts:
            sumList.append(sum(i))
            
        return max(sumList)
            
        