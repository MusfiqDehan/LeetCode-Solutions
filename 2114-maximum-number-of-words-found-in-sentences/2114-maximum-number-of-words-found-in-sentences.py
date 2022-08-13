class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length_of_sentences = []
        
        for i in sentences:
            length_of_sentences.append(len(i.split()))
            
        return max(length_of_sentences)
        