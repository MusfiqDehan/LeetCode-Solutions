class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        for box in boxTypes:
            if truckSize:
                if box[0] <= truckSize:
                    count += (box[1]*box[0])
                    truckSize -= box[0]
                else:
                    count += (truckSize*box[1])
                    truckSize =0
            else:
                return count
        return count
   