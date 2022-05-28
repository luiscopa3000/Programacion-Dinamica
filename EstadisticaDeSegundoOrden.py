from queue import PriorityQueue


def proceso():
    n = int(input())
    temp = list(map(int, input().split()))
    num = PriorityQueue()
    for i in range(n):
        if temp[i] not in num.queue:
            num.put(temp[i])
    num.get()
    if not num.empty():
        print(num.get())
    else:
        print("NO")
def main():
    t = int (input())
    for i in range(t):
        proceso()
main()