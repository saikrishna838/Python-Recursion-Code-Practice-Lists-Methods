numbers_list = input().split(",")

largest_frequency = 0
mode = 0

for number in numbers_list:
    each_frequency = numbers_list.count(number)
    if each_frequency > largest_frequency:
        largest_frequency = each_frequency
        mode = number
        
print(mode)