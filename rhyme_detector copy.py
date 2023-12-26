# Rhyme TODOS:

# Perfect/Imperfect rhymes (1 to 1)
    # Perfect rhymes => identical after the stressed syllable. rime is the same (nucleus + coda is the same while onset is different)
    # Imperfect rhymes => needs better definition

# Assonance and Consonance (Many to Many)
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

# Define a constant for vowels at the top of the file
VOWELS = ['AA', 'AE', 'AH', 'AO', 'AW', 'AX', 'AXR', 'AY', 'EH', 'ER', 'EY', 'IH', 'IX', 'IY', 'OW', 'OY', 'UH', 'UW', 'UX']

def split_into_syllables(word):
   """Split a word into syllables."""
   return word.split('-')

def find_stressed_syllable(syllables, vowels):
   """Find the stressed syllable in a list of syllables."""
   for syllable in reversed(syllables):
       if any(vowel in syllable for vowel in vowels):
           return syllable
   return None

def get_rhyme_part(word, vowels):
   """Return the rime part of a word."""
   syllables = split_into_syllables(word)
   if len(syllables) == 1:
       return word
   stressed_syllable = find_stressed_syllable(syllables, vowels)
   if stressed_syllable:
       stressed_index = syllables.index(stressed_syllable)
       return '-'.join(syllables[stressed_index:])
   return ""

def are_perfect_rhymes(word1, word2, vowels):
   """Check if two words have perfect rhymes."""
   rhyme_part1 = get_rhyme_part(word1, vowels)
   rhyme_part2 = get_rhyme_part(word2, vowels)
   return rhyme_part1 == rhyme_part2

# Tests
print("Print iteration 1")
result = are_perfect_rhymes("AXˈB-IH-L.AX.T-IY", "ˈEY.B-AX-L", VOWELS)
print(f"Test 'AXˈB-IH-L.AX.T-IY' and 'ˈEY.B-AX-L': {result} (Expected: False)")
assert result == False

result = are_perfect_rhymes("AXˈB-IH-L.AX.T-IY", "AXˈB-IH-L.AX.T-IY", VOWELS)
print(f"Test 'AXˈB-IH-L.AX.T-IY' and 'AXˈB-IH-L.AX.T-IY': {result} (Expected: True)")
assert result == True

# Test iteration 2
print("Print iteration 2")
result = are_perfect_rhymes("G-AE-NG", "S-L-AE-NG", VOWELS)
print(f"Test 'G-AE-NG' and 'S-L-AE-NG': {result} (Expected: True)")
assert result == True

result = are_perfect_rhymes("ˈHH-AY.L-AY-T", "ˈS-K-AY.L-AY-T", VOWELS)
print(f"Test 'ˈHH-AY.L-AY-T' and 'ˈS-K-AY.L-AY-T': {result} (Expected: True)")
assert result == True


# Test iteration 3
print("Print iteration 3")
result = are_perfect_rhymes("B-AE-T", "K-AE-T", VOWELS)
print(f"Test 'B-AE-T' and 'K-AE-T': {result} (Expected: True)")
assert result == True

result = are_perfect_rhymes("S-N-EY-K", "B-R-EY-K", VOWELS)
print(f"Test 'S-N-EY-K' and 'B-R-EY-K': {result} (Expected: True)")
assert result == True

result = are_perfect_rhymes("ˈF-L-AW.ER", "ˈP-AW.ER", VOWELS)
print(f"Test 'ˈF-L-AW.ER' and 'ˈP-AW.ER': {result} (Expected: True)")
assert result == True

# Test iteration 4
print("Print iteration 4")
result = are_perfect_rhymes("B-AE-T", "B-EH-T", VOWELS)
print(f"Test 'B-AE-T' and 'B-EH-T': {result} (Expected: False)")
assert result == False

result = are_perfect_rhymes("S-N-EY-K", "S-N-EH-K", VOWELS)
print(f"Test 'S-N-EY-K' and 'S-N-EH-K': {result} (Expected: False)")
assert result == False

print("All tests passed!")
