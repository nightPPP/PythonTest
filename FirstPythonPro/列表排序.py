name_list = ["aaa", "bbb", "cc"]
num_list = [2,4,1,5,3]

name_list.sort();
print(name_list)

num_list.sort()
print(num_list)

name_list.sort(reverse=True)
print(name_list)

num_list.sort(reverse=True)
print(num_list)

name_list.reverse()
print(name_list)

num_list.reverse()
print(num_list)

import keyword
print(keyword.kwlist)