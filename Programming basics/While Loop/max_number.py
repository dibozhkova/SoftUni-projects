import sys

num = input()

max_num = -sys.maxsize
while num != "Stop":
    copy_num = int(num)
    if copy_num > max_num:
        max_num = copy_num
    num = input()
print(max_num)
