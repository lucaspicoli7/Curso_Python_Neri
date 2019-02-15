print("<<< TIPOS DE DADOS AVANÇADOS >>>" + chr(10))

# Tupla - igual ao tipo list, porém, imutável
# Uma tupla consiste em uma sequência de valores separados por vírgulas,
# podendo ser vista como lista em Python, com a diferença de ser imutável (assim como strings).
# Pode receber diferentes tipos de dados em sua lista
# Para acessar o primeiro item da tupla a indexação é 0
# Pode ser declarado apenas com uma vírgula entre os itens

#Exemplo 1:
print("Exemplo 1 - Tupla com Conteúdos Diferentes:")
tupla1 = 1, 2, 'Londrina', 5.4, False
print ("1º Primeiro Conteúdo:",tupla1[0])
print ("2º Primeiro Conteúdo:",tupla1[1])
print ("3º Primeiro Conteúdo:",tupla1[2])
print ("4º Primeiro Conteúdo:",tupla1[3])
print ("5º Primeiro Conteúdo:",tupla1[4])
print ("Qt. Elementos:",len(tupla1))
print(type(tupla1))
print(chr(10))

# Podemos aninhar tuplas:
print("Exemplo 2 - Tuplas Aninhadas:")
tupla2 = tupla1, (1, 2, 3, 4, 5)
print ("Tupla Aninhada......:",tupla2,"Qt.Elementos:",len(tupla2))
print(type(tupla2))
print(chr(13))

"""
No exemplo retirado da Documentação Oficial, as tuplas são sempre envolvidas por parênteses quando aparecem na saída, a vantagem disso é que quando houverem tuplas aninhadas, a sua leitura será feita corretamente.
Uma das grandes utilidades das Tuplas é para a representação de valores constante, aleḿ disso elas podem ser usadas de diversas formas: pares ordenados (x, y), registros de funcionário extraídos uma base de dados, etc.
Um ponto interessante é a criação de tuplas contendo 0 ou 1 itens: a sintaxe usa certos truques para acomodar estes casos. No caso das Tuplas vazias, um par de parênteses vazios é o necessário para construí-la;
uma tupla unitária é construída por um único valor e uma vírgula entre parênteses (não basta colocar um único valor entre parênteses). Um pouco estranho, mas é assim que funciona:
"""
print("Exemplo 3 - Tupla Vazia:")
vazia = ()
#len(vazia)
print("Tupla Vazia:",vazia,"Qt.Elementos:",len(vazia))
print(type(vazia))
print(chr(13))

print("Exemplo 4 - Tupla Unitária:")
unitaria = "Hello!"
print("Tupla Unitária:",unitaria)
unitaria = "Hello!",
print("Tupla Unitária:",unitaria)
print(type(unitaria))
print(chr(13))

#As tuplas também suportam acesso aos valores através dos índices e maior parte das operações das listas, como fatiamento. Podemos utilizá-las também com o for:
print("Exemplo 4 - Tupla com For:")
numeros = (1, 2, 3, 4)
for num in numeros:
    print(num)
print(type(numeros))    
print(chr(13))

