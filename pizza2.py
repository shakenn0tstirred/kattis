# Since pi cancels itself out, I don't use it in this program.

R,C = map(int, input().split())

if R == C:
   print(0)
else:
   answer = (R - C)**2
   answer /= R**2
   print(answer*100)
