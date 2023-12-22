import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import cmudict

nltk.download('cmudict')
arpabet = cmudict.dict()

def process_input(input_string, word):
    # Remove the prefix
    input_string = input_string.replace(f"Divide {word} into syllables: ", "")
    
    # Find the index of "Stressed"
    index = input_string.find("Stressed")
    
    # If "Stressed" is found, remove everything after and including it
    if index != -1:
        input_string = input_string[:index]
    
    # Remove all spaces
    input_string = input_string.replace(" ", "")
    
    # Strip leading and trailing spaces
    input_string = input_string.strip()

    return input_string

def get_syllable_count(word):
    url = f"https://www.howmanysyllables.com/syllables/{word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    syllable_count = soup.find('p', {'id': 'SyllableContentContainer'}).text
    syllable = process_input(syllable_count,word)
    
    # Get the ARPAbet representation
    arpabet_repr = arpabet[word.lower()][0] if word.lower() in arpabet else None

    # Group the ARPAbet phonemes according to the syllables
    syllable_arpabet = []
    if arpabet_repr is not None:
        syllables = syllable.split('-')
        arpabet_index = 0
        for syl in syllables:
            syl_arpabet = []
            for char in syl:
                while arpabet_index < len(arpabet_repr) and char in arpabet_repr[arpabet_index].lower():
                    syl_arpabet.append(arpabet_repr[arpabet_index])
                    arpabet_index += 1
            syllable_arpabet.append(''.join(syl_arpabet))

    return syllable, arpabet_repr, syllable_arpabet

# Example usage:
syllable, arpabet_repr, syllable_arpabet = get_syllable_count("example")
print(f"Word: example\nSyllables: {syllable}\nARPAbet: {arpabet_repr}\nSyllable ARPAbet: {syllable_arpabet}")