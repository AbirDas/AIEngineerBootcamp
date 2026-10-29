for value in range(1,11):
    print(f"Number: {value} ")
    
print()
    
my_list = []
for value in range(10):
    value *= 2;
    my_list.append(value)
print(f"My list Number: {my_list}")

print()

max_num = max(my_list)
print("Maximum number:",max_num) 
min_num = min(my_list)
print("Minimum number:", min_num)
sum_total = sum(my_list)
print("Sum total:",sum_total)
 
print()
 
even_nums = list(range(0, 100, 2))
print(even_nums)