class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
        arra = []
        j = 0
        while (len(nums)) != 0:
            for i in range(len(nums)):
                if nums[i] not in arr[j]:
                    arr[j].append(nums[i])
                    arra.append(nums[i])
                else:
                    continue
            for k in range(len(arra)):
                nums.remove(arra[k])
            j += 1
            arra=[]
            arr.append([])
        return arr[:-1]
        