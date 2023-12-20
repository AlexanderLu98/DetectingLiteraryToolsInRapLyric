# DetectingLiteraryToolsInRapLyric

TODO: FIX AND FORMAT THIS README. ALSO FIX NAMING CONVENTION

# Folders

Sorry for a pretty chaotic project but I have created 4 folders to systematically put different scripts and files in their respective places.

"Unused" is the folder for unused scripts or scripts and files that were used in the early stages of the project

"Lyrics" is a folder full of lyrics in different file format. It is subdivided into folder that only makes sense to me... The two folder of notability is the "csv" folder containing an early iteration of the project and a proposed structure for the dataset. This is not used, but might be promising in the future. The "main" contains the list of songlyrics that were used in the final implementation and can be used for future expansions

"Helper Script" contains all the pythons script that is not necessary for the process, but that I used in different stages to make it easier for myself

"final results" contains the excel files that I have manually gone through to compare with the actuall rhyme highlighted text.

# Python programs
"automaticDatasetCreator.py" is the program that creates the dataset seen in the "lyrics/csv" folder and was the primary python file in the early iteration

"datasetCreator.py" is the predecessor to "automaticDatasetCreator". This was mainly used to figure out how the dataset should look like before implementing it on a larger scale.

"detectingRhyme.py" is the main program of the whole project. This is the logic behind the whole project

"documentCreator.py" would take the output from "detectingRhyme.py" as its input and in turn create a document with highlighted words. NOT OPTIMAL AND PRONE TO BUGS

"excelCreator.py" would take the output from "detectingRhyme.py" as its input and turn it into excel files so I could easily edit the output manually

"lyricRetriever.py" connects to Genius API and retrives the lyrics based on a list

"syllable.py" is a WIP and took words and deconstructed it into its respective syllables. Wished I made this earlier... It might be considered cheating but it is a web scraping tool that connects to https://www.howmanysyllables.com