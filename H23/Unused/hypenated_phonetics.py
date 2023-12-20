import nltk
from nltk.corpus import cmudict

# Load the CMU Pronouncing Dictionary
d = cmudict.dict()

def hyphenated_to_phonetic(word):
    # Split the word into syllables
    syllables = word.split('-')
    
    # Convert each syllable to phonetics
    phonetic_word = '-'.join([' '.join(d[syllable][0]) for syllable in syllables])
    
    return phonetic_word

# Example usage:
word = 'ex-am-ple'
print(hyphenated_to_phonetic(word))
