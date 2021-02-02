# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(int(input())):
    answer = ""
    sentence = input().lower() # Ensure everything's in lowercase
    sentence = re.sub(r"\W","",sentence) #remove non-alphanumerical characters from string
    sentence = re.sub(r"\d","",sentence) # remove digits from string
    sentence = re.sub(r"_","",sentence) #remove uunderscore from string
    sentence = re.sub(r"/s","",sentence) #remove whitespace characters from string

    if len(set(sentence)) != len(alphabet):
        for j in alphabet: # Because alphabet is in alphabetical order, don't need to sort it
            if j not in sentence:
                answer += j

    if len(answer) == 0:
        print("pangram")
    else:
        print("missing","".join(answer))
