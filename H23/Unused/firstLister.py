import os

def list_txt_files(directory):
    txt_files = [(f, os.path.getsize(os.path.join(directory, f))) for f in os.listdir(directory) if f.endswith('.txt')]
    count = len(txt_files)
    return txt_files, count

def group_files_by_size(txt_files):
    size_groups = {'<1KB': [], '1KB-2KB': [], '2KB-3KB': [], '3KB-4KB': [], '4KB-5KB': [], '5KB-6KB': [], '6KB-7KB': [], '>7KB': []}
    for file, size in txt_files:
        if size < 1024:  # less than 1KB
            size_groups['<1KB'].append(file)
        elif size < 2048:  # between 1KB and 2KB
            size_groups['1KB-2KB'].append(file)
        elif size < 3072:  # between 2KB and 3KB
            size_groups['2KB-3KB'].append(file)
        elif size < 4096:  # between 3KB and 4KB
            size_groups['3KB-4KB'].append(file)
        elif size < 5120:  # between 4KB and 5KB
            size_groups['4KB-5KB'].append(file)
        elif size < 6144:  # between 5KB and 6KB
            size_groups['5KB-6KB'].append(file)
        elif size < 7168:  # between 6KB and 7KB
            size_groups['6KB-7KB'].append(file)
        else:  # greater than 7KB
            size_groups['>7KB'].append(file)
    return size_groups

directory = 'lyrics/first iter txt'  # lyrics/txt original
txt_files, count = list_txt_files(directory)

# for file, size in txt_files:
#     print(f'{file} - {size} bytes')
# print(f'There are {count} txt files in the directory.')

# size_groups = group_files_by_size(txt_files)
# for group, files in size_groups.items():
#     print(f'There are {len(files)} txt files in the {group} size group.')

# # Write the titles of the txt files in the '1KB-2KB' size group to a new txt file
# with open('1-2KB songs.txt', 'w') as f:
#     for file in size_groups['1KB-2KB']:
#         f.write(file + '\n')
