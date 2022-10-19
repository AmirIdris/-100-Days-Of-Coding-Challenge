import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

# create dictionary from the csv file
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
word = input("Enter Your Name:").upper()
passing = 0
while passing == 0:
    try:
        new_list = [new_dict[letter] for letter in word]
    except:
        print("Sorry only letters in the alphabet")
        word = input("Enter Your Name:").upper()
    else:
        print(new_list)
        passing = 1



