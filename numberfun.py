N = int(input())

for i in range(N):
    answer = "Impossible"
    a,b,c = map(int, input().split())
    
    if a + b == c or a - b == c or b - a == c or a * b == c or a / b == c or b / a == c:
        answer = "Possible"
        
    print(answer)
