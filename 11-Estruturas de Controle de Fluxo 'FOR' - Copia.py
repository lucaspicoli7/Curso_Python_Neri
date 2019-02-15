print("<<< ESTRUTURAS DE CONTROLE 'FOR' >>>",chr(10))

# Exemplo 1:
print("Exemplo 1 - Forma Simples do 'FOR' -->")
print('-'*50,chr(13))

# Lista cada item da string (pode ser número, letra ou símbolo)
for contador in '01234567890abcdefg!@#$%':
    print("Posição..:",contador)
print('-'*50,chr(10))



# Exemplo 2:
print("Exemplo 2 - Repetição por Range -->")
print('-'*50,chr(13))

# Executa a repetição n vezes começando do 0 (zero) 
for contador in range(50):
    print("Posição..:",contador)
else:
    print("Fim das Repetições.")
print('-'*50,chr(10))


# Executa a repetição n vezes começando do 30 até 50 pulando de 2 em 2 
for contador in range(30,50,2):     
    print("Posição..:",contador)
else:
    print("Fim das Repetições.")
print('-'*50,chr(10))



# Executa a repetição n vezes começando do 30 até 50 pulando de 2 em 2 
for contador in range(50,40, -1):     
    print("Posição..:",contador)
else:
    print("Fim das Repetições.")
print('-'*50,chr(10))


for contador in range(-6,6):     
    print("Posição..:",contador)
else:
    print("Fim das Repetições.")
print('-'*50,chr(10))


# Tabuada
numTabuada = int(input("Digite um número para tabuada:"))
for tabuada in range(1,10):     
    print("%d * %d = %d" % (numTabuada,tabuada,(numTabuada * tabuada)))
print('-'*50,chr(10))




# Executa a repetição n vezes começando do 30 até 50 pulando de 1 em 1
# Quando chegar no 35 ele passa adiante (continua) sem executar o 35
for contador in range(30,50,1):
    if contador == 35:
        continue
    print("Posição..:",contador)
else:
    print("Fim das Repetições.")
print('-'*50,chr(10))



# Exemplo 3:
print("Exemplo 3 - Repetição Utilizando uma Lista -->")
print('-'*50,chr(13))

# Executa a repetição para cada item da lista 
for planeta in ["Mercúrio","Venus","Terra","Marte","Jupiter","Saturno","Urano","Netuno","Plutão"]:
    print("Planeta..:",planeta)
else:
    print("Fim dos Planetas.")
print('-'*50,chr(10))



# Exemplo 4:
print("Exemplo 4 - Repetição com Tuplas -->")
print('-'*50,chr(13))

# Executa a repetição com Tuplas
for cores in [("Preto","Branco"),("Verde","Amarelo"),("Azul","Vermelho"),("Prata","Ouro")]:
    print("Cor..:",cores)
print('-'*50,chr(10))



# Exemplo 5:
print("Exemplo 5 - Repetição com Interrupção (break) -->")
print('-'*50,chr(13))

# Executa a repetição até o break 
for planeta in ["Mercúrio","Venus","Terra","Marte","Jupiter","Saturno","Urano","Netuno","Plutão"]:
    print("Planeta..:",planeta)
    if planeta == "Urano":
        break
else:      # Este else nunca será executado porque o break interrompe a repetição antes
    print("Fim dos Planetas.")
print('-'*50,chr(10))



# Exemplo 6:
print("Exemplo 5 - Soma (por incremento) (o interessante é como é feito a soma '+=' ) -->")
print('-'*50,chr(13))

print("Soma dos números de 1 a 10) -->")
valorTotal = 0
for numero in range(1,11):
    valorTotal += numero
print("Valor Total",valorTotal)



