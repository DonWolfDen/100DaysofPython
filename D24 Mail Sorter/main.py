with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt")as letter:
    letter_list = letter.read()
    for i in range(len(names_list)):
        stripped_name = names_list[i].strip("\n")
        new_letter = letter_list.replace("[name]", f"{stripped_name}")
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", "w") as file:
            file.write(new_letter)


#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp