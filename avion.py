first  = input()
second = input()
third  = input()
forth  = input()
fifth  = input()
answer = ""


if "FBI" in first:
    answer += "1"
if "FBI" in second:
    answer += "2"
if "FBI" in third:
    answer += "3"
if "FBI" in forth:
    answer += "4"
if "FBI" in fifth:
    answer += "5"

if len(answer) != 0:
    print(" ".join(answer))
else:
    print("HE GOT AWAY!")
