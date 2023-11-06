import pandas as pd
from collections import defaultdict
from nltk.tokenize import word_tokenize
import pyphen
import re
import eng_to_ipa as ipa
from phonemizer import phonemize

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
        phonetic = ipa.convert(word)
        # Divide the word and its phonetic transcription into syllables
        word_syllables = dic.inserted(word).split("-")
        phonetic_syllables = phonemize(phonetic, language='en-us', backend='espeak', strip=True).split(" ")
        for k, (word_syllable, phonetic_syllable) in enumerate(zip(word_syllables, phonetic_syllables)):
            # Add the data to the list
            data.append((i+1, j+1, k+1, word_syllable, phonetic_syllable, None, None))

# Convert the list to a DataFrame
df = pd.DataFrame(data, columns=["LineID", "WordID", "SyllableID", "Syllable", "Phonetic", "RhymeGroup", "IsRhyme"])

print(df)
