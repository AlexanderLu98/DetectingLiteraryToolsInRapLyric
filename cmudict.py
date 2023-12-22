import nltk
from collections import defaultdict

# Download the cmudict corpus if it's not already downloaded
nltk.download('cmudict')

# Load the cmudict corpus into a Python dictionary
cmudict = nltk.corpus.cmudict.dict()

# Initialize a dictionary to hold the counts of words by syllable count
counts_by_syllable_count = defaultdict(int)

# Iterate over the words in the dictionary
for word, pronunciations in cmudict.items():
    # For each word, check the first pronunciation
    pronunciation = pronunciations[0]
    
    # Count the number of syllables (phonemes with a digit in them)
    syllable_count = sum(1 for phoneme in pronunciation if any(char.isdigit() for char in phoneme))
    
    # Update the count for this syllable count
    counts_by_syllable_count[syllable_count] += 1

# Print the counts of words by syllable count
for syllable_count, count in counts_by_syllable_count.items():
    print(f"Number of {syllable_count}-syllable words: {count}")
