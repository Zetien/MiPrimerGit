print ('programa que imprime serie fibonnaci hasta donde digite el usuario') 
n=int(input('Digite un numero hasta donde va a llegar la serie Fibonacci: \r\n')) 
a=0
b=1
c=0
contador=1
print('')
while contador<=n:
    print(c)
    contador+=1
    a=b
    b=c
    c=a+b
