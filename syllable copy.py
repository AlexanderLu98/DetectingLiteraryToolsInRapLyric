import requests
from bs4 import BeautifulSoup

def process_output(output_string):
    pronunciation = [line for line in output_string.split('\n') if line][-1]
    pronunciation = pronunciation.strip()
    return pronunciation

def get_pronunciation(word):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    pronunciation = soup.find('span', {'class': 'us dpron-i'}).text
    return pronunciation

def process_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        for word in f_in:
            word = word.strip()  # remove newline character
            output = get_pronunciation(word)
            pronunciation = process_output(output)
            f_out.write(f'{word}: {pronunciation}\n')

# Example usage:
process_words("top1000.txt", "pronunciations.txt")
