def find_hex_value(line, answer):
    for element in line[2:]:
        if element.isnumeric() or element == 'A' or element == 'B' or element == 'C' or element == 'D' or element == 'E' or element == 'F' or element == 'a' or element == 'b' or element == 'c' or element == 'd' or element == 'e' or element == 'f':
            answer += element
        else:
            break
    answer = "".join(answer)
    line = line[len(answer):]

    return line, answer

while True:
    row = input()
    while "0x" in row.lower():
        answer = list()

        if "0x" in row:
            location = row.find("0x")
            answer = "0x"
            row = row[location:]
            row, answer = find_hex_value(row, answer)
            
        elif "0X" in row:
            location = row.find("0X")
            answer = "0X"
            row = row[location:]
            row, answer = find_hex_value(row, answer)

        # Prints a line containing the hex number as it appeared in the input
        # and its non-negative decimal equivalent - int() can convert hex to
        # decimal (which starts at string's index 2 and must be uppercase)

        print(answer, int(answer.upper()[2:], 16))
