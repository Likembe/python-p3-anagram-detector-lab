class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        # Convert the input word to lowercase and sort its characters
        sorted_word = sorted(self.word)

        # Initialize an empty list to store the matching anagrams
        matches = []

        for candidate in possible_anagrams:
            # Convert the candidate to lowercase and sort its characters
            sorted_candidate = sorted(candidate.lower())

            # Check if the sorted candidate matches the sorted word and is not the same as the original word
            if sorted_word == sorted_candidate and self.word != candidate.lower():
                matches.append(candidate)

        return matches

# Example usage:
word = 'loogeg'
possible_anagrams = ['enlists', 'google', 'inlets', 'banana']
anagram_finder = Anagram(word)
result = anagram_finder.match(possible_anagrams)
print(result)
