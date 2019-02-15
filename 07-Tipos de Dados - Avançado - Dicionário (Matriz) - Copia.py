print("<<< TIPOS DE DADOS AVANÇADOS - DICIONÁRIO (MATRIZ) >>>" + chr(10))

# Os tipos compostos que voce aprendeu - strings, listas e tuplas - utilizam inteiros como indices. Se voce tentar utilizar qualquer outro tipo como indice, voce receberá um erro.
# Dicionários sao similiares a outros tipos compostos exceto por eles poderem user qualquer tipo imutavel de dados como indice.
# Como exemplo, nos criaremos um dicionário para traduzir palavras em Inglês para Espanhol. Para esse dicionário, os indices serão strings.
# Uma maneira de criar um dicionario é comecando com um dicionário vazio e depois adiconando elementos. Um dicionário vazio é denotado assim {}:

#Exemplo 1:
print("Exemplo 1 - Dicionário Vazio -->")

dict = {}     # <-- Apenas declarado como vazio
print("Dicionário Vazio",dict," Qtde. Elementos:",len(dict))
print(type(dict))
print(chr(13))


#Exemplo 2:
print("Exemplo 2 - Dicionário Unitário (Simples) -->")

dict = {}                   # <-- Apenas declarado como vazio
dict['Animal']='cavalo'     # <-- Atribuindo Valor
print("Dicionário Unitário:",dict['Animal']," Qtde. Elementos:",len(dict))
print(type(dict))
print(chr(13))


#Exemplo 3:
print("Exemplo 3 - Dicionário Composto (Vários Itens) -->")

dict = {}    # <-- Declarado com valor vazio
dict['Suco']           = 'Laranja'     # <-- Atribuindo Valores
dict['Comida']         = 'Arroz'       # <-- Atribuindo Valores
dict['Acompanhamento'] = 'Carne'       # <-- Atribuindo Valores

print(dict['Suco'])                                # <-- Exibe apenas um elemento

print(dict,chr(10),"Qtde. Elementos:",len(dict))   # <-- Exibe todos os elementos
print(type(dict))
print(chr(13))



#Exemplo 4:
print("Exemplo 4 - Dicionário Composto com Multiplos Valores e Tipos (Linhas e colunas] -->")
matriz = {(0,3): 1, (2, 1): 2, (4, 3): 3}   # <-- Declarado e atribuido direto
print(matriz[0,3])     # <-- Exibe apenas um elemento
print(matriz)          # <-- Exibe todos os elementos
print(" Qtde. Elementos:",len(matriz))
print(type(matriz))
print(chr(13))


#Exemplo 5:
print("Exemplo 5 - Dicionário Composto com Multiplos Valores e Tipos (Linhas e colunas] -->")
familia = {}           # <-- Apenas Declarado como vázio
familia[0,0] = "Silas"
familia[0,1] = "Vera"
familia[1,0] = "Leonardo"
familia[1,1] = "Guilherme"
familia[1,2] = "Willian"

print(familia[0,0])          # <-- Exibe apenas um elemento
print(familia[1,1])          # <-- Exibe apenas um elemento
print(chr(13))
print(familia)               # <-- Exibe todos os elementos
print("Qtde. Elementos:",len(familia))
print(type(familia))
print(chr(13))


