#Mititi Dan Ioan
#Inginerie anul I
print("Porti logice Calculator")


def AND(a, b):  # AND Gate
    a = int(a)
    b = int(b)
    if a == 1 and b == 1:  
        return 1
    else:
        return 0


def NAND(a, b):  
    a = int(a)
    b = int(b)
    if a == 1 and b == 1:  
        return 0
    elif a == 1 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 0
    else:
        return 1


def OR(a, b):  
    a = int(a)
    b = int(b)
    if a == 1:  
        return 1
    elif b == 1:
        return 1
    else:
        return 0


def NOR(a, b):  
    a = int(a)
    b = int(b)
    if a == 1 and b == 0:  
        return 1
    elif a == 0 and b == 1:
        return 1
    elif a == 0 and b == 0:
        return 1
    else:
        return 0


def XOR(a, b):  
    a = int(a)
    b = int(b)
    if a == 1 and b == 0:  
        return 1
    elif a == 1 and b == 1:
        return 1
    else:
        return 0


def main():  
    run = True
    while run:  
        question = input("Ce tip de poarta doriti OR, AND, NOR, or NAND or (Q)uit: ")  
        if question == "AND" or question == "and" or question == "And":  
            a = input("Introduce-ti valoarea pentru input 1 (1 or 0):")  
            b = input("Introduce-ti valoarea pentru input 2 (1 or 0):")  
            x = AND(a, b) 
            print("Output-ul va fii:", x)  
        elif question == "OR" or question == "or" or question == "Or":  
            a = input("Introduce-ti valoarea pentru input 1 (1 or 0):")  
            b = input("Introduce-ti valoarea pentru input 2 (1 or 0):")  
            x = OR(a, b)  
            print("Output-ul va fii:", x)  # Output result
        elif question == "NOR" or question == "nor" or question == "Nor":  
            a = input("Introduce-ti valoarea pentru input 1 (1 or 0):")   
            b = input("Introduce-ti valoarea pentru input 2 (1 or 0):")  
            x = NOR(a, b)  
            print("Output-ul va fii:", x)  
        elif question == "NAND" or question == "nand" or question == "Nand":  
            a = input("Introduce-ti valoarea pentru input 1 (1 or 0): ")  
            b = input("Introduce-ti valoarea pentru input 2 (1 or 0): ")  
            x = NAND(a, b)  
            print("Output-ul va fii::", x)  
        elif question == "XOR" or question == "xor" or question == "Xor":  
            a = input("Introduce-ti valoarea pentru input 1 (1 or 0): ")  
            b = input("Introduce-ti valoarea pentru input 2 (1 or 0): ")  
            x = XOR(a, b)  
            print("Output-ul va fii:", x)  
        elif question == "Q" or question == "q":  
            run = False
        else:
            print("Te rog Introduce-ti una dintre portile aratate, multumesc")  
            


main()
