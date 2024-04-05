import xlsxwriter as xw  # 导入 xlsxwriter 模块，用于创建 Excel 文件
import version.V1.Kernel.GraphBuffer as GB  # 导入 GraphBuffer 模块，用于获取数据


def xw_to_excel(data, filename):
    # n，m分别获取最大节点数量
    n = GB.MAX_NODE_SIZES
    m = GB.MAX_NODE_SIZES

    # 创建一个空列表，用于存储列号
    col_num = []
    for i in range(1, m + 1):
        # 将当前列号转换为字符串并添加到列表中
        col_num.append(str(i))

    # 创建一个 Excel 工作簿对象
    workbook = xw.Workbook(filename)
    # 在工作簿中添加一个名为 'sheet1' 的工作表
    worksheet1 = workbook.add_worksheet('sheet1')
    # 激活 'sheet1' 工作表
    worksheet1.activate()

    # 创建标题行，包含 'Generated Graph' 和列号
    title = ['Generated Graph'] + col_num
    # 在 'A1' 单元格写入标题行
    worksheet1.write_row('A1', title)

    i = 2
    # 遍历每一行，从1到n
    for j in range(n):
        # 获取当前行的行号，从A2开始
        row = 'A' + str(i)
        # 在当前行写入数据
        worksheet1.write_row(row, [str(i - 1)] + data[i - 1][1:m + 1])
        i += 1

    # 关闭 Excel 工作簿对象，保存文件
    workbook.close()
