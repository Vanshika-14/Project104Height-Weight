import csv

with open('Dataset.csv', newline = '') as f:
   reader = csv.reader(f)
   fileData = list(reader)

# Remove header while reading data
fileData.pop(0)

newData = []

### HEIGHT
# FOR I IN RANGE => for each
# len => length
for i in range(len(fileData)):
   n_num = fileData[i][1]
   newData.append(float(n_num))

# # ### WEIGHT
# # FOR I IN RANGE => for each
# # len => length
# for i in range(len(fileData)):
#    n_num = fileData[i][2]
#    newData.append(float(n_num))

# MEAN
n = len(newData)
total = 0
for x in newData:
   total = total + x
mean = total/n
print("The mean/average is " + str(mean))