import xlsxwriter as xw


class XlsxWriter:
    def __init__(self):
        self.col_num = []

    def xw_to_excel(self, data, filename, graph):
        n = graph.MAX_NODE_SIZES
        m = graph.MAX_NODE_SIZES
        self.col_num = []
        for i in range(1, m + 1):
            self.col_num.append(str(i))
        workbook = xw.Workbook(filename)
        worksheet1 = workbook.add_worksheet('sheet1')
        worksheet1.activate()  # 表已经激活
        title = ['Generated Graph'] + self.col_num
        worksheet1.write_row('A1', title)  # 表示开始位置,横向顺延
        i = 2
        for j in range(n):  # 这个参数放的是行
            row = 'A' + str(i)
            worksheet1.write_row(row, [str(i - 1)] + data[i - 1][1:m + 1])
            i += 1
        workbook.close()
