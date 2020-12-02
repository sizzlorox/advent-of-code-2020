import os
import re

file_path = os.path.dirname(os.path.realpath(__file__))
inputs = []
with open(os.path.join(file_path, 'inputs.txt')) as my_file:
    for line in my_file:
        inputs.append(re.sub(r'\n', '', line))

# PART ONE
solved = 0
for v in inputs:
  amount_data = re.findall(r'(\d+)', v)
  str_data = re.findall(r'(\S):', v)
  match_data = re.findall(r': (\S+)', v)

  letter = str_data[0]
  min = int(amount_data[0])
  max = int(amount_data[1])

  count = len(re.findall(rf'{letter}', match_data[0]))
  if min <= count <= max:
    solved += 1

print(solved)

# PART TWO
solved = 0
for v in inputs:
  amount_data = re.findall(r'(\d+)', v)
  str_data = re.findall(r'(\S):', v)
  match_data = re.findall(r': (\S+)', v)

  letter = str_data[0]
  first_index = int(amount_data[0]) - 1
  second_index = int(amount_data[1]) - 1

  letters = re.findall(r'\S', match_data[0])
  if letters[first_index] is not letter and letters[second_index] is not letter:
    continue
  if letters[first_index] is letter and letters[second_index] is letter:
    continue

  solved += 1

print(solved)
