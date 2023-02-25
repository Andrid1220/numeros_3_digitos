# porgrama para invertir un munero de 3 digitos

print("----------------------------")
print("-----INVERTIR DIGITOS-------")
print("----------------------------")

# input 

n = int(input("digite el valor de n: ") )

# procesing

mod = n % 10
de =  n // 10

# output

print("-----------------------------")
print("------RESULTADO--------------")
print("-----------------------------")
print("Reciduo: " + str(mod))
print("Parte entera: " + str(de))
