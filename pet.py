  # This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

scores = list()

for i in range(5):
  score = sum(list(map(int, input().split())))
  scores.append([score, i+1])

scores.sort(reverse = True)

print(scores[0][1],scores[0][0])
