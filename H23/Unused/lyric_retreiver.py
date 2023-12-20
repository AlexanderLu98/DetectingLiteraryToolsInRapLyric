import requests
from bs4 import BeautifulSoup

# URL of the song lyrics page
lyrics_url = "https://www.azlyrics.com/lyrics/icespice/prettygirl.html"

# Send an HTTP GET request to the lyrics URL
response = requests.get(lyrics_url)

if response.status_code == 200:
    # Parse the HTML content of the page with Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the lyrics section (may vary depending on the website's structure)
    lyrics_section = soup.find('div', class_='col-xs-12 col-lg-8 text-center')

    # Extract and print the lyrics
    if lyrics_section:
        lyrics = lyrics_section.get_text()
        print(lyrics)
    else:
        print("Lyrics not found on the page")
else:
    print("Failed to retrieve lyrics. Status code:", response.status_code)
