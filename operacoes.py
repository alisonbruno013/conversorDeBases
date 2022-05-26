#Alison Bruno Ferreira da Silva - 29843928

def tchau ():
    print("\nProcesso abortado")
       
    
def dec_hex (num):
    divNum = num

    hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    numOp = ""
    
    while divNum != 0:
        resto = divNum%16
        numOp = str(hexa[resto]) + numOp
        divNum = divNum//16
        
    
    if numOp == "":
        numOp = "0"
    
    print(f"\nO Hexadecimaol de {num} é igual a {numOp} ")
    
    
    
def dec_oct (num):
    
    divNum = num

    numOp = ""
        
    while divNum != 0:
        resto = divNum%8
        numOp = str(resto) + numOp
        divNum = divNum//8
    
    if numOp == "":
        numOp = "0"
    
    print(f"\nO Octal de {num} é igual a {numOp} ")
    
      
def dec_bin (num):
    
    divNum = num

    numOp = ""
    
    while divNum != 0:
        resto = divNum%2
        numOp = str(resto) + numOp
        divNum = divNum//2
    
    if numOp == "":
        numOp = "0000"
    
    print(f"\nO binário de {num} é igual a {numOp} ")
    
    
    
def hex_dec (num):
    
    str(num)

    numOp = 0

    hexa = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    n = (len(num)-1) 
    
    numHexa = []
    
    for i in num.upper():
        numHexa.append(hexa.index(i))
    
    
    for x in numHexa:
        
        numOp = numOp + int(x)*16**n
        n = n - 1

    print(f"\nO Hexadecimal de {num} é igual a {numOp} em Decimal ")
    
    
    
    
def oct_dec (num):
    str(num)

    numOp = 0

    n = (len(num)-1) 
    
    for x in num:
            
        numOp = numOp + int(x)*8**n
        n = n - 1

    print(f"\nO Octal de {num} é igual a {numOp} em Decimal ")
    
    
    
def bin_dec (num):
    str(num)

    numOp = 0


    n = (len(num)-1) 
    
    for x in num:
            
        numOp = numOp + int(x)*2**n
        n = n - 1
    
    print(f"\nO binário de {num} é igual a {numOp} em Decimal ")