#reconstructSentence.py take 2 arguments
#this program read 2 files that reverse and combine into 1 file
#argument 1 text file
#argument 2 text file
#.eg. python3 reconstructSentence.py input1.txt input2.txt

import sys

with open(sys.argv[1]) as f:
  list1 = f.readlines()

with open(sys.argv[2]) as f:
  list2 = f.readlines()

new_list1 = []
new_list2 = []

for i in range(len(list1)):
  new_list1.append(list1[i].split())

for i in range(len(list2)):
  new_list2.append(list2[i].split())

list1 = []
list2 = []

for i in range(len(new_list1)):
  list1.extend(new_list1[i])

for i in range(len(new_list2)):
  list2.extend(new_list2[i])

length1 = len(list1)
length2 = len(list2)
max_length = length1

if length1 > length2:
  max_length = length1
else:
  max_length = length2

new_list1 = []
new_list2 = []
for i in range(1,length1):
  new_list1.append(list1[-i])
new_list1.append(list1[0])

for i in range(1,length2):
  new_list2.append(list2[-i])
new_list2.append(list2[0])

out = []
for i in range(max_length):
  if length1 > 0:
    out.append(new_list1[i])
    length1 -= 1
  if length2 > 0:
    out.append(new_list2[i])
    length2 -= 1

with open('output.txt', "w") as f:
  for i in out:
    f.write(i + " ")





