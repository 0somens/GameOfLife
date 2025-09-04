# Introducción a sistemas Conexionistas??
# Sacar la formula de Celcius to Farenheit usando datos de entrenamiento
# Regrsión lineal
# Datos de entrenamiento
dfx = [0,5,10,15,20,25,30,35,40,45]
dfy = [32,41,50,59,68,77,86,95,104,113]

# Variables
n = len(dfx)
xy = 0
sumx2 = 0 
sumx = 0
sumy = 0
sumxy = 0
# Sumatorias
for i in range(len(dfx)):
    # n.append(dfx[i]*dfy[i])
    # xy = n[i] + xy
    # x2.append(dfx[i]*dfx[i])
    sumx2 = dfx[i]**2 + sumx2
    sumx = dfx[i] + sumx
    sumy = dfy[i] + sumy
    sumxy = dfx[i] * dfy[i] + sumxy


# print("N = " , n)
# print("x * y = " ,xy)
print("x2 = " , sumx2)
print("SumX = " , sumx)
print("SumY = ", sumy)
print(sumxy)
b = (n * sumxy - sumx * sumy) / (n*sumx2 - sumx**2)

a = (sumy - b*sumx) / n

print(f"Recta: y = {a:.2f} + {b:.2f}x")

