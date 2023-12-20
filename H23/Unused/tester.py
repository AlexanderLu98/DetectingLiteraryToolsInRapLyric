import pyphen
import re

# Initialize the Pyphen dictionary
dic = pyphen.Pyphen(lang='en_US')

# Define a function to tokenize text into syllables
def tokenize_into_syllables(text):
    # Remove special characters and split the text into words
    words = re.findall(r'\b\w+\b', text)

    # Tokenize each word into syllables
    syllable_tokens = []
    for word in words:
        syllables = dic.inserted(word).split('-')
        syllable_tokens.extend(syllables)

    return syllable_tokens

# Example rap lyric
rap_lyric = "I drop the illest rhymes, no one can stop my climb"

# Tokenize the rap lyric into syllables
syllables = tokenize_into_syllables(rap_lyric)

# Print the syllables
for syllable in syllables:
    print(syllable)
