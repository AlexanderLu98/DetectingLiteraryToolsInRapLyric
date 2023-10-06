import re
from nltk import word_tokenize
from nltk.corpus import cmudict

# Define a function to tokenize and preprocess the text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    return text

# Define a function to find rhyming words using CMU Pronouncing Dictionary
def find_rhymes(word):
    pronouncing_dict = cmudict.dict()
    if word in pronouncing_dict:
        return pronouncing_dict[word][0]
    else:
        return []

# Sample rap lyrics
rap_lyrics = """
Yo, I'm on a mission, spittin' with precision
Listen to my vision, risin' with ambition
I'm winnin', grinnin', never sinnin', always grinnin'
"""

# Tokenize and preprocess the lyrics
tokens = word_tokenize(preprocess_text(rap_lyrics))

# Find rhymes
rhymes = {}
for word in tokens:
    rhymes[word] = tuple(find_rhymes(word))  # Convert rhyme patterns to tuples

# Automatically generate color mapping based on rhyming patterns
color_mapping = {}
color_counter = 1

for word, rhyme_pattern in rhymes.items():
    if rhyme_pattern not in color_mapping:
        color_mapping[rhyme_pattern] = f"\033[3{color_counter}m"  # Assign a color code
        color_counter = (color_counter % 6) + 1  # Cycle through ANSI color codes

# Color-coding based on rhyme with dynamically generated colors
color_coded_lyrics = []
for word in tokens:
    color_code = color_mapping.get(rhymes.get(word, ()), "\033[39m")  # Default color if not found
    color_coded_lyrics.append((word, color_code))

# Print color-coded lyrics
for word, color_code in color_coded_lyrics:
    print(f"{color_code}{word}\033[0m", end=" ")

print("\n")
