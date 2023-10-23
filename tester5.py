import nltk
from nltk import word_tokenize
from nltk.corpus import cmudict
import pyphen
import csv
import os

# Download the CMU Pronouncing Dictionary data
nltk.download('cmudict')

# Function to get the phonetic representation of a word using the CMU Pronouncing Dictionary
def get_phonetic(word, prondict):
    word = word.lower()
    word_syllables = prondict.get(word, [['UNKNOWN']])
    return word_syllables[0]

# Read lyrics from a file
with open("lyrics.txt", "r") as file:
    lines = file.read().split("\n")

# Initialize the dataset
dataset = []

# Get the CMU Pronouncing Dictionary
prondict = cmudict.dict()

# Initialize the pyphen dictionary
pyphen_dict = pyphen.Pyphen(lang='en_US')

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

        # Get the phonetic representation for the word using the CMU Pronouncing Dictionary
        word_phonetic = get_phonetic(word, prondict)

        # Join the phonetic syllables for the word with a space
        word_phonetic = ' '.join(word_phonetic)

        dataset.append((current_line, word, word_phonetic, rhyme_group))

    # Increment the current line number for the next line
    current_line += 1

# # Print the dataset
# for entry in dataset:
#     print(entry)

def group_syllables(dataset):
    new_dataset = []
    current_entry = None

    for entry in dataset:
        line_number, word, phonetic, rhyme_group = entry

        if current_entry is None:
            # Initialize the current entry
            current_entry = (line_number, word, [phonetic], rhyme_group)
        elif current_entry[0] == line_number and current_entry[1] == word:
            # If the same word and line, append the syllable to the current entry
            current_entry[2].append(phonetic)
        else:
            # If a new word or line, add the current entry to the new dataset
            joined_phonetic = ' '.join(current_entry[2])
            new_dataset.append((current_entry[0], current_entry[1], joined_phonetic, current_entry[3]))
            current_entry = (line_number, word, [phonetic], rhyme_group)

    if current_entry is not None:
        # Add the last current entry to the new dataset
        joined_phonetic = ' '.join(current_entry[2])
        new_dataset.append((current_entry[0], current_entry[1], joined_phonetic, current_entry[3]))

    return new_dataset


# Print the dataset
new_dataset = group_syllables(dataset)

def save_to_csv(dataset, output_file):
    output_folder = 'datasets'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, output_file)

    with open(output_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write a header row if needed
        csv_writer.writerow(['Line Number', 'Word', 'Phonetic', 'Rhyme Group'])
        # Write the data
        for entry in dataset:
            csv_writer.writerow(entry)

# Call the save_to_csv function to save the grouped dataset
output_file = "test.csv"
save_to_csv(new_dataset, output_file)

for entry in new_dataset:
    print(entry)