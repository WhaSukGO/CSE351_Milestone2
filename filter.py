import pandas as pd
import os.path
from os import path

df = pd.read_csv('original_trainLabels.csv')

"""""
    1. Ramnit
    2. Lollipop
    3. Kelihos_ver3
    4. Vundo
    5. Simda
    6. Tracur
    7. Kelihos_ver1
    8. Obfuscator.ACY
    9. Gatak
"""""

# Create an empty dataframe for keeping training data
trainLabels = pd.DataFrame(None, columns=['Id', 'Class'])

# Filter rows with specific classes.
dfs = [df.loc[df['Class'] == x] for x in range(1, 10)]

for d in dfs:

    # For each class, 20 files are needed.
    count = 0

    # Check if that file actually exists
    # (Have noticed that there are missing files. I mean a lot...)
    for index, row in d.iterrows():

        # If the file exists, add it to the list
        if path.exists("train_full/{}.asm".format(row['Id'])):
            trainLabels = trainLabels.append(row, ignore_index=True)
            count += 1

            if count == 20:
                break

        else:
            print('NOPE')

# Save it! Yeah!
trainLabels.to_csv('trainLabels.csv', index=False)
