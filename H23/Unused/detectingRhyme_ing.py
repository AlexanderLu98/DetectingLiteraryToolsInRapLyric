import os 
import sys
from pprint import pprint as pp
from copy import deepcopy
import nltk
import logging
import json
import random


logging.basicConfig(level=logging.INFO)

#TODO: Look at checking by syllable, if its not possible 
# Then check last TWO phonemes for rhyme 
phone_dictionary = nltk.corpus.cmudict.dict()

def possible_phones(word):

    if word not in phone_dictionary:
        return []
    return phone_dictionary[word]


def phon_match(first_phon : list, second_phon : list,start : int, end: int,debug=False) -> int:
    logging.debug(f"FIRST: {first_phon} SECOND: {second_phon}")
    first_range = first_phon[start:end]
    second_range = second_phon[start:end]

    first_range = first_range[::-1]
    second_range = second_range[::-1]

    if debug:
        logging.debug(f"FIRST RANGE: {first_range}, SECOND RANGE: {second_range}")

    # we only want to loop through the smallest range
    if len(first_range) > len(second_range):
        first_range, second_range = second_range, first_range

    hits = 0
    total = len(first_range)
    #TODO: check if there is only one phoneneme in first_range, 
    # if so we can take out the loop here
    for idx, phone in enumerate(first_range):
        other_phone = second_range[idx]

        if phone == other_phone:
            hits += 1

            # Phones with emphasis are better matches, weight them more
            if phone[-1].isdigit():
                hits += 1
                total += 1

    return hits/total

def word_similarity(first_word, second_word, start_phone=None, end_phone=None,debug=False):
    # print(f"looking up Phonemes for {first_word} and {second_word}")
    first_word = first_word.strip(".!?-()").replace("in'", "ing")
    second_word = second_word.strip(".!?-()").replace("in'", "ing")
    
    first_phones = possible_phones(first_word)
    second_phones = possible_phones(second_word)
    logging.debug(f"SIMILARITY BETWEEN: {first_word} {first_phones} {second_word} {second_phones}")

    if not first_phones or not second_phones:
        return 0

    # If there is only one pronouciation of both words
    if len(first_phones) + len(second_phones) == 2:
        first_phones = first_phones[0]
        second_phones = second_phones[0] 
        return phon_match(first_phones, second_phones,start_phone,end_phone,debug=True)
    
    else:
    # multiple pronouciations for one or both words
    #we want to find if any pronouciations result in a rhyme
    # append all rhyme scores to list, if any of them > 0 its a rhyme
        scorelist = []
        for f_p in first_phones:
            for s_p in second_phones: 
                scorelist.append(phon_match(f_p,s_p,start_phone,end_phone,debug=True))
            
        if 1 in scorelist:
            return 1
        else: 
            return 0

def mark_with_rhymes(lyrics : str) -> str: 
    logging.debug(lyrics)
    mark_copy = deepcopy(lyrics)
    original_lyrics = lyrics.copy()  # Save a copy of the original lyrics

    found_rhymes = 0 
    prev_found = 0
    numremoved = 0
    colorlist = [-1] * len(mark_copy)
    rhymecolor = random.randint(0,0xFFFFFF)

    for idx, rhymer in enumerate(lyrics):
        if '[' in rhymer or ']' in rhymer:
            print(rhymer)
        found = False
        for rhymee in mark_copy[idx + 1:]:
            if rhymee in lyrics:
                they_rhyme = False
                rhymer_phon = possible_phones(rhymer.strip(".!?-()").replace("in'", "ing"))
                rhymee_phon = possible_phones(rhymee.strip(".!?-()").replace("in'", "ing"))

                if rhymer_phon == [] or rhymee_phon == []: 
                    they_rhyme = rhymer == rhymee
                    logging.debug(f"{rhymer} or {rhymee} was not found in CMUDict")
                else:
                    shortest_rhymer_phon = min(rhymer_phon, key=len)
                    shortest_rhymee_phon = min(rhymee_phon, key=len)
                    shortest_phon = min([shortest_rhymee_phon,shortest_rhymer_phon], key=len)

                    logging.debug(f"RHYMER: {rhymer} {rhymer_phon}, RHYMEE: {rhymee} {rhymee_phon}, SHORTEST: {shortest_phon}")
                    logging.debug(f"{len(shortest_phon)} phonemes in {shortest_phon}")
                    nphones_in_shortest = 0 if (len(shortest_phon) - 1) == 0 else len(shortest_phon) - 1
                    they_rhyme = word_similarity(rhymer,rhymee, start_phone=(nphones_in_shortest -1), debug=True) == 1

                if they_rhyme:
                    found = True
                    delimnated_rhymer = str(found_rhymes) + rhymer.replace("in'", "ING") + str(found_rhymes)
                    delimnated_rhymee = str(found_rhymes) + rhymee.replace("in'", "ING") + str(found_rhymes)
                    rhymee_indicies = [i for i, x in enumerate(mark_copy) if x == rhymee]
                    logging.debug(f"matching {rhymer}, {rhymee} is in {rhymee_indicies}")
                    for i in rhymee_indicies:
                        mark_copy[i] = delimnated_rhymee
                        colorlist[i] = found_rhymes

                    if mark_copy[idx] == rhymer:
                        mark_copy[idx] = delimnated_rhymer
                        colorlist[idx] = found_rhymes
                    else:
                        logging.debug(f"{rhymer, idx} alerady marked by another rhyme, rhymee: {rhymee}")
                        logging.debug(f"{rhymee_indicies}   indicies")

                    logging.debug(f"word {delimnated_rhymer} rhymes with {delimnated_rhymee}")

        if found: 
            found_rhymes += 1
            rhymecolor = random.randint(0,0xFFFFFF)

    for num in range(found_rhymes):
        indicies_of_rhymenum = [i for i, x in enumerate(colorlist) if num == x]
        if len(indicies_of_rhymenum) == 1: 
            colorlist[indicies_of_rhymenum[0]] = 0

    # Replace the modified words with the original words
    for i, word in enumerate(mark_copy):
        if "ING" in word:
            # Extract the rhyme numbers from the word
            start_num = word.find(str(colorlist[i])) + len(str(colorlist[i]))
            end_num = word.rfind(str(colorlist[i]))
            # Replace the modified part of the word with the original part
            mark_copy[i] = word[:start_num] + original_lyrics[i][start_num:end_num] + word[end_num:]

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
            logging.debug(f"RhymeNumbers: {len(rhyme_numbers)}MARKED {len(section)} ")
            rhyme_num_list.append(rhyme_numbers)
            marked_lyrics.append(marked)
            if showResult:
                logging.debug(marked)
        else:
            logging.debug("Found an empty section")
    logging.debug(rhyme_num_list)

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