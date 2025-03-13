from preloaded import MORSE_CODE

# In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, 
# it still has its use in some applications around the world. The Morse code encodes every character as a sequence of "dots" and "dashes". For example, 
# the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital 
# letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. 
# For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

# Solution

def decode_morse(morse_code):
    letters = morse_code.split(" ")
    decoded = ""
    for letter in letters:
        if letter == "":
            decoded+= " "
        else:
            decoded+= MORSE_CODE[letter]
    return decoded.replace("  ", " ").strip()
