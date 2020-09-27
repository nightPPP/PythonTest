num_str = "0123456789"

# 从索引2到索引5
print(num_str[2:5])

# 从索引2开始到最后
print(num_str[2:])

# 从索引0到索引6
print(num_str[:6])

# 步长
# 从索引0开始，步长2---隔一个取一个
print(num_str[::2])

# 从索引1开始，步长2----隔一个取一个
print(num_str[1::2])

# 索引2到倒数第一个索引
print(num_str[2:-1])

# 截取最后2个
print(num_str[-2:])

# 逆序
print(num_str[::-1])
print(num_str[-1::-1])