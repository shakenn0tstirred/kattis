for _ in range(int(input())):
    word1 = input()
    word2 = input()
    answer = ""
    
    for i,j in enumerate(word1): # Compare each character, one at a time
        if j == word2[i]:
            answer += "."
        else:
            answer += "*"

    print(word1)
    print(word2)
    print(answer)
    print("") # Print empty line
