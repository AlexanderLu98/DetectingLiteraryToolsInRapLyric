import os

def list_txt_files(directory):
    txt_files = [(f, os.path.getsize(os.path.join(directory, f))) for f in os.listdir(directory) if f.endswith('.txt')]
    count = len(txt_files)
    return txt_files, count

def group_files_by_size(txt_files):
    size_groups = {'1KB-1.1KB': [], '1.1KB-1.2KB': [], '1.2KB-1.3KB': [], '1.3KB-1.4KB': [], '1.4KB-1.5KB': [], '1.5KB-1.6KB': [], '1.6KB-1.7KB': [], '1.7KB-1.8KB': [], '1.8KB-1.9KB': [], '1.9KB-2KB': []}
    for file, size in txt_files:
        if 1024 <= size < 1126:  # between 1KB and 1.1KB
            size_groups['1KB-1.1KB'].append(file)
        elif 1126 <= size < 1229:  # between 1.1KB and 1.2KB
            size_groups['1.1KB-1.2KB'].append(file)
        elif 1229 <= size < 1331:  # between 1.2KB and 1.3KB
            size_groups['1.2KB-1.3KB'].append(file)
        elif 1331 <= size < 1434:  # between 1.3KB and 1.4KB
            size_groups['1.3KB-1.4KB'].append(file)
        elif 1434 <= size < 1536:  # between 1.4KB and 1.5KB
            size_groups['1.4KB-1.5KB'].append(file)
        elif 1536 <= size < 1638:  # between 1.5KB and 1.6KB
            size_groups['1.5KB-1.6KB'].append(file)
        elif 1638 <= size < 1741:  # between 1.6KB and 1.7KB
            size_groups['1.6KB-1.7KB'].append(file)
        elif 1741 <= size < 1843:  # between 1.7KB and 1.8KB
            size_groups['1.7KB-1.8KB'].append(file)
        elif 1843 <= size < 1946:  # between 1.8KB and 1.9KB
            size_groups['1.8KB-1.9KB'].append(file)
        elif 1946 <= size < 2048:  # between 1.9KB and 2KB
            size_groups['1.9KB-2KB'].append(file)
    return size_groups



directory = 'lyrics/second iter txt'  # lyrics/txt original
txt_files, count = list_txt_files(directory)

for file, size in txt_files:
    print(f'{file} - {size} bytes')
print(f'There are {count} txt files in the directory.')

size_groups = group_files_by_size(txt_files)
for group, files in size_groups.items():
    print(f'There are {len(files)} txt files in the {group} size group.')

# # Write the titles of the txt files in the '1KB-2KB' size group to a new txt file
# with open('1-2KB songs.txt', 'w') as f:
#     for file in size_groups['1KB-2KB']:
#         f.write(file + '\n')
