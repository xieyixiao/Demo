sequence = [1, 3, 4, 5, 4, 3, 8, 9, 9, ]
s = len(sequence) - 1
k = 0
if sequence[0] > sequence[1]:
    sequence[0] = sequence[1]
    k += 1
for i in range(1, s + 1):
    if sequence[i] < sequence[i - 1]:
        sequence[i] = sequence[i - 1]
        k += 1
if k <= 1:
    print("True")
else:
    print("False")
