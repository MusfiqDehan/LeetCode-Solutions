class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        h={}
        alpha="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(order)):
            h[order[i]]=alpha[i]
        def change(word):
            s=""
            for i in word:
                s+=h[i]
            return s
        if words==sorted(words,key=lambda x:change(x)):
            return True
        return False
        