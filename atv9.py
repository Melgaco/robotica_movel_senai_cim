# 9-Arbitrary Base Conversions
# (61 Lines)
# Write a program that allows the user to convert a number from one base to another. Your program should
# support bases between 2 and 16 for both the input number and the result number. If the user chooses a base
# outside of this range then an appropriate error message should be displayed and the program should exit.
# Divide your program into several functions, including a function that converts from an arbitrary base to base
# 10, a function that converts from base 10 to an arbitrary base, and a main program that reads the bases and
# input number from the user.
#16 2 3BF12
num_over_10 = {"A":"10","B":"11","C":"12","D":"13","E":"14","F":"15"}

def convert_to_10(num,base):
    #separas os numeros
    #coloca numero onde tem letra2 16 
    #multiplica pela potencia da base
    numlist = []
    numlist[:0] = num
    for x in range(len(numlist)):
        if numlist[x] in num_over_10:
            numlist[x] = num_over_10[numlist[x]]
    #coloca em prioridade posicional
    numlist.reverse()
    #transforma em int
    numlist = [int(n) for n in numlist]
    pot = 0
    output =0
    for n in numlist:
        output += n * base**pot
        pot += 1 
        
    
    return output

def convert_from_10(num,base):
    #Pega a maior potencia possivel e começa dela, vai adicionando as menores até zerar
    outputlist = []
    while num > base:
        resto = num%base
        outputlist.append(resto)
        num = int((num-resto)/base)
    outputlist.append(num)
    outputlist.reverse()

    output = ""
    for x in outputlist:
        output+=str(x)

    return output
    

    

if __name__ == "__main__":
   
    print("enter: the input base, the output base, number")
    x = input()
    split_x = x.split(' ')
    #print(split_x)
    if int(split_x[0]) < 2 or int(split_x[0]) >16 or int(split_x[1]) < 2 or int(split_x[1]) >16:
       raise Exception ("base out of limites 2 - 16")  
    inputb10 = convert_to_10(split_x[2],int(split_x[0]))
    
    
    output = convert_from_10(inputb10, int(split_x[1]))
    

    print(output + " Base " + split_x[1])