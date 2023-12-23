class Solution:
    def isPathCrossing(self, path: str) -> bool:
        arr=[x for x in path]
        x=0
        y=0
        n=[]
        flag=False
        n.append([0,0])
        for i in range(len(arr)):
            if arr[i]=="N":
                y+=1
            elif arr[i]=="S":
                y-=1
            elif arr[i]=="E":
                x+=1
            else:
                x-=1
            if [x,y] not in n:
                n.append([x,y])
            else:
                flag=True
                break
        return flag
        