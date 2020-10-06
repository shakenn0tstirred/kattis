coded_sentence = input().split()
uncoded_sentence = []
answer = []
vowels = "aeiou"

for i in range(len(coded_sentence)):
    for j,k in enumerate(coded_sentence[i]):
        if k in vowels:
            coded_sentence[i] = coded_sentence[i][:j+1] + coded_sentence[i][j+3:]
            j += 2
    answer.append(coded_sentence[i])

print(" ".join(answer))
