import os

# Specify the directory you want to start from
rootDir = 'lyrics/second iter txt'  # current directory
specific_file = '1-2KB songs.txt'  # the specific text file

# Read the specific file and get the list of files to keep
with open(specific_file, 'r') as f:
    files_to_keep = f.read().splitlines()

# Walk through the directory
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        # If the file is a text file and not in the list of files to keep
        if fname.endswith('.txt') and fname not in files_to_keep:
            file_path = os.path.join(dirName, fname)
            os.remove(file_path)  # remove the file
            print(f'Removed file: {file_path}')
