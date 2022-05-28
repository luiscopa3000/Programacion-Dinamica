#Verificar si el nombre es alfabeticamente menor que otro nombre.
def alfabeticamente_menor(nombre1, nombre2):
    if nombre1 < nombre2:
        return True
    else:
        return False

#Unir dos listas sin repetir elementos.
def unir_listas(lista1, lista2):
    lista_unida = lista1
    for i in lista2:
        if i not in lista_unida:
            lista_unida.append(i)
    return lista_unida
def proceso():
    import re
    while True:
        try:
            n = int (input())
            lis = []
            for i in range(n):
                tmp = input()
                tmp = re.sub(r'[0-9]+', ' ', tmp).split()
                lis = unir_listas(lis, tmp)
            avenA = input()
            c = 0
            for i in lis:
                if alfabeticamente_menor(i, avenA):
                    c += 1
            print(c)
        except EOFError:
            break
proceso()

