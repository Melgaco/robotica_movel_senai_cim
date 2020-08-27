def reduce(numer, denom):
    if numer % 9 == 0 and denom % 9 == 0:
        numer /= 9
        denom /= 9
        reduce(numer, denom)
    elif numer % 8 == 0 and denom % 8 == 0:
        numer /= 8
        denom /= 8
        reduce(numer, denom)
    elif numer % 7 == 0 and denom % 7 == 0:
        numer /= 7
        denom /= 7
        reduce(numer, denom)
    elif numer % 6 == 0 and denom % 6 == 0:
        numer /= 6
        denom /= 6
        reduce(numer, denom)
    elif numer % 5 == 0 and denom % 5 == 0:
        numer /= 5
        denom /= 5
        reduce(numer, denom)
    elif numer % 4 == 0 and denom % 4 == 0:
        numer /= 4
        denom /= 4
        reduce(numer, denom)
    elif numer % 3 == 0 and denom % 3 == 0:
        numer /= 3
        denom /= 3
        reduce(numer, denom)
    elif numer % 2 == 0 and denom % 2 == 0:
        numer /= 2
        denom /= 2
        reduce(numer, denom)
    else:
        print("Reduced: " + str(int(numer)) + "/" + str(int(denom)))
        return

def main():
    numer = int(input("What's your numerator: "))
    denom = int(input("What's your denominator: "))
    reduce(numer, denom)
    print("=====")

if __name__ == "__main__":
    main()
