from xlutils.copy import copy
import xlwt
import xlrd

"""style---字体font,  边框border，   对齐alignment"""
def writeData():
    # 打开文件
    # 文件的路径C:/Users/Administrator/Desktop/data.xls
    tem_excel = xlrd.open_workbook('C:/Users/Administrator/Desktop/data.xls', formatting_info=True)
    # 文件的表
    tem_sheet = tem_excel.sheet_by_index(0)

    # 复制文件
    new_excel = copy(tem_excel)
    # 在第一个表
    new_sheet = new_excel.get_sheet(0)

    # 初始化字体
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = '微软雅黑'
    font.bold = True
    font.height = 360
    style.font = font

    # 设置边框
    borders = xlwt.Borders()
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    style.borders = borders

    # 对齐
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment

    # 写入数据
    new_sheet.write(2, 1, 12, style)
    new_sheet.write(3, 1, 19, style)
    new_sheet.write(4, 1, 33, style)
    new_sheet.write(5, 1, 66, style)
    # 保存的位置
    new_excel.save('C:/Users/Administrator/Desktop/newData.xls')


if __name__ == '__main__':
    writeData()