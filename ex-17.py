n1 = int(input('Digite algum número: '))
n2 = int(input('Digite algum número: '))
n3 = int(input('Digite algum número: '))
if(n1>n2>=n3):
    nm=n1
elif(n2>=n1>=n3):
    nm=n2
else:
    nm=n3
    
print('o número maior:', nm)
