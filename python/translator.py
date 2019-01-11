'''
tag language
vowel -> n
 e.g. dog -> dng
        cat -> cnt
'''

def translate(phrase):
    translation = ""
    for letter in phrase:
        if  letter.lower() in "aeiou":     # .lower turns all letters to lower case and checks but letter remains unchanged
            if letter.isupper():
                translation += "X"
            else:
                translation += "x"
        else:
            translation += letter
    return translation

word = input("Enter phrase to be translated: ")
print(translate(word))