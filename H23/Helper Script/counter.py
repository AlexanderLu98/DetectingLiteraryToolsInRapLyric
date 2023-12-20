import os

def count_txt_files(directory):
    return len([f for f in os.listdir(directory) if f.endswith('.txt')])

directory = 'lyrics/txt original'  # replace with your directory
directory1 = 'lyrics/first iter txt'
directory2 = 'lyrics/second iter txt'
directory3 = 'lyrics/final preproccess txt/first group'
directory4 = 'lyrics/final preproccess txt/second group'


print("list of 462 songs, retrived them from azlyrics and cleaned them afterwards. not every song existed or where mislabeld so I ended up with")
print(f'The number of txt files in the txt orinal is: {count_txt_files(directory)}')
print("after further cleaning I removed more due to them been incrrect")
print(f'The number of txt files in the first iter is: {count_txt_files(directory1)}')
print("removed files that were either to small or too big. only txt files between 1-2 kb")
print(f'The number of txt files in the second iter is: {count_txt_files(directory2)}')
print(f'The number of txt files in the first group is: {count_txt_files(directory3)}')
print("Also created a folder of the csv file")
print(f'The number of txt files in the second group is: {count_txt_files(directory4)}')
print("not wokring, divided the first group into two and rearranged them a little bit")
print("created a new folder of 25 excel files. I manually compared 10 of them to the real resilt")
