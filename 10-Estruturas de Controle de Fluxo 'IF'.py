print("<<< ESTRUTURAS DE CONTROLE DE FLUXO 'IF / FOR' >>>",chr(10))

# Exemplo 1:
print("Exemplo 1 - Forma Simples 'IF/ELSE' -->")
print('-'*50,chr(13))
cargaMaxCaminhaoKg = 6000
cargaInformadaEmKg = float(input("Informe a Carga do Caminhão em Kg: "))
if cargaInformadaEmKg >= cargaMaxCaminhaoKg:
    print("Carga Superior a Capacidade do Caminhão!")
else:
    print("Carga Suportável para o Caminhão!")
print('-'*50,chr(10))



# Exemplo 2:
print("Exemplo 2 - Forma Complexa 'IF/ELIF/ELSE' -->")
print('-'*50,chr(13))
cargaMaxCaminhaoKg = 6000
cargaInformadaEmKg = float(input("Informe a Carga do Caminhão em Kg: "))
if cargaInformadaEmKg == 0:
    print("Caminhão Vazio!")
elif cargaInformadaEmKg <= 1000:
    print("Caminhão com pouca Carga!")
elif cargaInformadaEmKg > 1000 and cargaInformadaEmKg <= 5500:
    print("Ainda Cabe mais Carga!")
elif cargaInformadaEmKg > 5500 and cargaInformadaEmKg < cargaMaxCaminhaoKg:
    print("Carga no Limite - Caminhão quase cheio!")
elif cargaInformadaEmKg == cargaMaxCaminhaoKg:
    print("Caminhão está Completo - não cabe mais nada!")
else:
    print("Carga Superior a Capacidade do Caminhão!")
print('-'*50,chr(10))
