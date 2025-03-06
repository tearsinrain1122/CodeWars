# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched

# Solution

def pig_it(text):
    text = text.split()
    pig_latin = []
    for word in text:
        if word not in [".", ",", "!", "-", "?"]:
            pig_latin.append(word[1:]+word[0]+"ay")
        else:
            pig_latin.append(word)
    return " ".join(pig_latin)
