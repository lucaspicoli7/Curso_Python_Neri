print("<<< MANIPULAÇÃO DE STRINGS >>>",chr(10))

# Exemplo 1:
print("Exemplo 1 - Entrada de Dados Simples -->")
print('-'*50,chr(13))
nome    = input("Informe o Nome    do Funcionário: ")
idade   = input("Informe a Idade   do Funcionário: ")
salario = input("Informe o Salário do Funcionário: ")
print("Nome: %s - Idade: %s - Salário: %s" %(nome,idade,salario),chr(13))     # <-- Note que os tipos aqui são todos strings na substituição
print('-'*50,chr(13))

# Exemplo 2:
# Entrada de Dados Simples
print("Exemplo 2 - Entrada de Dados com Conversão de Tipo de Dados -->")
print('-'*50,chr(13))
nome    =       input("Nome    do Funcionário: ")
idade   = int  (input("Idade   do Funcionário: "))
salario = float(input("Salário do Funcionário: "))
print("Nome: %s - Idade: %d - Salário: R$ %9.2f" %(nome,idade,salario),chr(13))     # <-- Note que os tipos aqui nao são somente string
print('-'*50,chr(13))
