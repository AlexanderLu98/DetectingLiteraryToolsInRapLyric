import lyricsgenius
import os

# Replace 'your_access_token' with your actual Genius.com access token
genius = lyricsgenius.Genius('NWG-NDg462DSE3cYXI5FZy8XMdUxgKsqFCyt3eDygTV1LYAN06_S_TKNGpQzJ1oM')

# Read the songs from the text file
with open('list.txt', 'r') as f:
    songs = [line.strip() for line in f]

# Create the lyrics directory if it doesn't exist
os.makedirs('lyrics/txt', exist_ok=True)

not_found_songs = []

for song in songs:
    # Try different separators for artist and title
    for sep in [' on ', ' - ', ' / ']:
        if sep in song:
            artist, title = song.split(sep, 1)
            break
    else:
        # If no separator is found, use the whole line as the title
        artist, title = None, song

    if artist and title:
        try:
            song = genius.search_song(title.strip(), artist.strip())
            if song is not None:
                with open(f'lyrics/txt/{artist.strip()} - {title.strip()}.txt', 'w', encoding='utf-8') as f:
                    f.write(song.lyrics)
            else:
                not_found_songs.append(song)
        except Exception as e:
            print(f"An error occurred while processing '{artist} - {title}': {e}")
    else:
        not_found_songs.append(song)

# Write the not found songs to a file
with open('lyrics/notFound.txt', 'w', encoding='utf-8') as f:
    for song in not_found_songs:
        f.write(song + '\n')
