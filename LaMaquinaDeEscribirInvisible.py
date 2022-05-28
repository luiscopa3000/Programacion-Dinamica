def main():
    casos = int(input())
    for i in range(casos):
        entrada = input()
        x = -1;y = -1; z = -1
        acu = 10**9
        for j in range(len(entrada)):
            if entrada[j] == '1':
                x = j
            elif entrada[j] == '2':
                y = j
            else:
                z = j
            if x != -1 and y != -1 and z != -1:
                cur = max(x, max(y, z))- min(x, min(y, z))+1
                acu = min(acu, cur)
        if acu == 10**9:
            print("0")
        else:
            print(acu)
main()
        