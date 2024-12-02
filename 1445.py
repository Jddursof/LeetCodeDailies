class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent=sentence.split(" ")
        for i in range(len(sent)):
            word=sent[i]
            if searchWord==word[:len(searchWord)]:
                return i+1
        return -1