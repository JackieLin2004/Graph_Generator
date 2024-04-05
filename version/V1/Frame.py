import sys  # 导入 sys 模块，用于系统相关操作

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage, QGuiApplication
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QHeaderView
from generator_ui import Ui_Form  # 导入自动生成的界面文件中的 Ui_Form 类
import version.V1.Kernel.DirectedGraph as DAG
import version.V1.Kernel.UndirectedGraph as UDG
import version.V1.Kernel.trans_to_xlsx as xlsx_writer
import version.V1.Kernel.GraphBuffer as GB
import version.V1.Kernel.GraphUtils as Utils
from qt_material import apply_stylesheet  # 导入 qt_material 模块中的 apply_stylesheet 函数，用于美化界面


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 窗口标题
        self.setWindowTitle("Graph Generator")

        # 获取当前窗口的大小
        self.screen = QGuiApplication.primaryScreen().geometry()
        # 把窗口的大小赋值给宽高
        self.width, self.height = self.screen.width(), self.screen.height()
        # 重新调整窗口大小
        self.resize(self.width, self.height - 80)
        # 校准，距离屏幕左上角的位置
        self.move(0, 0)

        # 设置为全屏
        # self.showFullScreen()

        # 输入结点和边数的文本框默认显示0
        self.node_num.setPlaceholderText('0')
        self.edge_num.setPlaceholderText('0')
        # 设置边列表的列数为3，即u，v，w 三列
        self.edgelistframe.setColumnCount(3)
        self.titles = ['u', 'v', 'w']
        # 设置边列表的表头标题，即u，v，w
        self.edgelistframe.setHorizontalHeaderLabels(self.titles)

        # 初始化表格行索引
        self.tableIndex = 0
        # 设置视图中的图像居中显示
        self.view.setAlignment(Qt.AlignCenter)
        # 初始化图类型，默认为无向图
        self.Gtype = 0
        # 设置无向图按钮默认选中
        self.btn_UDG.setChecked(True)
        # 设置边列表的表头自适应列宽
        self.edgelistframe.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # 设置矩阵表格的表头自适应列宽
        self.matrixTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        # 绑定信号和槽
        self.bind()

    # 绑定函数，统一绑定所有事件
    def bind(self):
        # 绑定生成按钮点击事件
        self.btn_generate.clicked.connect(lambda: self.generate())
        # 绑定添加边按钮点击事件
        self.btn_addEdge.clicked.connect(lambda: self.addEdge())
        # 绑定删除边按钮点击事件
        self.btn_delEdge.clicked.connect(lambda: self.delEdge())
        # 绑定确认图按钮点击事件
        self.btn_confirm.clicked.connect(lambda: self.confirmGraph())
        # 绑定无向图按钮点击事件
        self.btn_UDG.clicked.connect(lambda: self.changeType(0))
        # 绑定有向图按钮点击事件
        self.btn_DAG.clicked.connect(lambda: self.changeType(1))
        # 绑定快速生成按钮点击事件
        self.btn_qspawn.clicked.connect(lambda: self.quickSpawn())
        # 绑定退出按钮点击事件
        self.btn_exit.clicked.connect(lambda: self.exit())

    def generate(self):
        # 如果选择无向图
        if self.Gtype == 0:
            UDG.Generate_UndirectedGraph()
            self.showPicture()
            xlsx_writer.xw_to_excel(UDG.matrix, f'./xlsx/UndirectedGraph/xlsx_{UDG.timestamp}.xlsx')
            self.showMatrixTable()
        # 如果选择有向图
        else:
            DAG.Generate_DirectedGraph()
            self.showPicture()
            xlsx_writer.xw_to_excel(DAG.matrix, f'./xlsx/DirectedGraph/xlsx_{DAG.timestamp}.xlsx')
            self.showMatrixTable()

    # 有可能是已经生成了，重新改了再生成，所以要先清空
    def confirmGraph(self):
        # 清除节点矩阵表格的行
        for i in range(GB.MAX_NODE_SIZES, -1, -1):
            self.matrixTable.removeRow(i)
        # 清除节点矩阵表格的列
        for i in range(GB.MAX_NODE_SIZES, -1, -1):
            self.matrixTable.removeColumn(i)
        # 清除边列表中的行
        for i in range(self.tableIndex, 0, -1):
            self.edgelistframe.removeRow(i - 1)

        # 获取节点数输入框的值，如果为空则设置最大节点数量为0
        if self.node_num.text() == '':
            GB.MAX_NODE_SIZES = 0
        else:
            GB.MAX_NODE_SIZES = int(self.node_num.text())
        # 清空边缓存
        GB.edges_buffer = []
        # 重置表格行索引
        self.tableIndex = 0

    def addEdge(self):
        # e是一个有uvw值的三元组
        e = Utils.random_edges()
        # 获取的三元组放进buffer
        GB.edges_buffer.append(e)
        # 创建 QTableWidgetItem 对象，并设置文本
        col1 = QTableWidgetItem(str(e[0]))
        col2 = QTableWidgetItem(str(e[1]))
        col3 = QTableWidgetItem(str(e[2]))
        # 在边列表末尾插入一行
        self.edgelistframe.insertRow(int(self.edgelistframe.rowCount()))
        # 设置边列表中当前行的项
        self.edgelistframe.setItem(self.tableIndex, 0, col1)
        self.edgelistframe.setItem(self.tableIndex, 1, col2)
        self.edgelistframe.setItem(self.tableIndex, 2, col3)
        self.tableIndex += 1

    def delEdge(self):
        # 如果边缓存为空，则返回
        if not GB.edges_buffer:
            return
        # 移除边列表中的最后一行
        self.edgelistframe.removeRow(self.tableIndex - 1)
        self.tableIndex -= 1
        # 移除边缓存中的最后一项
        GB.edges_buffer.pop()

    def showPicture(self):
        if self.Gtype == 0:
            img = QImage(f"./images/UndirectedGraph/UDG_{UDG.timestamp}")
            # 将 QImage 转换为 QPixmap,会更清晰一些
            pixmap = QPixmap.fromImage(img)
            # 在视图中显示图像
            self.view.setPixmap(pixmap)
        else:
            img = QImage(f"./images/DirectedGraph/DAG_{DAG.timestamp}")
            # 将 QImage 转换为 QPixmap,会更清晰一些
            pixmap = QPixmap.fromImage(img)
            # 在视图中显示图像
            self.view.setPixmap(pixmap)

    def showMatrixTable(self):
        # 设置矩阵表格的行数
        self.matrixTable.setRowCount(GB.MAX_NODE_SIZES)
        # 设置矩阵表格的列数
        self.matrixTable.setColumnCount(GB.MAX_NODE_SIZES)
        # 清除矩阵表格内容
        self.clearMatrixTable()
        if self.Gtype == 0:
            for pack in GB.edges_buffer:
                # 在矩阵表格中设置对应的单元格，无向图为对称矩阵，需要设置两个
                self.matrixTable.setItem(pack[0] - 1, pack[1] - 1, QTableWidgetItem(str(pack[2])))
                self.matrixTable.setItem(pack[1] - 1, pack[0] - 1, QTableWidgetItem(str(pack[2])))
        else:
            for pack in GB.edges_buffer:
                # 在矩阵表格中设置对应的单元格
                self.matrixTable.setItem(pack[0] - 1, pack[1] - 1, QTableWidgetItem(str(pack[2])))

    def changeType(self, val):
        # 切换图类型为指定值
        self.Gtype = val

    # 不一个个加边，而是快速生成
    def quickSpawn(self):
        if self.edge_num.text() == '':
            GB.MAX_EDGE_SIZES = 0
        else:
            GB.MAX_EDGE_SIZES = int(self.edge_num.text())
        cnt = GB.MAX_EDGE_SIZES
        # 循环调用加边函数进行加边
        for i in range(cnt):
            self.addEdge()

    def clearMatrixTable(self):
        # 清除矩阵表格内容
        self.matrixTable.clear()

    def exit(self):
        # 关闭窗口
        self.close()


def run():
    # 创建应用程序对象
    app = QApplication([])
    # 应用主题样式
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    # apply_stylesheet(app, theme='light_lightgreen.xml')
    # 创建主窗口对象
    window = Frame()
    # 显示主窗口
    window.show()
    # 运行应用程序，直到应用程序退出
    sys.exit(app.exec_())
