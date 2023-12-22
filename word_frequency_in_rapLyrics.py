import os
import collections
import csv

def count_words_in_dir(dir_path):
    word_counter = collections.Counter()

    for filename in os.listdir(dir_path):
        if filename.endswith('.txt'):
            with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for ch in ['.','!', '"', '(', ')', ',', '?']:
                    if ch in text:
                        text = text.replace(ch, '')
                text = text.replace('�', "'")
                words = text.split()
                word_counter.update(words)

    with open('word_frequencies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        for word, count in word_counter.most_common():
            writer.writerow([word, count])

# Replace 'your_directory_path' with the path to the directory you want to analyze
count_words_in_dir('rap lyrics')
