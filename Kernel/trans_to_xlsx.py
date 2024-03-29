import xlsxwriter as xw
import Kernel.DirectedGraph as DAG
import Kernel.UndirectedGraph as UDG
import Kernel.GraphBuffer as GB


def xw_to_excel(data, filename):
    n = GB.MAX_NODE_SIZES
    m = GB.MAX_NODE_SIZES
    col_num = []
    for i in range(1, m + 1):
        col_num.append(str(i))
    workbook = xw.Workbook(filename)
    worksheet1 = workbook.add_worksheet('sheet1')
    worksheet1.activate()  # 表已经激活
    title = ['Generated Graph'] + col_num
    worksheet1.write_row('A1', title)  # 表示开始位置,横向顺延
    i = 2
    for j in range(n):  # 这个参数放的是行
        row = 'A' + str(i)
        worksheet1.write_row(row, [str(i - 1)] + data[i - 1][1:m + 1])
        i += 1
    workbook.close()
