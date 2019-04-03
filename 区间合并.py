element = [[1, 3], [2, 6], [8, 10], [15, 18], [0, 0]]
for j in range(0, len(element)):
    for i in range(j, len(element)-1):
        if element[j][0] in range(element[i+1][0], element[i+1][1]+1):
            if element[j][1] > element[i+1][1]:
                element[i+1][1] = element[j][1]
                element[j][0] = 0
                element[j][1] = 0
            else:
                element[j][0] = 0
                element[j][1] = 0
        elif element[j][1] in range(element[i+1][0], element[i+1][1]+1):
            if element[j][0] < element[i + 1][0]:
                element[i + 1][0] = element[j][0]
                element[j][0] = 0
                element[j][1] = 0
            else:
                element[j][0] = 0
                element[j][1] = 0
for j in range(0, len(element)):
    if element[j][0] != 0 and element[j][1] != 0:
        print(element[j])




















