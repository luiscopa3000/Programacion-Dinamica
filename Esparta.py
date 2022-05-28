#separar de la lista los caracteres que no sean letras
def separar_letras(lista):
    lista_letras = []
    temp = []
    for i in lista:
        if i.isalpha():
            lista_letras.append(i)
        elif i.isnumeric():
            temp.append(int(i))
        elif i == '+' and len(temp) > 1:
            x = temp.pop()
            y = temp.pop()
            temp.append(y + x)
        elif i == '*' and len(temp) > 1:
            x = temp.pop()
            y = temp.pop()
            temp.append(y * x)
    print("".join(lista_letras)[::-1]+": habilidad", end=" ")
    return temp.pop()
def main():
    while True:
        try:
            st = list(input())
            lis = separar_letras(st)
            print(str(lis))
        except EOFError:
            break
main()