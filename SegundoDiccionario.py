from queue import PriorityQueue
import re
def proceso():
    lis = PriorityQueue()
    temp = []
    while True:
        try:
            x = input()
            x = x.lower()
            temp += list(map(str, x.split()))
        except EOFError:
            while True:
                try:
                    y = temp.pop(0)
                    if "-" in y:
                        if y.index("-") == len(y)-1:
                            while True:
                                if y[len(y)-1] == "-": 
                                    y += temp.pop(0)
                                else:
                                    break
                            lis.put(re.sub(r"[^a-z]","",y))
                        else:
                            lis.put(re.sub(r"[^a-z ^-]","",y))
                    else:
                        lis.put(re.sub(r"[^a-z]","",y))
                except IndexError:
                    ant = ""
                    for i in range(lis.qsize()):
                        m = lis.get()
                        if m != ant:
                            print(m)
                            ant = m
                    break
            break
    
proceso()