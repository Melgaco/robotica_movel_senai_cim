print('''
3-Capitalize it
(48 Lines)
Many people do not use capital letters correctly, especially when typing on small devices like smart phones.
In this exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase
“i” should be replaced with an uppercase “I” if it is both preceded and followed by a space. The first
character in the string should also be capitalized, as well as the first non-space character after a “.”, “!” or
“?”. For example, if the function is provided with the string “what time do i have to be there? what’s the
address?” then it should return the string “What time do I have to be there? What’s the address?”. Include a
main program that reads a string from the user, capitalizes it using your function, and displays the result.''')
print('###############################################################################')
print('\n'*3)

minhaStr = input("Escreva a sua string: ")

inter = '?'
excl = '!'
point = '.'
nextCapitalize = False

Capitalized = ''
first = True

for letter in minhaStr:
    if first:
        myLet = letter.upper()
        Capitalized += myLet
        first = False
        continue

    if(letter == ' '):
        Capitalized += ' '
        continue
    if(letter == inter or letter == excl or letter == point):
        nextCapitalize = True
        Capitalized += letter
        continue

    if(nextCapitalize):
        myLet = letter.upper()
        Capitalized += myLet
    else:
        myLet = letter.lower()
        Capitalized += myLet
    
    nextCapitalize = False

print(f"{Capitalized}")
#what time do i have to be there? what’s the address?
#What time do I have to be there? What’s the address?