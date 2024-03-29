import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsScene, QTableWidgetItem, QHeaderView
from generator_ui import Ui_Form
import Kernel.DirectedGraph as DAG
import Kernel.UndirectedGraph as UDG
import Kernel.trans_to_xlsx as xlsx_writer
import Kernel.GraphBuffer as GB
import Kernel.GraphUtils as Utils
from qt_material import apply_stylesheet


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Graph Generator")
        self.showFullScreen()
        self.node_num.setPlaceholderText('0')
        self.edge_num.setPlaceholderText('0')
        self.edgelistframe.setColumnCount(3)
        self.titles = ['u', 'v', 'w']
        self.edgelistframe.setHorizontalHeaderLabels(self.titles)
        self.tableIndex = 0
        self.view.setAlignment(Qt.AlignCenter)
        self.Gtype = 0
        self.btn_UDG.setChecked(True)
        self.edgelistframe.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.matrixTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.bind()

    def bind(self):
        self.btn_generate.clicked.connect(lambda: self.generate())
        self.btn_addEdge.clicked.connect(lambda: self.addEdge())
        self.btn_delEdge.clicked.connect(lambda: self.delEdge())
        self.btn_confirm.clicked.connect(lambda: self.confirmGraph())
        self.btn_UDG.clicked.connect(lambda: self.changeType(0))
        self.btn_DAG.clicked.connect(lambda: self.changeType(1))
        self.btn_qspawn.clicked.connect(lambda: self.quickSpawn())
        self.btn_exit.clicked.connect(lambda: self.exit())

    def generate(self):
        if self.Gtype == 0:
            UDG.Generate_UndirectedGraph()
            self.showPic()
            xlsx_writer.xw_to_excel(UDG.matrix, f'./xlsx/UndirectedGraph/xlsx_{UDG.timestamp}.xlsx')
            self.showMatrixTable()
        else:
            DAG.Generate_DirectedGraph()
            self.showPic()
            xlsx_writer.xw_to_excel(DAG.matrix, f'./xlsx/DirectedGraph/xlsx_{DAG.timestamp}.xlsx')
            self.showMatrixTable()

    def confirmGraph(self):
        for i in range(GB.MAX_NODE_SIZES, -1, -1):
            self.matrixTable.removeRow(i)
        for i in range(GB.MAX_NODE_SIZES, -1, -1):
            self.matrixTable.removeColumn(i)
        for i in range(self.tableIndex, 0, -1):
            self.edgelistframe.removeRow(i - 1)

        if self.node_num.text() == '':
            GB.MAX_NODE_SIZES = 0
        else:
            GB.MAX_NODE_SIZES = int(self.node_num.text())

        GB.edges_buffer = []
        self.tableIndex = 0

    def addEdge(self):
        e = Utils.random_edges()
        GB.edges_buffer.append(e)
        col1 = QTableWidgetItem(str(e[0]))
        col2 = QTableWidgetItem(str(e[1]))
        col3 = QTableWidgetItem(str(e[2]))
        self.edgelistframe.insertRow(int(self.edgelistframe.rowCount()))
        self.edgelistframe.setItem(self.tableIndex, 0, col1)
        self.edgelistframe.setItem(self.tableIndex, 1, col2)
        self.edgelistframe.setItem(self.tableIndex, 2, col3)
        self.tableIndex += 1

    def delEdge(self):
        if not GB.edges_buffer:
            return
        self.edgelistframe.removeRow(self.tableIndex - 1)
        self.tableIndex -= 1
        GB.edges_buffer.pop()

    def showPic(self):
        if self.Gtype == 0:
            img = QImage(f"./images/UndirectedGraph/UDG_{UDG.timestamp}")
            pixmap = QPixmap.fromImage(img)
            self.view.setPixmap(pixmap)
        else:
            img = QImage(f"./images/DirectedGraph/DAG_{DAG.timestamp}")
            pixmap = QPixmap.fromImage(img)
            self.view.setPixmap(pixmap)

    def showMatrixTable(self):
        self.matrixTable.setRowCount(GB.MAX_NODE_SIZES)
        self.matrixTable.setColumnCount(GB.MAX_NODE_SIZES)
        self.clearMatrixTable()
        if self.Gtype == 0:
            for pack in GB.edges_buffer:
                self.matrixTable.setItem(pack[0] - 1, pack[1] - 1, QTableWidgetItem(str(pack[2])))
                self.matrixTable.setItem(pack[1] - 1, pack[0] - 1, QTableWidgetItem(str(pack[2])))
        else:
            for pack in GB.edges_buffer:
                self.matrixTable.setItem(pack[0] - 1, pack[1] - 1, QTableWidgetItem(str(pack[2])))

    def changeType(self, val):
        self.Gtype = val

    def quickSpawn(self):
        if self.edge_num.text() == '':
            GB.MAX_EDGE_SIZES = 0
        else:
            GB.MAX_EDGE_SIZES = int(self.edge_num.text())
        cnt = GB.MAX_EDGE_SIZES
        for i in range(cnt):
            self.addEdge()

    def clearMatrixTable(self):
        self.matrixTable.clear()

    def exit(self):
        self.close()


def run():
    app = QApplication([])
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    window = Frame()
    window.show()
    sys.exit(app.exec_())
