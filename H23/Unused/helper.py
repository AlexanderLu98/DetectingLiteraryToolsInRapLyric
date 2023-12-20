def convert_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return words

# Usage:
print(convert_text('testfolder\Big L - The Enemy.txt'))
