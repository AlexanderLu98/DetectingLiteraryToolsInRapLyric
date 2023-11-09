import pandas as pd
from collections import defaultdict
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize
import pyphen
import re
import os

# Initialize the CMU Pronouncing Dictionary
d = cmudict.dict()

def get_phonetic(word):
    """Return the phonetic transcription of a word."""
    return d[word.lower()][0] if word.lower() in d else word

# Initialize a list to store your data
data = []

# Initialize a Pyphen object for syllable division
dic = pyphen.Pyphen(lang='en')

# Specify the directory containing the text files
directory = 'lyrics/final preproccess txt/first group'

# Iterate over all text files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        # Extract the artist name and song name from the filename
        artist_name, song_name = filename[:-4].split(' - ')
        # Read the lyrics from the text file
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            lyrics = f.read().split('\n')
        for i, line in enumerate(lyrics):
            # Remove words inside parentheses
            line = re.sub(r'\([^)]*\)', '', line)
            # Remove punctuation from the line
            line = re.sub(r'[^\w\s\']', '', line)
            words = word_tokenize(line)
            for j, word in enumerate(words):
                # Get the phonetic transcription of the word
                phonetic = get_phonetic(word)
                found_in_cmu = word.lower() in d
                # Divide the word into syllables
                syllables = dic.inserted(word).split("-")
                for k, syllable in enumerate(syllables):
                    # Add the data to the list
                    data.append((i+1, j+1, k+1, syllable, phonetic, 0, False, 0, False, found_in_cmu, artist_name, song_name))
        # Convert the list to a DataFrame
        df = pd.DataFrame(data, columns=["LineID", "WordID", "SyllableID", "Syllable", "Phonetic", "RhymeGroup", "IsRhyme", "AlliterationSound", "IsAlliteration", "FoundInCMU", "ArtistName", "SongName"])
        # Save the DataFrame to a CSV file in a specific folder
        df.to_csv('lyrics/csv/' + filename[:-4] + '.csv', index=False)
        print(df)
