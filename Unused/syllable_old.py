import cmudict

def lookup_word(word_s):
    return cmudict.dict().get(word_s)

def get_syllables(word_s):
    phones = lookup_word(word_s)  # this returns a list of matching phonetic rep's
    syllables = []
    if phones:  # if the list isn't empty (the word was found)
        phones0 = phones[0]  # process the first
        syllable = []
        for p in phones0:
            if p[-1].isdigit():  # if it's a vowel sound
                syllable.append(p[:-1])  # add the phoneme without stress marker to the syllable
                syllables.append(syllable)  # add the syllable to the list of syllables
                syllable = []  # start a new syllable
            else:
                syllable.append(p)  # add the phoneme to the syllable
    return syllables

word_s = 'tester'
syllables = get_syllables(word_s)
print(f"SYLLABLES ({word_s!r}) yields {syllables}")
