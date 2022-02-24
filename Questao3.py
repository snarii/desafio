from collections import Counter #Para filtrar específicamente os anagramas
def all_substrs(a):
    return [[a[j:j+i] for j in range(len(a) - i + 1)] for i in range(1, len(a))]
def countem(filtro):
    qt=Counter()
    a=0
    for ana in filtro:
        for es in ana: #Colocando em ordem os pares
            q=''.join(sorted(es))
            qt[q] += 1
    for es in qt:
        a += int(qt[es]*(qt[es]-1)/2)
    return a
a=input("Palavra:")
print(countem(all_substrs(a)))
