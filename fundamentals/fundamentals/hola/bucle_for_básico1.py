'''Contador del 0 al 150'''
for i in range(151):
    print(i)

'''Múltiplos de cinco'''
for i in range(5,1005,5):
    print(i)

'''Contar, a la manera del Dojo'''
for i in range(1,101):
    if i % 10 == 0:
        print ("coding dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print(i)

'''Whoa. Es un gran idiota'''
sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)
    

'''Cuenta regresiva de a 4'''
y = 2018
while y > 0:
    print(y)
    y = y - 4
    if y == 0:
        break
else:
    print("sentencia else final")

'''Contador flexible'''

N1= 4
N2= 18
N3= 6

for i in range(N1,N2+1):
    if i % N3 == 0:
        print(i)