def solve3(ff,chrs):
    ans = []
    for i in ff:
        if i in chrs:
            ans.append(True)
    return True if len(ans)==len(ff) else False

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = [0]*26
        for c in chars:
            cnt[ord(c)-ord('a')]+=1

        ans = 0
        for j in words:
            w_cnt = [0]*26
            for c in j:
                w_cnt[ord(c)-ord('a')]+=1
            bol = True
            for i in range(26):
                if cnt[i]<w_cnt[i]:
                    bol=False
                    break
            if bol:
                ans +=len(j)
        return (ans) 
        