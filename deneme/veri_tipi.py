''' daire Alanı     : pi

'''
pi = 3.14
yariCap = float(input("yarı çap: "))
alan = pi * (yariCap ** 2)
print(type(alan))

cevre = 2*pi*yariCap
print(type(cevre))

print('alan'+ str(alan) + 'cevre', str(cevre))

