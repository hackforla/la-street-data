import re

with open('streetsweepingdata.csv', 'r') as fileData:
    read_data = fileData.readlines()

read_data = read_data[1:]
read_lines_split = []
for line in read_data:
    newStreets = []
    splitLine = line.strip().split(",", 4)
    print(splitLine)
    a = re.split("[ ]+(?:[,\=\-/\&]|to)[ ]+", splitLine[4].strip("\""), flags=re.IGNORECASE)
    for element1 in a:
        b = re.split("(?<=bl)\.([ a-zA-Z])", element1, flags=re.IGNORECASE)
        for element2 in b:
            if element2.strip() == "":
                continue
            newStreets.append(element2.strip())
            if len(newStreets) > 4:
                print("newStreets >4:"+str(newStreets) + " for line: "+splitLine[0])
    read_lines_split.append(splitLine[0:4]+[newStreets])  # remember slice range in python is end - 1
print(read_lines_split)



