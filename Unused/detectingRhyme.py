import os 
from copy import deepcopy
import nltk

phone_dictionary = nltk.corpus.cmudict.dict()

def possible_phones(word):
    if word not in phone_dictionary:
        return []
    return phone_dictionary[word]

def phon_match(first_phon : list, second_phon : list,start : int, end: int,debug=False) -> int:
    first_range = first_phon[start:end]
    second_range = second_phon[start:end]

    first_range = first_range[::-1]
    second_range = second_range[::-1]

    hits = 0
    total = len(first_range)

    for idx, phone in enumerate(first_range):
        if idx < len(second_range):  # Ensure idx is within range of second_range
            other_phone = second_range[idx]

            # Break down the phonemes into sub-phonemes
            phone_parts = list(phone)
            other_phone_parts = list(other_phone)

            # Compare the sub-phonemes
            for part, other_part in zip(phone_parts, other_phone_parts):
                if part == other_part:
                    hits += 1

                    # Phones with emphasis are better matches, weight them more
                    if part.isdigit():
                        hits += 1
                        total += 1

    return hits/total


def word_similarity(first_word, second_word, start_phone=None, end_phone=None,debug=False):
    first_word = first_word.strip(".!?-()").replace("in'", "ing")
    second_word = second_word.strip(".!?-()").replace("in'", "ing")
    first_phones = possible_phones(first_word)
    second_phones = possible_phones(second_word)
    if not first_phones or not second_phones:
        return 0

    if len(first_phones) + len(second_phones) == 2:
        first_phones = first_phones[0]
        second_phones = second_phones[0] 
        return phon_match(first_phones, second_phones,start_phone,end_phone,debug=True)
    else:
        scorelist = []
        for f_p in first_phones:
            for s_p in second_phones: 
                scorelist.append(phon_match(f_p,s_p,start_phone,end_phone,debug=True))
            
        if 1 in scorelist:
            return 1
        else: 
            return 0

def mark_with_rhymes(lyrics : str) -> str: 
    """
    marks the lyrics with delims around words based on rhymes 
    """
    mark_copy = deepcopy(lyrics)

    found_rhymes = 0 
    colorlist = [-1] * len(mark_copy)

    for idx, rhymer in enumerate(lyrics):
        if '[' in rhymer or ']' in rhymer:
            print(rhymer)
        found = False
        for rhymee in mark_copy[idx + 1:]:
            if rhymee in lyrics:
                they_rhyme = False
                # we are concerned with end rhymes for now, only want to check if the last phoneme in the word matches
                # so start at the last phoneme of the shortest word (length of shortest - 1 OR 1 if its a 1 phoneme word)
                rhymer_phon = possible_phones(rhymer.strip(".!?-()").replace("in'", "ing"))
                rhymee_phon = possible_phones(rhymee.strip(".!?-()").replace("in'", "ing"))

                # if one of the words are not, the best we can do is check for exact equaliy (for now)
                if rhymer_phon == [] or rhymee_phon == []: 
                    they_rhyme = rhymer == rhymee
                else:
                    #shortest pronounciation of each word 
                    shortest_rhymer_phon = min(rhymer_phon, key=len)
                    shortest_rhymee_phon = min(rhymee_phon, key=len)
                    shortest_phon = min([shortest_rhymee_phon,shortest_rhymer_phon], key=len)
                    nphones_in_shortest = 0 if (len(shortest_phon) - 1) == 0 else len(shortest_phon) - 1
                    they_rhyme = word_similarity(rhymer,rhymee, start_phone=(nphones_in_shortest -1), debug=True) == 1


                if they_rhyme:
                    found = True
                    #print(f"{rhymer} rhymes with {rhymee}")
                    #rhyme is between WORD in splitlyrics (original) and some other word (rhymee) in the iter_copy
                    #mark both words in rhyme pair with the same number 
                    delimnated_rhymer = str(found_rhymes) + rhymer.replace("in'", "ING") + str(found_rhymes)
                    delimnated_rhymee = str(found_rhymes) + rhymee.replace("in'", "ING") + str(found_rhymes)
                    # replace ALL INSTANCES of the rhymee with a delimnated version of it
                    rhymee_indicies = [i for i, x in enumerate(mark_copy) if x == rhymee]
                    for i in rhymee_indicies:
                        mark_copy[i] = delimnated_rhymee
                        colorlist[i] = found_rhymes

                    if mark_copy[idx] == rhymer:
                        mark_copy[idx] = delimnated_rhymer
                        colorlist[idx] = found_rhymes

        if found: 
            # this word did not rhyme and has not been delimnated / appended
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
        words.append(word.strip(",?\".()—")) 
    return [words]

def analyze_lyrics(lyrics: list,showResult=False) -> list:
    """
    Takes in lyrics, and analyzes them for rhymes, returning a list[list] of Rhyme Numbers by section
    lyrics: [[list of words in section] for each section]
    ShowResult: whether or not to print results for that song to the console, used for -t flag 
    returns:
    rhyme_numbers: [[list of rhyme numbers] for each section]
    rhyme_numbers and lyrics are one-to-one
    marked_lyrics: A String of lyrics where rhyming words are delimnated by their rhyme number
    used for debugging and development
    """
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