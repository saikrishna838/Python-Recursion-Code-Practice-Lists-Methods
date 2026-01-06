list_a = [5, 4, 10, 2, 3, 2, 5, 15, 4, 4]
number = int(input())
indices = []

for index in range(len(list_a)):
    if number == list_a[index]:
        indices.append(str(index))
print(" ".join(indices))


