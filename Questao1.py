n=0
n=input(str("n="))
n=int(n)
valor=0
valor=n*("*")
i=len(valor)
for i in range(1,len(valor)+1): #Elaboração da Escada
    espaço=(len(valor)-i)*" " #Adição do espaço " " e caractere "*"
    print(espaço+valor[:i])
    
    
    



