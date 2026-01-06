L = ["5", "7", "Rohit", "Virat", "Dhoni"]
string = input()

list_a = L
list_b = string.split(" ")

list_a.extend(list_b)
print(list_a)
