import os 
import nltk
import logging
import random

logging.basicConfig(level=logging.INFO)
phone_dictionary = nltk.corpus.cmudict.dict()

def possible_phones(word):
    return phone_dictionary.get(word, [])

def phon_match(first_phon, second_phon, start, end):
    first_range = first_phon[start:end][::-1]
    second_range = second_phon[start:end][::-1]
    hits = sum(phone1 == phone2 for phone1, phone2 in zip(first_range, second_range))
    return hits / len(first_range)

def word_similarity(first_word, second_word, start_phone=None, end_phone=None):
    first_phones = possible_phones(first_word)
    second_phones = possible_phones(second_word)
    if not first_phones or not second_phones:
        return 0
    return max(phon_match(f_p, s_p, start_phone, end_phone) for f_p in first_phones for s_p in second_phones)

def mark_with_rhymes(lyrics):
    mark_copy = lyrics.copy()
    colorlist = [-1] * len(mark_copy)
    found_rhymes = 0
    for idx, rhymer in enumerate(lyrics):
        for rhymee in mark_copy[idx + 1:]:
            if word_similarity(rhymer, rhymee, start_phone=-2) > 0:
                mark_copy[idx] = str(found_rhymes) + rhymer + str(found_rhymes)
                colorlist[idx] = found_rhymes
                found_rhymes += 1
    return colorlist, mark_copy

def analyze_lyrics(lyrics):
    return [mark_with_rhymes(section) for section in lyrics if section]

def parse_and_analyze_lyrics(lyrics_files):
    for lyrics_file in lyrics_files:
        with open(lyrics_file, 'r') as file:
            lyrics = file.read().split()
            results = analyze_lyrics([lyrics])
            for rhyme_num, marked in results:
                print(f"Results for {lyrics_file}:\n{rhyme_num}\n{marked}")


if __name__ == "__main__":
    lyrics_dir = "testfolder"
    lyrics_files = [os.path.join(lyrics_dir, file) for file in os.listdir(lyrics_dir) if file.endswith(".txt")]
    parse_and_analyze_lyrics(lyrics_files)
