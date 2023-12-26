# Rhyme TODOS:

# Perfect/Imperfect rhymes
    # Perfect rhymes => identical after the stressed syllable. rime is the same (nucleus + coda is the same while onset is different)
    # Imperfect rhymes => needs better definition

# Assonance and Consonance
    # Vowel Assonance
    # Consonant Assonance (Consonance)

# Posistioning
    # End rhyme
    # Identical rhyme
    # Alliteration

# Manipulation of sound
    # Forced rhyme

# Nah
    # Eye rhyme, Mind rhyme, Identical rhyme

def get_rhyme_part(word, vowels):
    # Split the word into syllables
    syllables = word.split('-')
    
    # If the word is monosyllabic, return the word
    if len(syllables) == 1:
        return word
    
    for i in reversed(range(len(syllables))):
        # Find the stressed syllable
        if any(vowel in syllables[i] for vowel in vowels):
            # Return the rime (the part from the vowel onwards) and all following syllables
            return '-'.join(syllables[i:])
    
    return ""

def are_perfect_rhymes(word1, word2, vowels):
    # Get the rhyme parts of the words
    rhyme_part1 = get_rhyme_part(word1, vowels)
    rhyme_part2 = get_rhyme_part(word2, vowels)
    
    # Check if the rhyme parts are the same
    return rhyme_part1 == rhyme_part2

# Hardcoded vowels
vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AX', 'AXR', 'AY', 'EH', 'ER', 'EY', 'IH', 'IX', 'IY', 'OW', 'OY', 'UH', 'UW', 'UX']


#Todo: move test to own folder

# Test iteration 1
print("Print iteration 1")
result = are_perfect_rhymes("AXˈB-IH-L.AX.T-IY", "ˈEY.B-AX-L", vowels)
print(f"Test 'AXˈB-IH-L.AX.T-IY' and 'ˈEY.B-AX-L': {result} (Expected: False)")
assert result == False

result = are_perfect_rhymes("AXˈB-IH-L.AX.T-IY", "AXˈB-IH-L.AX.T-IY", vowels)
print(f"Test 'AXˈB-IH-L.AX.T-IY' and 'AXˈB-IH-L.AX.T-IY': {result} (Expected: True)")
assert result == True

# Test iteration 2
print("Print iteration 2")
result = are_perfect_rhymes("G-AE-NG", "S-L-AE-NG", vowels)
print(f"Test 'G-AE-NG' and 'S-L-AE-NG': {result} (Expected: True)")
assert result == True

result = are_perfect_rhymes("ˈHH-AY.L-AY-T", "ˈS-K-AY.L-AY-T", vowels)
print(f"Test 'ˈHH-AY.L-AY-T' and 'ˈS-K-AY.L-AY-T': {result} (Expected: True)")
assert result == True


# Test iteration 3
print("Print iteration 3")
result = are_perfect_rhymes("B-AE-T", "K-AE-T", vowels)
print(f"Test 'B-AE-T' and 'K-AE-T': {result} (Expected: True)")
assert result == True

result = are_perfect_rhymes("S-N-EY-K", "B-R-EY-K", vowels)
print(f"Test 'S-N-EY-K' and 'B-R-EY-K': {result} (Expected: True)")
assert result == True

result = are_perfect_rhymes("ˈF-L-AW.ER", "ˈP-AW.ER", vowels)
print(f"Test 'ˈF-L-AW.ER' and 'ˈP-AW.ER': {result} (Expected: True)")
assert result == True

# Test iteration 4
print("Print iteration 4")
result = are_perfect_rhymes("B-AE-T", "B-EH-T", vowels)
print(f"Test 'B-AE-T' and 'B-EH-T': {result} (Expected: False)")
assert result == False

result = are_perfect_rhymes("S-N-EY-K", "S-N-EH-K", vowels)
print(f"Test 'S-N-EY-K' and 'S-N-EH-K': {result} (Expected: False)")
assert result == False

print("All tests passed!")
