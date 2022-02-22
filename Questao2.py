print("A senha tem que conter:")
print ("No mínimo 6 caracteres,Contém no mínimo 1 digito")
print ("No mínimo 1 letra em minúsculo.")
print ("No mínimo 1 letra em maiúsculo.")
print ("No mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+")

senha=""
while (senha!="sair"):
    senha=(input("Senha:"))
    erro=0
    if len(senha)<=0:
        erro+=6
        print(erro)
    else:
        if any(num.isdigit () for num in senha): #Pelo menos 1 digito
            print("Contém no mínimo 1 digito")
        else: #Não contido 1 digito
            print("Não contém no mínimo 1 digito")
            erro+=1
        if any(x.islower () for x in senha): #Pelo menos 1 letra em minúsculo
            print("Contém no mínimo 1 letra em minúsculo")
        else: #Não contido 1 letra em minúsculo
            print("Não contém no mínimo 1 letra em minúsculo")
            erro+=1
        if any(x.isupper () for x in senha): #Pelo menos 1 letra em maiúsculo
            print("Contém no mínimo 1 letra em maiúsculo")
        else: #Não contido 1 letra em maiúsculo
            print("Não contém no mínimo 1 letra em maiúsculo")
            erro+=1
        if(str("!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "(" or ")" or "-" or "+") in (senha)): #Pelo menos 1 caractere especial
            print("Contém no mínimo 1 caractere especial")
        else: #Não contido 1 caractere especial
            print("Não contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+")
            erro+=1
        if len(senha)>=6: #Quatidade de senha de acordo com o limite
            print("Contém no mínimo 6 caracteres")
            print(erro)
        elif len(senha)==5:
            if erro==1:
                print(1)
            if erro==2:
                print(2)
            if erro==3:
                print(3)
        elif len(senha)==4:
            if erro==1:
                print(2)
            if erro==2:
                print(2)
            if erro==3:
                print(3)
        elif len(senha)==3:
            print(3)
        elif len(senha)==2:
             print(4)
        elif len(senha)==1:
                print(5)     
        
        
        


