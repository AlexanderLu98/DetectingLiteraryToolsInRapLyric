# Create a dictionary to map IPA symbols to ARPABET symbols
ipa_to_arpabet_dict = {
    'ɑ': 'AA',
    'ɒ': 'AA',
    'æ': 'AE',
    'ʌ': 'AH',
    'ɔ': 'AO',
    'aʊ': 'AW',
    'ə': 'AX',
    'ɚ': 'AXR',
    'aɪ': 'AY',
    'ɛ': 'EH',
    'e': 'EH',
    'ɝ': 'ER',
    'eɪ': 'EY',
    'ɪ': 'IH',
    'ɨ': 'IX',
    'i': 'IY',
    'oʊ': 'OW',
    'ɔɪ': 'OY',
    'ʊ': 'UH',
    'u': 'UW',
    'ʉ': 'UX',
    'b': 'B',
    'tʃ': 'CH',
    'd': 'D',
    'ð': 'DH',
    'ɾ': 'DX',
    'l̩': 'EL',
    'm̩': 'EM',
    'n̩': 'EN',
    'f': 'F',
    'ɡ': 'G',
    'h': 'HH',
    'dʒ': 'JH',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'ŋ': 'NG',
    'ɾ̃': 'NX',
    'p': 'P',
    'ʔ': 'Q',
    'ɹ': 'R',
    'r': 'R',
    's': 'S',
    'ʃ': 'SH',
    't': 'T',
    'θ': 'TH',
    'v': 'V',
    'w': 'W',
    'ʍ': 'WH',
    'j': 'Y',
    'z': 'Z',
    'ʒ': 'ZH'
}

def ipa_to_arpabet(ipa_string):
    arpabet_string = ''
    i = 0
    while i < len(ipa_string):
        if i < len(ipa_string) - 1 and ipa_string[i:i+2] in ipa_to_arpabet_dict:
            arpabet_string += ipa_to_arpabet_dict[ipa_string[i:i+2]]
            i += 2
        elif ipa_string[i] in ipa_to_arpabet_dict:
            arpabet_string += ipa_to_arpabet_dict[ipa_string[i]]
            i += 1
        else:
            arpabet_string += ipa_string[i]  # If the character is not in the dictionary, keep it as is
            i += 1
    return arpabet_string

def process_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            word, ipa = line.strip().split(':')  # Split the line into word and IPA
            ipa = ipa.strip(' /')  # Remove the slashes and spaces around the IPA
            arpabet = ipa_to_arpabet(ipa)
            f_out.write(f'{word}: {arpabet}\n')

# Example usage:
process_words("pronunciations1000.txt", "arpabet_pronunciations.txt")
