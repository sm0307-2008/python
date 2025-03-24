n1 = int(input('Digite algum número: '))
n2 = int(input('Digite algum número: '))
n3 = int(input('Digite algum número: '))
if n1>n2 and n3>n2:
    soma=n1+n3
elif n2>n1 and n3>n1:
    soma=n2+n3
else:
    soma=n1+n2
    
print(soma)
