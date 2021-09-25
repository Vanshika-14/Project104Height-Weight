import csv
from collections import Counter

with open('Dataset.csv', newline = '') as f:
   reader = csv.reader(f)
   fileData = list(reader)

# Remove header while reading data
fileData.pop(0)

newData = []

# # FOR I IN RANGE => for each
# # len => length
# for i in range(len(fileData)):
#    n_num = fileData[i][1]
#    newData.append(float(n_num))

# # MODE
# data = Counter(newData)
# modeDataForRange = {
#    "50-60":0,
#    "60-70":0,
#    "70-80":0
# }

# for height, occurence in data.items():
#    if 50 < float(height) < 60:
#       modeDataForRange["50-60"] += occurence
#    elif 60 < float(height) < 70:
#       modeDataForRange["60-70"] += occurence
#    elif 70 < float(height) < 80:
#       modeDataForRange["70-80"] += occurence




# FOR I IN RANGE => for each
# len => length
for i in range(len(fileData)):
   n_num = fileData[i][2]
   newData.append(float(n_num))

# MODE
data = Counter(newData)
modeDataForRange = {
   "100-110":0,
   "110-120":0,
   "120-130":0
}

for height, occurence in data.items():
   if 100 < float(height) < 110:
      modeDataForRange["100-110"] += occurence
   elif 110 < float(height) < 120:
      modeDataForRange["110-120"] += occurence
   elif 120 < float(height) < 130:
      modeDataForRange["120-130"] += occurence




modeRange, modeOccurence = 0, 0
for range, occurence in modeDataForRange.items():
    if occurence > modeOccurence:
        modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((modeRange[0] + modeRange[1]) / 2)
print(f"Mode is: {mode:2f}")