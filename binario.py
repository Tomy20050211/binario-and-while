num = float(input("Introduce un número decimal: "))
ent, dec = int(num), num %1
binEnt = bin(ent) [2:]
binDec = ''.join(str(int((num*2**i)%2)) for i in range (1, 11))
print(f"Binario: {binEnt}. {binDec}")