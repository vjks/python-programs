T = int(input())

for x in range(T):
    a, b, c = map(int, input().split())
    if (a + b) / 2 > c: 
        print("YES");
    else:
        print("NO");