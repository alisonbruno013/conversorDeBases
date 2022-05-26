#Alison Bruno Ferreira da Silva - 29843928


import os

import operacoes

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


print("Calculadora de Conversão\n")

print("""Escolha um tipo de converção ou aborte o processo:\n
[0] Para a aborta o processo
[1] Para converte de Deccimal para outras bases
[2] Para converter de outras bases para decimal""")


while True:
    operacao = int(input("\nDigite uma opção: "))
    
    if operacao >= 0 and operacao <3:
        break
    else:
        print("Operação inválida, Digite uma operação valida!")



if operacao == 0:
    
    cls()
    operacoes.tchau()
    
elif operacao == 1:
    
    cls()
    print("Escolha a base que deseja converte o decimal:\n")
    print("[1] Para Binário  \n[2] Para Octal \n[3] Para HexaDecimal \n[0] Para a aborta o processo")
   
    while True:
        
        tConversao = int(input("\nDigite uma opção: "))
        
        if tConversao >= 0 and tConversao <4:
            cls()
            break
    
        else:
            print("Operação inválida, Digite uma operação valida!")
    
    
    if tConversao != 0:
        num = int(input("Digite um numero para que seja feita a converção: "))
    
    if tConversao == 1:
        operacoes.dec_bin(num)
        
        
    elif tConversao == 2:
        operacoes.dec_oct(num)
        
    elif tConversao == 3:       
        operacoes.dec_hex(num)
    elif tConversao == 0:
        operacoes.tchau()
   

    
elif operacao == 2:
    cls()
    print("Escolha a base que deseja converte para decimal:\n")
    print("[1] De Binário  \n[2] De Octal \n[3] De HexaDecimal \n[0] Para a aborta o processo")
    
    while True:
        
        tConversao = int(input("\nDigite uma opção: "))
        
        if tConversao >= 0 and tConversao <4:
            cls()
            break
    
        else:
            print("Operação inválida, Digite uma operação valida!")

    
    if tConversao != 0:
        num = input("Digite um numero para que seja feita a converção: ")
    
    if tConversao == 1:
        operacoes.bin_dec(num)
    elif tConversao == 2:
        operacoes.oct_dec(num)
        
    elif tConversao == 3:
        operacoes.hex_dec(num)
    elif tConversao == 0:
          
        operacoes.tchau()