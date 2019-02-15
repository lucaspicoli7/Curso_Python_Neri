print("<<< LISTAS >>>",chr(10))

"""
# Exemplo 1:
print("Exemplo 1 - Listas -->")
print('-'*50,chr(13))

animais = ["Cachorro","Gato","Galinha"]
print(animais,"- Quantidade de Elementos:",len(animais))
"""



# Exemplo 2:
print("Exemplo 2 - Declarando e Manipulando Listas -->")
print('-'*50,chr(13))

material = ["Cimento",1,True]
print(material,"- Quantidade de Elementos:",len(material))

print(material[0])
material[0] = "Areia"     # <-- Muda o Elemento 1
print(material[0])

"""




# Exemplo 3:
print("Exemplo 3 - Adicionando Elementos na Listas -->")
print('-'*50,chr(13))

notasMusicais = ["Dó","Ré","Mi","Fá"]
print(notasMusicais,"- Quantidade de Elementos:",len(notasMusicais))

# <-- Adicionando elementos à Lista letra a letra
notasMusicais += ["La"]              # <-- Adiciona elementos na Lista
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
notasMusicais.extend(["Si"])         # <-- Adiciona elementos na Lista (outra forma de fazer - usando extend)
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
notasMusicais.append("Dó")           # <-- Adiciona elementos na Lista (Usar sem os colchetes - insere na última posição)
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
notasMusicais.insert(4,"Sol")        # <-- Adiciona elementos na Lista (Em uma posição específica)
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
notasMusicais += "Lucas"             # <-- Se não colocar o colchetes [] ele adiciona letra a letra          
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))




# Exemplo 4:
print("Exemplo 3 - Removendo Elementos de uma Lista -->")
print('-'*50,chr(13))

notasMusicais = ["Dó","Ré","Mi","Fá","Sol","Lá","Si","Do"]
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
notasMusicais.pop()                  # <-- Remove o último elemento da lista
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
notasMusicais.pop(4)                 # <-- Remove o elemento da posição especificada na lista
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
del notasMusicais[2]                 # <-- Remove o elemento da posição especificada na lista (mesma coisa que o comando anterior)
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
notasMusicais.remove("Fá")           # <-- Remove o elemento com o conteúdo especificado
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))
notasMusicais = ["Dó","Ré","Mi","Fá","Sol","Lá","Si","Do"]
del notasMusicais[2:6]               # <-- Remove os elemento das posições especificada na lista (remove de uma fatia)
print(notasMusicais,"- Qtde. Elementos:",len(notasMusicais))





# Exemplo 5:
print("Exemplo 5 - Trocando Elementos de uma Lista -->")
print('-'*50,chr(13))

notasMusicais1 = ["Dó","Ré","Mi","Fá","Sol","Lá","Si","Do"]
notasMusicais2 = notasMusicais1       # Neste caso as variáveis terão o mesmo endereço de memória (alterar uma equivale a alterar a outra também)
print(notasMusicais1,"- Qtde. Elementos:",len(notasMusicais1))
print(notasMusicais2,"- Qtde. Elementos:",len(notasMusicais2))
notasMusicais2[4] = "Picoli"          # Substitui o elemento 4 (afeta a outra variavel também)
print(notasMusicais1,"- Qtde. Elementos:",len(notasMusicais1))
print(notasMusicais2,"- Qtde. Elementos:",len(notasMusicais2))
notasMusicais1 = ["Dó","Ré","Mi","Fá","Sol","Lá","Si","Do"]
notasMusicais3 = notasMusicais1[:]    # Neste caso as variáveis terão endereços de memória diferentes (alterar um não afeta em nada o outro, pois são independentes)
notasMusicais3[4] = "Picoli"          # Substitui o elemento 4 (NÃO afeta a outra variavel)
print(notasMusicais1,"- Qtde. Elementos:",len(notasMusicais1))
print(notasMusicais3,"- Qtde. Elementos:",len(notasMusicais3))




# Exemplo 6:
print("Exemplo 6 - Contando Elementos de uma Lista -->")
print('-'*50,chr(13))

carros = ["Dodge","Opala","Maverick","Karmanguia","Corcel","Opala","Fusca","Opala"]
print("Qtde. Opalas:",carros.count("Opala"))     # conta quantos opalas tem na lista




# Exemplo 7:
print("Exemplo 7 - Encontrar a Posição de um Elemento na Lista -->")
print('-'*50,chr(13))

carros = ["Dodge","Opala","Maverick","Karmanguia","Corcel","Opala","Fusca","Opala"]
print("Posição do Elemento:",carros.index("Maverick"))     # Mostra a posição do elemento na lista




# Exemplo 8:
print("Exemplo 8 - Reverter a sequencia da Lista -->")
print('-'*50,chr(13))

planetas = ["Mercúrio","Venus","Terra","Marte","Jupter","Saturno","Urano","Netuno","Plutão"]
print(planetas)
planetas.reverse()              # Inverte a sequencia dos itens na lista
print(planetas)




# Exemplo 9:
print("Exemplo 9 - Cópias de Lista -->")
print('-'*50,chr(13))

materiaisCasa = ["Areia","Cimento","Cal"]
materiaisSobrado=materiaisCasa              # Cópia semelhante - que aponta para o mesmo endereço de memória
print(materiaisCasa)
print(materiaisSobrado)

materiaisCasa.append("Pedra")               # Acrescentar um item a lista afeta a outra lista também pois
                                            # os dois compartilham o mesmo endereço de memória, ou seja,
                                            # é uma variável só com duas referências a ela.
print(materiaisCasa)
print(materiaisSobrado)

materiaisSobrado2=materiaisCasa[:]          # <-- Desta forma ele copia a variável criando uma nova (cópia independente)
                                            # Ao alterar uma não irá afetar a outra.
materiaisSobrado2.append("Cano")            # Desta forma ao Acrescentar um item a lista nao irá afetar o outro
                                            # os dois NÃO compartilham o mesmo endereço de memória.
print(materiaisCasa)
print(materiaisSobrado2)




# Exemplo 10:
print("Exemplo 10 - Ordenando uma Lista -->")
print('-'*50,chr(13))

materiaisCasa = ["Tijolo","Tábua",'Cano',"Areia","Cimento","Cal"]
print(materiaisCasa)
materiaisCasa.sort()                        # Ordena a Lista em ordem alfabética
print(materiaisCasa)

numeroMegaSena = [89,99,73,44,14,56,76,55,7]
print(numeroMegaSena)
numeroMegaSena.sort()                       # Ordena a Lista em ordem numérica (depende do tipo da lista)
print(numeroMegaSena)

estoque=["Cimento",1,True,"Areia",5,False,"Pedra",2,True]
print(estoque)
estoque.sort()                              # <-- Sort não funciona para tipo de dados hibrido - reporta erro.
print(estoque)





# Exemplo 11:
print("Exemplo 11 - Listas com For -->")
print('-'*50,chr(13))

materiaisCasa = ["Areia","Cimento","Cal"]
print(materiaisCasa)
for contador in materiaisCasa:
    print(contador)

# Outra forma de fazer numerando os itens da lista
for i, itemLista in enumerate(materiaisCasa):
    print("Lista Materiais ",i+1,"--> ",itemLista)




# Exemplo 12:
print("Exemplo 12 - Listando partes da lista -->")
print('-'*50,chr(13))

materiaisCasa = ["Areia","Cimento","Cal","Tijolo","Argamassa","Pedra","Táboa"]
print(materiaisCasa[3:])                    # <-- Neste caso lista a partir do elemento 3
print(materiaisCasa[:3])                    # <-- Neste caso lista até o elemento 3
print(materiaisCasa[2:5])                   # <-- Neste caso lista do elemento 2 até o 4




# Exemplo 13:
print("Exemplo 13 - Entrada de Dados na lista - uso do FOR -->")
print('-'*50,chr(13))

listaMembrosGrupo = []
while True:
    membroGrupo = input("Informe o Membro do Grupo (0 para fim): ")
    if membroGrupo == "0":
        break
    listaMembrosGrupo.append(membroGrupo)
    
print("Lista dos Membros do Grupo:",listaMembrosGrupo)





# Exemplo 13:
print("Exemplo 13 - Exemplo Pesquisa Estoque Mat. Construção -->")
print('-'*50,chr(13))

itensEstoque = ["Parafuso","Aroela","Porca","Bucha","Parafuso","Grampo","Rebite","Abraçadeira","Guia","Prego"]

materialPesquisado = input("Informe o Item do Estoque a Pesquisar: ")

for item in itensEstoque:
    if materialPesquisado == item:
        print('Item "%s" encontrado no estoque.' % materialPesquisado)
        break
else:
    print("Item incorreto ou inexistente no estoque, informe item válido.")
"""

