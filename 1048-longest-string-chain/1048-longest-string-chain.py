class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        l_words = defaultdict(list)
        for word in words:
            l_words[len(word)].append(word)

        word_map = {}
        for word in words:
            word_map[word] = 1
        
        keys = sorted(l_words.keys(), reverse=True)
        for k_idx, k in enumerate(keys[:-1]):
            if k-1 in keys:
                for word in l_words[k]:
                    for i in range(len(word)):
                        prev = word[:i]+word[i+1:]
                        if prev in l_words[k-1]:
                            word_map[prev] = max(word_map[prev], word_map[word]+1)
        return max(word_map.values())