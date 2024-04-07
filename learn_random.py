from random import randint as rdint 

a = rdint(100, 1000)

print("a = ", a)

str_a = str(a)
modified_str_a = str_a[0] + '0' + str_a[2:]

print(f"modified_str_a = {int(modified_str_a)}")
