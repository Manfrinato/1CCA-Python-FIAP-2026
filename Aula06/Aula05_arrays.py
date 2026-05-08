listf = ["maçã","morango","uva"]

print(listf[1])

listf.append("jabuticaba")
print(listf[-1])
print()

tamanho = len(listf)

for i in range(tamanho):
    print(listf[i])


print()

for fruta in listf:
        print(fruta)

print()


msg =  input()

for i in range(len(msg)):
    print(msg[i])

