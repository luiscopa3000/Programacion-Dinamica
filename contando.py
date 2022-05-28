def main(occ_a = {}, b = {}, c = {}):
    n = int (input())
    x = list(map(int, input().split()))
    for i in x:
        if i in occ_a:
            occ_a[i] += 1
        else:
            occ_a[i] = 1
    y = list(map(int, input().split()))
    for i in range(1,n+1):
        b[i] = y[i-1]
    z = list(map(int, input().split()))
    for i in range(1,n+1):
        c[i] = z[i-1]
    ans = 0
    for i in range(1,n+1):
        if c[i] in b and b[c[i]] in occ_a:
            ans = ans+occ_a[b[c[i]]]
    print(ans)
        
main()
    
    