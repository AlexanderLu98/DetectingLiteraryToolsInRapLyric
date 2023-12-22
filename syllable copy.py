import requests
from bs4 import BeautifulSoup


def process_output(output_string):
    # Split the string by newline characters and keep only the last non-empty line
    pronunciation = [line for line in output_string.split('\n') if line][-1]
    
    # Remove leading and trailing spaces
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

# Example usage:
output = get_pronunciation("example")
pronunciation = process_output(output)
print(pronunciation)

