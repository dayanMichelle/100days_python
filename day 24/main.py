PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()  # creating a names array 

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()  # lee la carta
    for name in names:
        stripped_name = name.strip()  # deleted each \n in the names
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
