t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = sum(a)
    skip = min(a)
    print(total - skip)