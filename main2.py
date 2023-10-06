import re
from nltk import word_tokenize
import pronouncing

# Define a function to tokenize and preprocess the text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    return text

# Sample rap lyrics
rap_lyrics = """
Ha, sicker than your average
Poppa twist cabbage off instinct
Niggas don't think shit stink
Pink gators, my Detroit players
"""

# Tokenize and preprocess the lyrics
tokens = word_tokenize(preprocess_text(rap_lyrics))

# Define the provided rhyme pattern
rhyme_pattern = [
    "Ha, sick1-er than your ave2-rage1",
    "Poppa twist1 cab2-bage1 off3 in4-stinct1",
    "Nig1-gas don't3 think4 shit1 stink4",
    "Pink4 ga5-tors6, my Detroit play5-ers6"
]

# Create a mapping of words to their corresponding rhyme numbers
rhyme_mapping = {}
for line in rhyme_pattern:
    words = line.split()
    for word in words:
        match = re.match(r'(.+?)(\d+)', word)
        if match:
            word, rhyme_number = match.groups()
            rhyme_mapping[word] = rhyme_number

# Automatically generate color mapping based on rhyme numbers
color_mapping = {}
color_counter = 1

for word in tokens:
    rhyme_number = rhyme_mapping.get(word)
    if rhyme_number:
        if rhyme_number not in color_mapping:
            color_mapping[rhyme_number] = f"\033[3{color_counter}m"  # Assign a color code
            color_counter = (color_counter % 6) + 1  # Cycle through ANSI color codes

# Color-coding based on rhyme numbers with dynamically generated colors
color_coded_lyrics = []

for word in tokens:
    rhyme_number = rhyme_mapping.get(word)
    color_code = color_mapping.get(rhyme_number, "\033[39m")  # Default color if not found
    color_coded_lyrics.append((word, color_code))

# Print color-coded lyrics
for word, color_code in color_coded_lyrics:
    print(f"{color_code}{word}\033[0m", end=" ")

print("\n")
