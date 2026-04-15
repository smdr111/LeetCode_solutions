class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        lower_letters = list(string.ascii_lowercase)
        reversed_letters = lower_letters[::-1]
        result = ''
        for i in range(len(words)):
            k = 0
            for j in words[i]:
                k += weights[lower_letters.index(j)]
            result += reversed_letters[k%26]
        return result
            




        
