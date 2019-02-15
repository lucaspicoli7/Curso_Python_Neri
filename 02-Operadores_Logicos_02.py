print("<<< Operadores de Lógica >>>" + chr(10))
print("Operador de Pertence" + chr(10))

brasil  = 3
italia  = 7
america = [1,2,3,4,5]
europa  = [6,7,8,9,10]

print ("Brasil está contido na América?:",brasil in america)     # <-- Contido em
print ("Brasil está contido na Europa?.:",brasil in europa )
print (chr(10))

print ("Italia pertence a América?.....:",italia in america)
print ("Italia pertence a Europa?......:",italia in europa )
print (chr(10))

print ("Brasil não pertence a América?.:",brasil not in america)     # <-- Não está contido
print ("Italia não pertence a América?.:",italia not in america)
print (chr(10))
