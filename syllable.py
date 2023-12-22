import requests
from bs4 import BeautifulSoup


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
    return syllable

# Example usage:
print(get_syllable_count("example"))
