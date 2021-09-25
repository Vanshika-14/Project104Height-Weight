import csv

with open('Dataset.csv', newline = '') as f:
   reader = csv.reader(f)
   fileData = list(reader)

# Remove header while reading data
fileData.pop(0)

newData = []

# ### HEIGHT
# # FOR I IN RANGE => for each
# # len => length
# for i in range(len(fileData)):
#    n_num = fileData[i][1]
#    newData.append(float(n_num))

# ### WEIGHT
# FOR I IN RANGE => for each
# len => length
for i in range(len(fileData)):
   n_num = fileData[i][2]
   newData.append(float(n_num))

# MEDIAN
n = len(newData)
newData.sort()

if n % 2 == 0:
   median1 = float(newData[n//2])
   median2 = float(newData[n//2-1])
   median = (median1 + median2)/2
else:
   median = newData[n//2]

print("The median is " + str(median))