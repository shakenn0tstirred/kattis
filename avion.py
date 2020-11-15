answer = ""


if "FBI" in input():
    answer += "1"
if "FBI" in input():
    answer += "2"
if "FBI" in input():
    answer += "3"
if "FBI" in input():
    answer += "4"
if "FBI" in input():
    answer += "5"

if len(answer) != 0:
    print(" ".join(answer))
else:
    print("HE GOT AWAY!")
