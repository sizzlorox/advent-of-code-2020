import os
import re

file_path = os.path.dirname(os.path.realpath(__file__))
inputs = []
with open(os.path.join(file_path, 'inputs.txt')) as my_file:
    for line in my_file:
        inputs.append(int(re.sub(r'\D+', '', line)))
solved = []

# PART ONE
for i, v in enumerate(inputs):
  for j, v2 in enumerate(inputs):
    sum = v + v2
    if sum == 2020:
      if v not in solved:
        solved.append(v)
      if v2 not in solved:
        solved.append(v2)

print(solved[0] * solved[1])
solved = []

# PART TWO
for i, v in enumerate(inputs):
  for j, v2 in enumerate(inputs):
    for k, v3 in enumerate(inputs):
      sum = v + v2 + v3
      if sum == 2020:
        if v not in solved:
          solved.append(v)
        if v2 not in solved:
          solved.append(v2)
        if v3 not in solved:
          solved.append(v3)

print(solved[0] * solved[1] * solved[2])
