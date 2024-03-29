import xlsxwriter as xw  # 导入 xlsxwriter 模块，用于创建 Excel 文件
import Kernel.GraphBuffer as GB  # 导入 GraphBuffer 模块，用于获取数据


def xw_to_excel(data, filename):
    n = GB.MAX_NODE_SIZES  # 获取最大节点数量
    m = GB.MAX_NODE_SIZES  # 获取最大节点数量
    col_num = []  # 创建一个空列表，用于存储列号
    for i in range(1, m + 1):  # 循环遍历从1到最大节点数量的范围
        col_num.append(str(i))  # 将当前列号转换为字符串并添加到列表中
    workbook = xw.Workbook(filename)  # 创建一个 Excel 工作簿对象
    worksheet1 = workbook.add_worksheet('sheet1')  # 在工作簿中添加一个名为 'sheet1' 的工作表
    worksheet1.activate()  # 激活 'sheet1' 工作表
    title = ['Generated Graph'] + col_num  # 创建标题行，包含 'Generated Graph' 和列号
    worksheet1.write_row('A1', title)  # 在 'A1' 单元格写入标题行
    i = 2
    for j in range(n):  # 循环遍历每一行数据
        row = 'A' + str(i)  # 获取当前行的行号
        worksheet1.write_row(row, [str(i - 1)] + data[i - 1][1:m + 1])  # 在当前行写入数据
        i += 1
    workbook.close()  # 关闭 Excel 工作簿对象，保存文件
