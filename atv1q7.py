import string
import random

def main():
    pswd = []
    for x in range(random.randint(6, 9)):
        pswd.append(chr(random.randint(33, 126)))

    print(pswd)

if __name__ == "__main__":
    main()