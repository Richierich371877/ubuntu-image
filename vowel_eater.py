# vowel eater /removes vowels
user_word = input("Please Enter a word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        print(letter)