import pandas as pd
from collections import defaultdict
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize
import pyphen
import re

# Initialize the CMU Pronouncing Dictionary
d = cmudict.dict()

def get_phonetic(word):
    """Return the phonetic transcription of a word."""
    return d[word.lower()][0] if word.lower() in d else word

# Initialize a list to store your data
data = []

# Initialize a Pyphen object for syllable division
dic = pyphen.Pyphen(lang='en')

# Read the lyrics from a text file
with open('lyrics.txt', 'r') as f:
    lyrics = f.read().split('\n')

for i, line in enumerate(lyrics):
    words = word_tokenize(line)
    for j, word in enumerate(words):
        # Get the phonetic transcription of the word
        phonetic = get_phonetic(word)
        # Divide the word into syllables
        syllables = dic.inserted(word).split("-")
        for k, syllable in enumerate(syllables):
            # Add the data to the list
            data.append((i+1, j+1, k+1, syllable, phonetic, None, None))

# Convert the list to a DataFrame
df = pd.DataFrame(data, columns=["LineID", "WordID", "SyllableID", "Syllable", "Phonetic", "RhymeGroup", "IsRhyme"])

print(df)
