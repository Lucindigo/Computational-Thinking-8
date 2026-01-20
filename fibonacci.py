import math
num_1 = 1
num_2 = 1

nums_calculated = 0
target_num = input ("what fibonacci number do you want calculated: ")
target_num = int(target_num)
while nums_calculated < target_num:
    num_1 += num_2
    nums_calculated += 1
    num_2 += num_1
    nums_calculated += 1
else:
    print (f"you got {num_2} as your fibonacci number")
    print (f"test {nums_calculated}")