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

# Find rhymes using the "pronouncing" library
rhymes = {}
for word in tokens:
    rhymes[word] = pronouncing.rhymes(word)

# Automatically generate color mapping based on rhyming patterns
color_mapping = {}
color_counter = 1

for word, rhyme_words in rhymes.items():
    if rhyme_words:
        rhyme_pattern = ",".join(rhyme_words)
        if rhyme_pattern not in color_mapping:
            color_mapping[rhyme_pattern] = f"\033[3{color_counter}m"  # Assign a color code
            color_counter = (color_counter % 6) + 1  # Cycle through ANSI color codes

# Color-coding based on rhyme with dynamically generated colors
color_coded_lyrics = []
ipa_lyrics = []  # Store IPA version of lyrics

for word in tokens:
    rhyme_words = rhymes.get(word, [])
    rhyme_pattern = ",".join(rhyme_words)
    color_code = color_mapping.get(rhyme_pattern, "\033[39m")  # Default color if not found

    # Get the IPA pronunciation of the word using the pronouncing library
    ipa_pronunciation = pronouncing.phones_for_word(word)
    
    if ipa_pronunciation:
        # Concatenate IPA syllables without spaces
        ipa_word = "".join(ipa_pronunciation[0].split())
        ipa_lyrics.append(ipa_word)
    else:
        ipa_lyrics.append(word)  # Use the original word if IPA not found

    color_coded_lyrics.append((word, color_code))

# Print color-coded lyrics and combined IPA version
for word, color_code in color_coded_lyrics:
    print(f"{color_code}{word}\033[0m", end=" ")

print("\n")

# Combine and print the IPA version of the lyrics
combined_ipa_lyrics = " ".join(ipa_lyrics)
print("IPA Version of Lyrics:")
print(combined_ipa_lyrics)
