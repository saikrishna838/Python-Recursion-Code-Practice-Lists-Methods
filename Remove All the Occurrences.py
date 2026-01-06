nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
n = int(input())
count = nums_list.count(n)

for num in range(count):
    if n in nums_list:
        nums_list.remove(n)
        
print(nums_list)
        
