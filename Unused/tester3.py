import nltk
from nltk import word_tokenize
from nltk.corpus import cmudict
from nltk.corpus import words

# Download the CMU Pronouncing Dictionary data
nltk.download('cmudict')
nltk.download('words')
nltk.download('cmusyllables')

from nltk.tokenize.sonority_sequencing import SyllableTokenizer

# Initialize the syllable tokenizer
syllable_tokenizer = SyllableTokenizer()

# Function to get the phonetic representation of a word using the CMU Pronouncing Dictionary
def get_phonetic(word, prondict):
    # Convert the word to lowercase before looking it up in the dictionary
    word = word.lower()
    word_syllables = prondict.get(word, [['UNKNOWN']])
    syllables = [syl for syl in word_syllables[0] if syl.isalpha()]
    return syllables

# Read lyrics from a file
with open("lyrics.txt", "r") as file:
    lines = file.read().split("\n")

# Initialize the dataset
dataset = []

# Get the CMU Pronouncing Dictionary
prondict = cmudict.dict()

# Initialize the current line number
current_line = 1

# Process each line separately
for line in lines:
    # Tokenize the lyrics into words for the current line
    words = word_tokenize(line)

    # Process the words for the current line
    for word in words:
        # Convert the word to lowercase to improve phonetic lookup
        word = word.lower()

        # Determine the rhyme group for each word manually or using a library
        rhyme_group = 0  # Replace with actual rhyme group logic

        # Get the phonetic representation (syllables) for the word
        phonetic_syllables = get_phonetic(word, prondict)

        # Create a separate entry for each syllable
        for syllable in phonetic_syllables:
            dataset.append((current_line, word, syllable, rhyme_group))

    # Increment the current line number for the next line
    current_line += 1

# Print the dataset
for entry in dataset:
    print(entry)
