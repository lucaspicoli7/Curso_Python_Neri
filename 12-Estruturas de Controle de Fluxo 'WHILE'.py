print("<<< ESTRUTURAS DE CONTROLE 'FOR' >>>",chr(10))

# Exemplo 1:
print("Exemplo 1 - While -->")
print('-'*50,chr(13))

while True:
    print("Os Políticos Brasileiros são corruptos...")
print('-'*50,chr(13))

#Obs: Para parar esse laço infinito teclar CTRL + C




# Exemplo 2:
print("Exemplo 2 - While' -->")
print('-'*50,chr(13))

var1 = 0
while var1 <= 10:
    print("Ordem:", var1)
    #var1 = var1 + 1
    var1 += 1     # <-- Incrementa a variável
else:
    print("Fim do While")
print('-'*50,chr(13))




# Exemplo 2:
print("Exemplo 3 - While' -->")
print('-'*50,chr(13))

animais = ["Galinha","Pato","Girafa","Leão","Baleia","Hipopótamo","Ema"]
i = 0
while i < len(animais):
    print("Animal:",animais[i])
    i += 1     
print('-'*50,chr(13))


