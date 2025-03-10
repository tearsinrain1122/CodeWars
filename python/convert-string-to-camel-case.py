# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, 
# also often referred to as Pascal case). The next words should be always capitalized.

# Solution

def to_camel_case(text):
    new_text = text.replace("-", "_")
    list_text = new_text.split("_")
    for i in range (1,len(list_text)):
        list_text[i] = list_text[i].capitalize()
    return "".join(list_text)
