from nltk.metrics.distance import edit_distance

def get_rhyme(word, syllables=2):
    phonemes = d[word.lower()][0]
    return phonemes[-syllables:]

def is_rhyme(word1, word2, max_distance=2):
    rhyme1 = get_rhyme(word1)
    rhyme2 = get_rhyme(word2)
    distance = edit_distance(rhyme1, rhyme2)
    return distance <= max_distance

def rhyme_scheme(poem):
    lines = poem.split("\n")
    end_words = [line.split()[-1] for line in lines]
    
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    scheme = ""
    mapping = {}
    
    for i in range(len(end_words)):
        word = end_words[i]
        if word not in mapping:
            for j in range(i):
                if is_rhyme(word, end_words[j]):
                    mapping[word] = mapping[end_words[j]]
                    break
            if word not in mapping:
                mapping[word] = letters[0]
                letters = letters[1:]
        scheme += mapping[word]
        
    return scheme