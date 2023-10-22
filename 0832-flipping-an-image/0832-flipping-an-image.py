class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        out = []
        for arr in image:
            reverse_arr =  [1 if value == 0 else 0 for value in arr[::-1]]
            out.append(reverse_arr)
        return out