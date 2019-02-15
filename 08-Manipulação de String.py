print("<<< MANIPULAÇÃO DE STRINGS >>>",chr(10))

# Exemplo 1:
print("Exemplo 1 - String Simples -->")
print('-'*50,chr(13))
NOME = "Lucas Picoli Bello"     # Lembrando que o Python faz diferenciação entre Maiúsculas e Minúsculas
nome = "Silas Belo"
print(NOME)
print(type(NOME))
print(chr(13))
print(nome)
print(type(nome))
print('-'*50,chr(10))



# Exemplo 2:
print("Exemplo 2 - Tamanho da String -->")
print('-'*50,chr(13))
print(len(NOME))
print(chr(13))
print(len(nome))
print('-'*50,chr(10))



# Exemplo 3:
# Lembrando que começa na posição 0 (zero) 
print("Exemplo 3 - Extraindo Parte da String e Fatiamento -->")
print('-'*50,chr(13))
print(NOME[6],chr(13))                  # <-- Demonstra a Posição 6 da String 
print(nome[7],chr(13))                  # <-- Demonstra a Posição 7 da String
frase1 ="O Brasil é o país da corrupção."
frase2 ="Só a bateria tem a solução."
print(frase1[0:17])                     # <-- Demonstra da posição  0 até 17
print(frase1[:17])                      # <-- Demonstra da posição  0 até 17
print(frase1[13:])                      # <-- Demonstra a partir da posição 13 até o final
print(frase1[0:21] + frase2[19:27])     # <-- Demonstra concatenação de duas posicoes de cada string
print('-'*50,chr(10))



# Exemplo 4:
print("Exemplo 4 - Concatenação de String -->")
print('-'*50,chr(13))
cidade = 'Londrina'
estado = 'Paraná'
pais   = 'Brasil'
print(cidade + ' - ' + estado + ' - ' + pais,chr(13))       # <-- Concatena 3 Strings 
print(cidade + ' - ' + cidade + ' - ' + cidade,chr(13))     # <-- Concatena a mesma string
print(cidade*5,chr(13))                                     # <-- Concatena a mesma string 5 vezes de forma mais simples
print('-'*50,chr(10))



# Exemplo 4:
# Forma mais simples e prática de concatenação 
print("Exemplo 5 - Substituição de Strings (Substitute) -->")
print('-'*50,chr(13))
nome    = 'Rosinalva'
idade   = 28
salario = 2300
print("Nome: %s - Idade: %d - Salário: %d" %(nome,idade,salario),chr(13))       # <-- Concatena 3 Strings 
print('-'*50,chr(10))



# Exemplo 5:
print("Exemplo 5 - Caps, Centralizar, Contar Caracteres, Terminação da String -->")
print('-'*50,chr(13))
nome    = "LUCAS PICOLI"
print("Nome convertido em Minúsculo:",nome.lower())                               # <-- Coloca todo o conteúdo da string em minúsculo 
print(chr(13))
print("Nome convertido em Título (Primeiras Letras em Maiúsculo):",nome.title())  # <-- Coloca as primeiras letras das palavras em maiúsculo 
print(chr(13))
nome    = "Lucas Picoli"
print("Nome invertido Maiúsculo/Minúsculo:",nome.swapcase())                      # <-- Inverte caracteres maiúsculos por minúsculos e vice-versa
print(chr(13))
nome    = "lucas picoli"
print("Nome convertido em Maiúsculo:",nome.upper())                               # <-- Coloca todo o conteúdo da string em minúsculo 
print(chr(13))
print("Nome:",nome.capitalize())                                                  # <-- Coloca o primeiro caracter em maiúsculo 
print(chr(13))
print("Centralizado:",nome.center(30))                                            # <-- Centraliza o texto em 30 caracteres 
print(chr(13))
print("Qt. Letra 'C':",nome.count("c"))                                           # <-- Conta quantas letras 'c' existe na string
print(chr(13))
print("Termina com 'li'?:",nome.endswith('li'))                                   # <-- Retorna True se nome termina com 'li'
print('-'*50,chr(10))



# Exemplo 6:
# O método find e index tem funcionamentos similares
print("Exemplo 6 - Localizar String dentro de String -->")
print('-'*50,chr(13))
cidadeLinda = "Londrina capital do café"
print("Cidade:",cidadeLinda)
print(chr(13))
print("Qual a Posição do trecho 'capital' na String?:",cidadeLinda.find('capital'))     # <-- Obs: Faz diferenciação entre minúsculas e maiúsculas
print(chr(13))
print("Qual a Posição do trecho 'ca' na String?:",cidadeLinda.find('ca'))               # <-- Note que há 2 'ca' na string, aqui ele acha o primeiro
print(chr(13))
print("Qual a Posição do trecho 'ca' na String?:",cidadeLinda.find('ca',11))            # <-- Aqui ele vai buscar a string a partir da posicao 11
print(chr(13))
print("Qual a Posição do 2º trecho 'c' na String?:",cidadeLinda.index('a',8))           # <-- Comando Index - vai buscar o caracter 'c' a partir da posicao 8
print(chr(13))
print('-'*50,chr(10))



# Exemplo 7:
print("Exemplo 7 - Testar o Tipo do Conteúdo de uma Variável -->")
print('-'*50,chr(13))
endereco = "RuaLondrina"
print("Endereço:",endereco)
print("Essa Variável é Alfa?:",endereco.isalpha())     # <-- Testa se no conteúdo contém apenas letras do alfabeto
print(chr(13))
endereco = "Rua Londrina, 700"
print("Endereço:",endereco)
print("Essa Variável é Alfa?:",endereco.isalpha())     # <-- Retorna False porque o espaço não é uma letra.
print(chr(13))
endereco = "Rua Londrina, 700"
print("Endereço:",endereco)
print("Essa Variável é Alfa?:",endereco.isalpha())     # <-- Retorna False porque tem espaço, virgula e números.
print(chr(13))
var = input("Digite o Conteúdo Desejado: ")
print("Essa Variável é Alfa?   ",var.isalpha())                   # <-- Testa se o conteúdo é alfabético.
print("Essa Variável é Número?",var.isnumeric())                  # <-- Testa se o conteúdo é um número.
print("Essa Variável é Decimal?",var.isdecimal())                 # <-- Testa se o conteúdo é decimal.
print("Essa Variável é Dígito? ",var.isdigit())                   # <-- Testa se o conteúdo é um dígito.
print("Essa Variável está em maiúsculo? ",var.isupper())          # <-- Testa se o conteúdo está em maiúsculo.
print("Essa Variável está em minúsculo? ",var.islower())          # <-- Testa se o conteúdo está em minúsculo.
print("Essa Variável é em forma Titulo? ",var.istitle())          # <-- Testa se o conteúdo está em forma de título (primeira letra de cada palavra em maiúsculo)
print("Essa Variável Contém Somente Espaços? ",var.isspace())     # <-- Testa se o conteúdo possui apenas espaços em branco (retorna False se conteúdo não tiver nenhum espaço)
print('-'*50,chr(10))



# Exemplo 8:
print("Exemplo 8 - Junção de Elementos String (Join), Justificação (ljust), Particionamento de String -->")
print('-'*50,chr(13))
familia = ['Pedro','Maria','Fernanda','Glasielli','Felipe']
print(familia)
print("-".join(familia))                 # Junta todos os elementos de família e exibe eles separado por "-"
print(" / ".join(familia))               # Junta todos os elementos de família e exibe eles separado por " / "
print("\n".join(familia))                # Exibe todos os elementes, com uma quebra de linha em cada um deles
print(chr(13))
palavra1 = "Picoli"
palavra2 = "Bello"
print(palavra1.ljust(30) + palavra2)     # Alinha a Expressão à esquerda completando com espaços a direita  até completar o tamanho desejado (30)
print(palavra1.rjust(30) + palavra2)     # Alinha a Expressão à direita  completando com espaços a esquerda até completar o tamanho desejado (30)
print(chr(13))
dados="15400Londrina2500"
print(dados.partition("Londrina"))                  # Divide a string em tuplas tendo como base uma parte da string
print("400Curitiba99099".partition("Curitiba"))     # Divide a string em tuplas tendo como base uma parte da string
print("400São Paulo99099".partition("400"))         # Divide a string em tuplas tendo como base uma parte da string
print("400São Paulo99099".rpartition("0"))          # Divide a string em tuplas partindo do parte da string mais a direita
print(chr(13))
print("Lucas Picoli Bello".split())                 # Divide a string em tuplas tendo como base o espaço
print("Lucas;Picoli;Bello".split(';'))              # Divide a string em tuplas tendo como base o ponto e vírgula
print("Lucas;Picoli;Bello".rsplit(';'))             # Divide a string em tuplas tendo como base o ponto e vírgula mais a direita
print('-'*50,chr(10))



# Exemplo 9:
print("Exemplo 9 - Substituição de Parte da String ou Expressão / Acrescimo de Caracteres na String-->")
print('-'*50,chr(13))
print("|" + "        Lucas  Picoli    Bello    ".strip() + "|")      # Elimina os espaços a direita e a esquerda da string ou expressão
print("|" + "        Lucas  Picoli    Bello    ".rstrip() + "|")     # Elimina os espaços a direita  da string ou expressão
print("|" + "        Lucas  Picoli    Bello    ".lstrip() + "|")     # Elimina os espaços a esquerda da string ou expressão
print(chr(13))
print("15100".zfill(50))      # Acrescenta 0 (Zeros) a esquerda da string ou expressão
print('-'*50,chr(10))



# Exemplo 10:
print("Exemplo 10 - Teste de Conteúdo de String -->")
print('-'*50,chr(13))
funcionario = "Lucas Picoli Bello"
print("String começa com 'Lucas'?",funcionario.startswith("Lucas"))    # Retorna Verdadeiro se a String ou expressão iniciar com a expressão especificada
print('-'*50,chr(10))



