#set é um conjunto pra armazenar valores únicos ou seja elimina valores repetidos

numeros = set([1,2,3,4,5,5,5,5,5,5,5,5,5,5])  
print(numeros)

for n in numeros:
    print(n)


A = {1,2,3}
B = {3,4,5}

Conjunto_somado = A.union(B)  
print(Conjunto_somado)  #valores que existem em A ou B

Conjunto_intersecao = A.intersection(B) 
print(Conjunto_intersecao)#valores que existem em A e B

Conjunto_diferente= A.difference(B)
print(Conjunto_diferente) #valores que existem em A mas não em B
Conjunto_diferente2= B.difference(A)
print(Conjunto_diferente2) #valores que existem em B mas não em A

Conjunto_simetrica= A.symmetric_difference(B)
print(Conjunto_simetrica)

SubsetA = A.issubset(B) #verifica se A é subconjunto de B
SubsetB = B.issuperset(A) #verifica se B é superconjunto de A
print(SubsetA, SubsetB) 