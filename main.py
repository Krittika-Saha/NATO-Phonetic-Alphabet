import pandas as pds

data1 = pds.read_csv('nato_phonetic_alphabet.csv')
code_dictionary = {data1['letter'][i]:data1['code'][i] for i in range(0, 26)}
name_input = list(input("Enter a name: ").upper())
for i in name_input:
    print(f"{i} is for {code_dictionary[i]}")
