import xlrd

# 读取单元格的值
# 下面的是复制过来的路径，是不对的，要把斜杠改成这样的‘/’，键盘上问号的那个键的斜杠
# xlsx = xlrd.open_workbook('C:\Users\Administrator\Desktop\pythonTest.xlsx')

xlsx = xlrd.open_workbook('C:/Users/Administrator/Desktop/pythonTest.xlsx')
table = xlsx.sheet_by_index(0)

# 方法一
# table.cell_value(a, b)
#   a 代表哪一行（减1）
#   b 代表那一列（减1）
print("用table.cell_value=== %s" %table.cell_value(4, 0))

# 方法二
print(table.cell(4, 0).value)

# 方法三
print(table.row(4)[0].value)

# 获取某一行的所有值 得到的是一个列表
print(table.row_values(0))




