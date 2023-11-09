import pandas as pd

fileName ='lyrics\csv\Big L - The Enemy.csv'
# Load the CSV file
df = pd.read_csv(fileName)

# Ask the user for the starting line
start_line = int(input('Enter the starting line number: '))

for i in range(start_line - 1, len(df)):
    # Print the current line
    print(df.iloc[i])

    # Ask the user if they want to edit the line
    edit = input('Do you want to edit this line? (y/n): ')
    if edit.lower() == 'y':
        # Ask the user for the new values
        rhyme_group = input('Enter the new value for RhymeGroup: ')
        is_rhyme = input('Enter the new value for IsRhyme (t/f): ')

        # Validate the IsRhyme input
        while is_rhyme not in ['t', 'f']:
            print('Invalid input. Please enter t or f.')
            is_rhyme = input('Enter the new value for IsRhyme (t/f): ')

        # Update the DataFrame
        df.loc[i, 'RhymeGroup'] = int(rhyme_group)
        df.loc[i, 'IsRhyme'] = True if is_rhyme == 't' else False
    elif edit.lower() == 'end':
        break

# Ask the user if they want to save the changes
save = input('Do you want to save the changes? (y/n): ')
if save.lower() == 'y':
    # Save the edited DataFrame back to a CSV file
    df.to_csv(fileName, index=False)
