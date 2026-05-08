nome=["Bob","luis","ana","felipe"]
tamanho=len(nome)


for i in range(tamanho):
    for j in range(i+1,tamanho):
        

        print (nome[i],nome[j])


print("==============================")





#correção
for i in range(len(nome)):
    for j in range(i+1,len(nome)):
        print(nome[i],nome[j])