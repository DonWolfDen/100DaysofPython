import pandas

nato_dict = {row.letter:row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
def generate():
    word = input("Enter a word: ").upper()
    try:
        letters = [nato_dict[letter] for letter in word]
    except KeyError:
        print("English letters only please")
        generate()
    else:
        print(letters)

generate()