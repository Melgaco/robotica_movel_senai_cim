print('''
6-Is a Number Prime? (28 Lines) A prime number is an integer greater than 1 that is only divisible by one and itself. 
Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise.
Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime. 
Ensure that the main program will not run if the file containing your solution is imported into another program''')
print('###############################################################################')
print('\n'*3)

minhaStr = input("Escreva a sua string: ")

meuNumber = int(minhaStr)

count = 1
success = 0

while count <= meuNumber/2:
    res = meuNumber/count
    if(meuNumber%count == 0):
        success += 1
        if(success > 1):
            print(f'{res}')
            print('Fail')
            pass
    count+=1

