student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data = pandas.DataFrame(data)

dic = {row.letter: row.code for (index, row) in data.iterrows()}
print(dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("¿What's is the name?").upper()

output_list = [dic[letter] for letter in name if letter in dic.keys()]
print(output_list)
