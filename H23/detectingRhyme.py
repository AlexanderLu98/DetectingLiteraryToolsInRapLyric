import os 
from copy import deepcopy
import nltk

phone_dictionary = nltk.corpus.cmudict.dict()

def get_phones(word):

    if word not in phone_dictionary:
        return []
    return phone_dictionary[word]


def phon_match(phon_1 : list, phon_2 : list,start : int, end: int) -> int:
    range_1 = phon_1[start:end]
    range_2 = phon_2[start:end]

    range_1 = range_1[::-1]
    range_2 = range_2[::-1]

    # we only want to loop through the smallest range
    if len(range_1) > len(range_2):
        range_1, range_2 = range_2, range_1
    hits = 0
    total = len(range_1)

    for idx, phone in enumerate(range_1):
        other_phone = range_2[idx]

        if phone == other_phone:
            hits += 1

            # increse weight
            if phone[-1].isdigit():
                hits += 1
                total += 1

    return hits/total

def word_similarity(word_1, word_2, start_phone=None, end_phone=None):
    #in to ing because of slang
    word_1 = word_1.strip(".!?-()").replace("in'", "ing")
    word_2 = word_2.strip(".!?-()").replace("in'", "ing")
    phones_1 = get_phones(word_1)
    phones_2 = get_phones(word_2)
    if not phones_1 or not phones_2:
        return 0

    # If there is only one pronouciation of both words
    if len(phones_1) + len(phones_2) == 2:
        phones_1 = phones_1[0]
        phones_2 = phones_2[0] 
        return phon_match(phones_1, phones_2,start_phone,end_phone)
    else:
    # multiple pronouciations for one or both words
        scorelist = []
        for p_1 in phones_1:
            for p_2 in phones_2: 
                scorelist.append(phon_match(p_1,p_2,start_phone,end_phone))
            
        if 1 in scorelist:
            return 1
        else: 
            return 0

def mark_with_rhymes(lyrics : str) -> str: 
    mark_copy = deepcopy(lyrics)
    found_rhymes = 0 
    colorlist = [-1] * len(mark_copy)

    for idx, rhyme_1 in enumerate(lyrics):
        if '[' in rhyme_1 or ']' in rhyme_1:
            print(rhyme_1)
        found = False
        for rhyme_2 in mark_copy[idx + 1:]:
            if rhyme_2 in lyrics:
                they_rhyme = False
                # Focus one syllable end rhymes
                rhyme_1_phon = get_phones(rhyme_1.strip(".!?-()").replace("in'", "ing"))
                rhyme_2_phon = get_phones(rhyme_2.strip(".!?-()").replace("in'", "ing"))

                if rhyme_1_phon == [] or rhyme_2_phon == []: 
                    they_rhyme = rhyme_1 == rhyme_2
                else:
                    #shortest pronounciation of each word 
                    shortest_rhyme_1_phon = min(rhyme_1_phon, key=len)
                    shortest_rhyme_2_phon = min(rhyme_2_phon, key=len)
                    shortest_phon = min([shortest_rhyme_2_phon,shortest_rhyme_1_phon], key=len)
                    nphones_in_shortest = 0 if (len(shortest_phon) - 1) == 0 else len(shortest_phon) - 1
                    they_rhyme = word_similarity(rhyme_1,rhyme_2, start_phone=(nphones_in_shortest -1)) == 1


                if they_rhyme:
                    found = True
                    #mark both words in rhyme pair with the same number 
                    delimnated_rhyme_1 = str(found_rhymes) + rhyme_1.replace("in'", "ing") + str(found_rhymes)
                    delimnated_rhyme_2 = str(found_rhymes) + rhyme_2.replace("in'", "ing") + str(found_rhymes)
                    rhyme_2_indicies = [i for i, x in enumerate(mark_copy) if x == rhyme_2]
                    for i in rhyme_2_indicies:
                        mark_copy[i] = delimnated_rhyme_2
                        colorlist[i] = found_rhymes

                    if mark_copy[idx] == rhyme_1:
                        mark_copy[idx] = delimnated_rhyme_1
                        colorlist[idx] = found_rhymes
        if found: 
            found_rhymes += 1

    for num in range(found_rhymes):
        indicies_of_rhymenum = [i for i, x in enumerate(colorlist) if num == x]
        if len(indicies_of_rhymenum) == 1: 
            # marking as 0 means no highlight 
            colorlist[indicies_of_rhymenum[0]] = 0
    return colorlist, mark_copy


def parse_lyrics(lyrics) -> list:
    words = []
    for word in lyrics.split():
        word.lower()
        words.append(word.strip(",?\".()—")) 
    return [words]

def analyze_lyrics(lyrics: list) -> list:
    rhyme_num_list = []
    marked_lyrics = []
    for section in lyrics:
        if section != [] and (section is not None):
            rhyme_numbers, marked = mark_with_rhymes(section)
            rhyme_num_list.append(rhyme_numbers)
            marked_lyrics.append(marked)
    return rhyme_num_list, marked_lyrics

def parse_and_analyze_lyrics(lyrics_files=None):
    for lyrics_file in lyrics_files:
        with open(lyrics_file, 'r') as file:
            lyrics = file.read()
            songlyrics = parse_lyrics(lyrics)
            rhyme_num, marked = analyze_lyrics(songlyrics)
            print(f"Results for {lyrics_file}:")
            print(rhyme_num)
            print(marked)


if __name__ == "__main__":
    lyrics_dir = "testfolder"
    lyrics_files = [os.path.join(lyrics_dir, file) for file in os.listdir(lyrics_dir) if file.endswith(".txt")]
    parse_and_analyze_lyrics(lyrics_files)