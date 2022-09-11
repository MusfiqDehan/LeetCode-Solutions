from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        arr=[n for n in nums if n%2==0]
        print(arr)
        
        if(not arr):
            return -1
        
        count=Counter(arr)
        print(count)
        
        d=defaultdict(list)
        print(d)
        
        for k,v in count.items():
            d[v].append(k)
        print(d)
        
        res = min(d[max(count.values())]) 
        return res