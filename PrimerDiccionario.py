#Problema 1045
from queue import PriorityQueue
def extrae(texto, lis ):
    import re
    nuevo = re.sub(r'[0-9]+', ' ', texto)
    texto = str(re.sub(r"[^a-zA-Z0-9]"," ",nuevo))
    busqueda =texto.split()
    for i in busqueda:
            lis.put(i)
def main(lis = PriorityQueue()):
    while True:
        try:
                x = input()
                extrae(x.lower(), lis)
        except EOFError:
            ant = ""
            while not lis.empty():
                temp = lis.get()
                if temp != ant:
                    print(temp)
                    ant = temp
            break
main()