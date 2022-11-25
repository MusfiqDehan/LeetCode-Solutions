class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_array = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        result = set()
        for word in words:
            word = word.lower()
            transformations = ""
            for ch in word:
                transformations += morse_code_array[ord(ch) - 97]
            result.add(transformations)
        return len(result)
        