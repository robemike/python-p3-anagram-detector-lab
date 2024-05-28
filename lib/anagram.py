# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = sorted(word.lower())
    
    
    def match(self, anagrams):
        sorted_anagrams = [sorted(possible_anagram.lower()) for possible_anagram in anagrams]
        return [anagram for anagram in anagrams if sorted_anagrams[anagrams.index(anagram)] == self.word]
