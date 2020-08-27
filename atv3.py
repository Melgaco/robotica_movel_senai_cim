print('''
3-Center a String in the Terminal
(31 Lines)
Write a function that takes a string of characters as its first parameter, and the width of the terminal in
characters as its second parameter. Your function should return a new string that consists of the original
string and the correct number of leading spaces so that the original string will appear centered within the
provided width when it is printed. Do not add any characters to the end of the string. Include a main program
that demonstrates your function.''')
print('###############################################################################')

#print('MyString')

import os
rows, columns = os.popen('stty size', 'r').read().split()

print(f"Linhas: {rows}")
print(f"Colunas: {columns}")

minhaStr = input("Escreva a sua string: ")

splitIni = round((int(columns)-len(minhaStr))/2)

print(' '*splitIni + str(minhaStr))


