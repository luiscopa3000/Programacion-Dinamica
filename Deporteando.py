


def porce():
    n = int (input())
    dic1 = {}
    dic2 = {}
    for i in range(n):
        x,y = map(str,input().split())
        if len(y) == 2:
            dic2[int(x)] = y
        else:
            dic1[int(x)] = y
    temp1 = {}
    temp2 = {}
    while len(dic1) > 0 and len(dic2) > 0:
        x,y = min(dic1.items(), key=lambda x:x[1])
        print(x,y)
        print(dic1.popitem(y))
        
#porce()
dic = {9:"FW", 11: "WB" , 4:"B"}
def mostrar(lsit):
    while not lsit.empty():
        print(lsit.get())
from queue import PriorityQueue
def test():
    n = int (input())
    lis1 = PriorityQueue()
    lis2 = PriorityQueue()
    for i in range(n):
        z = input()
        x,y = list(map(str,z.split()))
        if len(y) == 2:
            lis2.put((int(x),y))
        else:
            lis1.put((int(x),y))
    mostrar(lis1)
    mostrar(lis2)
    
test()


