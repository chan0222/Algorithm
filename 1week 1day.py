n = int(input())

for i in range(1,n+1): 
    a = list(str(i))
    if i + sum(map(int,a)) == n:
        print(i)
        break
    if i == n:
        print(0)