def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota tem que ser entre 0 e 10")
        nota = float(input("digite a nota novamente:"))
    return nota

notaA = float (input("digite sua primeira nota:"))
notaA= validar_nota(notaA)



notaB = float (input("digite sua segunda nota:"))
notaB = validar_nota(notaB)

media = (notaA + notaB)/2
print (media)