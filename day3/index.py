import os
import re
from functools import reduce

file_path = os.path.dirname(os.path.realpath(__file__))
inputs = []
with open(os.path.join(file_path, 'inputs.txt')) as my_file:
    for line in my_file:
        inputs.append(re.sub(r'\n', '', line))

# PART ONE
tree_count = 0

for i, v in enumerate(inputs):
  if i >= len(inputs) - 1:
    break
  is_tree = inputs[i + 1][3 * (i + 1) % len(inputs[i])] == '#'
  if is_tree:
    tree_count += 1

print(tree_count)

# PART TWO
def slope_dir(right, down):
  tree_count = 0
  for i, v in enumerate(inputs):
    if down == 1 and i >= len(inputs) - 1:
      break
    if down != 1 and (i + 1) * down > len(inputs) - 1:
      break
    if down != 1:
      print(i * down, right * (i + 1) % len(inputs[i]))
    is_tree = inputs[(i + 1) * down][right * (i + 1) % len(inputs[i])] == '#'
    if is_tree:
      tree_count += 1

  print(right, down, tree_count)
  return tree_count

questions = [
  { "right": 1, "down": 1 },
  { "right": 3, "down": 1 },
  { "right": 5, "down": 1 },
  { "right": 7, "down": 1 },
  { "right": 1, "down": 2 },
]

answers = []
for question in questions:
  answer = slope_dir(question["right"], question["down"])
  answers.append(answer)

total = reduce(lambda a, b: a * b, answers)

print(total, answers)
