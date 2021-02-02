# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
           'V', 'W', 'X', 'Y', 'Z']

input_text = input()

last_half = input_text[(int(len(input_text)/2)):]
first_half = input_text[:-(int(len(input_text)/2))]

rotate_1 = 0
rotate_2 = 0

for i in range(len(first_half)):
    rotate_1+=letters.index(first_half[i])
    rotate_2+=letters.index(last_half[i])
    
final = ''

for j in range(len(first_half)):
    final+= letters[(((letters.index(first_half[j]) + rotate_1) % 26 + 
                      (letters.index(last_half[j])  + rotate_2) % 26) % 26)]
                     
print(final)
