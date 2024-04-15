import os
import sys
import time

from PySide6.QtCore import Qt, QUrl, QPropertyAnimation, QThread, Signal
from PySide6.QtGui import QPixmap, QImage, QGuiApplication
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QHeaderView

import PaperLauncher
from generator_ui import Ui_Form
import Kernel.DirectedGraph as DAG
import Kernel.UndirectedGraph as UDG
import Kernel.trans_to_xlsx as xlsx_writer
import Kernel.GraphBuffer as GB
import Kernel.GraphUtils as Utils
import Kernel.DrawChart as DC
import Kernel.PageRank as PG
import Kernel.ShortestPath as Algo
import HLMLauncher
import multiprocessing
import Thesis.Matrix as PMat
from qt_material import apply_stylesheet


class Frame(QWidget, Ui_Form, multiprocessing.Process):
    glob = Signal(int)
    globPaper = Signal(int)

    def __init__(self):
        super().__init__()
        self.paperThread = None
        self.paperLauncher = None
        self.hlmThread = None
        self.hlmlauncher = None
        self.footerAnima = None
        self.sidebarAnima = None
        self.setupUi(self)
        self.setWindowTitle("Graph Generator")
        self.screen = QGuiApplication.primaryScreen().geometry()
        self.width, self.height = self.screen.width(), self.screen.height()
        self.resize(self.width, self.height - 80)
        self.move(0, 0)
        # self.showFullScreen()
        self.node_num.setPlaceholderText('0')
        self.edge_num.setPlaceholderText('0')
        self.start_point.setPlaceholderText('start point of the shortest path')
        self.end_point.setPlaceholderText('end point of the shortest path')
        self.edgelistframe.setColumnCount(3)
        self.edgelistframe.setHorizontalHeaderLabels(['u', 'v', 'w'])
        self.PRtable.setColumnCount(2)
        self.PRtable.setHorizontalHeaderLabels(['id', 'PR'])
        self.PageRankView.setColumnCount(2)
        self.PageRankView.setHorizontalHeaderLabels(['id', 'PR'])
        self.tableIndex = 0
        self.PR_tableIndex = 0
        self.PaperPR_tableIndex = 0
        self.view.setAlignment(Qt.AlignCenter)
        self.relationView.setAlignment(Qt.AlignCenter)
        self.btn_UDG.setChecked(True)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.PaperTable.setCurrentIndex(0)
        self.KGtabs.setCurrentIndex(0)
        self.edgelistframe.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.matrixTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.PRtable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.PageRankView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.progressBar.setValue(0)
        self.graph = GB.GraphBuffer()
        self.UDGgen = UDG.UDGgenerator()
        self.DAGgen = DAG.DAGgenerator()
        self.pageR = PG.PageRank()
        self.HLMprogressbar.setValue(0)
        self.PaperprogressBar.setValue(0)
        self.HLMmaskinmask.hide()
        self.papermaskinmask.hide()
        self.Xwriter = xlsx_writer.XlsxWriter()
        self.cur = 1
        self.KGtabs.hide()
        self.PaperTable.hide()
        self.footer.setStyleSheet("QWidget{border-top:1px solid gray;}")
        self.progressBar.setStyleSheet("QProgressBar{border:none;}")
        self.setStyleSheet("QWidget {background-color:white;}")
        self.bindComboBox()
        self.edgelistframe.setStyleSheet(
            "QHeaderView::section {background-color:white; border-color: darkgray;color: black;}")
        self.matrixTable.setStyleSheet(
            "QHeaderView::section {background-color:white; border-color: darkgray;color: black;}")
        self.PageRankView.setStyleSheet(
            "QHeaderView::section {background-color:white; border-color: darkgray;color: black;}")
        self.groupBox.setStyleSheet("QGroupBox:title{color:black;} QGroupBox{border-color:lightgray;}")
        self.webEngineView.setUrl('http://localhost:7474/browser')
        self.PaperKGView.setUrl('http://localhost:7474/browser')

        self.bind()

    # 绑定函数
    def bind(self):
        self.btn_generate.clicked.connect(lambda: self.generate())
        self.btn_addEdge.clicked.connect(lambda: self.addEdge())
        self.btn_delEdge.clicked.connect(lambda: self.delEdge())
        self.btn_confirm.clicked.connect(lambda: self.confirmGraph())
        self.btn_UDG.clicked.connect(lambda: self.changeType(0))
        self.btn_DAG.clicked.connect(lambda: self.changeType(1))
        self.btn_qspawn.clicked.connect(lambda: self.quickSpawn())
        self.btn_exit.clicked.connect(lambda: self.exit())
        self.btn_runSP.clicked.connect(lambda: self.runSPFA())
        self.btn_nw.clicked.connect(lambda: self.turnNeg())
        self.btn_activHLM.clicked.connect(lambda: self.activateHLM())
        self.btn_activPaper.clicked.connect(lambda: self.activatePaper())
        self.tabWidget.currentChanged['int'].connect(self.sideBarChange)
        self.btn_search.clicked.connect(lambda: self.showRelationship())

    def generate(self):
        self.clearPRTable()
        if self.graph.Gtype == 0:
            self.progressBar.setValue(10)
            self.UDGgen.Generate_UndirectedGraph(self.graph)
            self.progressBar.setValue(40)
            self.showPic()
            self.progressBar.setValue(60)
            self.Xwriter.xw_to_excel(self.graph.matrix, f'./xlsx/UndirectedGraph/xlsx_{self.UDGgen.timestamp}.xlsx',
                                     self.graph)
            self.progressBar.setValue(70)
            self.showMatrixTable()
            self.progressBar.setValue(80)
            imp_time, lib_time = self.run_PR()
            self.showPlotlyFig(['implemented', 'networkx library'], [imp_time, lib_time], 1, 2)
            self.progressBar.setValue(90)
            self.runFloyd()
            self.progressBar.setValue(100)
            self.progressBar.setValue(0)
        else:
            self.progressBar.setValue(10)
            self.DAGgen.Generate_DirectedGraph(self.graph)
            self.progressBar.setValue(40)
            self.showPic()
            self.progressBar.setValue(60)
            self.Xwriter.xw_to_excel(self.graph.matrix, f'./xlsx/DirectedGraph/xlsx_{self.DAGgen.timestamp}.xlsx',
                                     self.graph)
            self.progressBar.setValue(70)
            self.showMatrixTable()
            self.progressBar.setValue(80)
            imp_time, lib_time = self.run_PR()
            self.showPlotlyFig(['implemented', 'networkx library'], [imp_time, lib_time], 1, 2)
            self.progressBar.setValue(90)
            self.runFloyd()
            self.progressBar.setValue(100)
            self.progressBar.setValue(0)

    def confirmGraph(self):
        for i in range(self.tableIndex, 0, -1):
            self.edgelistframe.removeRow(i - 1)

        self.clearMatrixTable()
        self.clearPRTable()
        self.clearFloydTable()

        if self.node_num.text() == '':
            self.graph.MAX_NODE_SIZES = 0
        else:
            self.graph.MAX_NODE_SIZES = int(self.node_num.text())

        self.graph.edges_buffer = []
        self.tableIndex = 0

    def addEdge(self):
        e = Utils.random_edges(self.graph)
        self.graph.edges_buffer.append(e)
        col1 = QTableWidgetItem(str(e[0]))
        col2 = QTableWidgetItem(str(e[1]))
        col3 = QTableWidgetItem(str(e[2]))
        self.edgelistframe.insertRow(int(self.edgelistframe.rowCount()))
        self.edgelistframe.setItem(self.tableIndex, 0, col1)
        self.edgelistframe.setItem(self.tableIndex, 1, col2)
        self.edgelistframe.setItem(self.tableIndex, 2, col3)
        self.tableIndex += 1

    def delEdge(self):
        if not self.graph.edges_buffer:
            return
        self.edgelistframe.removeRow(self.tableIndex - 1)
        self.tableIndex -= 1
        self.graph.edges_buffer.pop()

    def showPic(self):
        if self.graph.Gtype == 0:
            img = QImage(f"./images/UndirectedGraph/UDG_{self.UDGgen.timestamp}")
            pixmap = QPixmap.fromImage(img)
            self.view.setPixmap(pixmap)
        else:
            img = QImage(f"./images/DirectedGraph/DAG_{self.DAGgen.timestamp}")
            pixmap = QPixmap.fromImage(img)
            self.view.setPixmap(pixmap)

    def showMatrixTable(self):
        self.matrixTable.setRowCount(self.graph.MAX_NODE_SIZES)
        self.matrixTable.setColumnCount(self.graph.MAX_NODE_SIZES)
        self.matrixTable.clear()
        for i in range(1, len(self.graph.matrix)):
            for j in range(1, len(self.graph.matrix)):
                self.matrixTable.setItem(i - 1, j - 1, QTableWidgetItem(str(self.graph.matrix[i][j])))

    def changeType(self, val):
        self.graph.Gtype = val

    def quickSpawn(self):
        if self.edge_num.text() == '':
            self.graph.MAX_EDGE_SIZES = 0
        else:
            self.graph.MAX_EDGE_SIZES = int(self.edge_num.text())
        cnt = self.graph.MAX_EDGE_SIZES
        for i in range(cnt):
            self.addEdge()

    def exit(self):
        self.close()

    def runSPFA(self):
        st = self.start_point.text()
        ed = self.end_point.text()
        spfa = Algo.SPFA()
        time_start = time.time()
        chk, sp = spfa.work(self.graph.matrix, st, ed)
        time_end = time.time()
        delay = time_end - time_start
        self.progressBar.setValue(20)
        if chk == 2:
            if self.graph.Gtype == 1:
                self.DAGgen.GenerateDAGShortestPathGraphic(self.graph, sp)
            else:
                self.UDGgen.GenerateUDGShortestPathGraphic(self.graph, sp)
            lib_start_time = time.time()
            try:
                libp = spfa.lib_Bellman_Ford_Algorithm(self.graph, st, ed)
            except Exception as e:
                self.SPFAreport.setText('Neg Ring DETECTED!')
                self.progressBar.setValue(100)
                self.progressBar.setValue(0)
            lib_end_time = time.time()
            lib_elapsed_time = lib_end_time - lib_start_time
            self.showSPPic()
            self.showPlotlyFig(['implemented', 'networks bellman_ford'], [delay, lib_elapsed_time], 1, 1)
            text = 'nodes passed through: '
            for i in range(len(sp)):
                if i == len(sp) - 1:
                    text += str(sp[i])
                else:
                    text += str(sp[i])
                    text += ' -> '
            self.SPFAreport.setText(text)
        elif chk == 0:
            self.SPFAreport.setText('Impossible!')
        else:
            self.SPFAreport.setText('Neg Ring DETECTED!')
        self.progressBar.setValue(100)
        self.progressBar.setValue(0)

    def showSPPic(self):
        if self.graph.Gtype == 0:
            img = QImage(f"./temp/UDG_SP")
            pixmap = QPixmap.fromImage(img)
            self.SPFAview.setPixmap(pixmap)
        else:
            img = QImage(f"./temp/DAG_SP")
            pixmap = QPixmap.fromImage(img)
            self.SPFAview.setPixmap(pixmap)

    def runFloyd(self):
        floyd = Algo.Floyd()
        time_start = time.time()
        dis_matrix = floyd.work(self.graph)
        time_end = time.time()
        delay = time_end - time_start
        lib_start_time = time.time()
        floyd.lib_Floyd_Algorithm(self.graph)
        lib_end_time = time.time()
        lib_elapsed_time = lib_end_time - lib_start_time
        self.showPlotlyFig(['implemented', 'networks floyd'], [delay, lib_elapsed_time], 1, 4)
        self.showFloydTable(dis_matrix)

    def showFloydTable(self, dis_matrix):
        self.floydTable.setRowCount(self.graph.MAX_NODE_SIZES)
        self.floydTable.setColumnCount(self.graph.MAX_NODE_SIZES)
        self.floydTable.clear()
        for i in range(1, len(self.graph.matrix)):
            for j in range(1, len(self.graph.matrix)):
                self.floydTable.setItem(i - 1, j - 1, QTableWidgetItem(str(dis_matrix[i][j])))

    def showPlotlyFig(self, x_coordinate, y_coordinate, fig_type, id, data=None):
        dc = DC.DrawChart()
        match fig_type:
            case 1:
                dc.drawBar(x_coordinate, y_coordinate, id)
            case 2:
                dc.drawScatter(x_coordinate, y_coordinate, id, data)
            case _:
                print('Invalid')

        match id:
            case 1:
                self.SPFAStatistic.load(
                    QUrl.fromLocalFile(os.path.abspath(f'./temp/plotly_bar{id}.html')))
            case 2:
                self.PRStatistic.load(
                    QUrl.fromLocalFile(os.path.abspath(f'./temp/plotly_bar{id}.html')))
            case 3:
                self.webEngineView_3.load(
                    QUrl.fromLocalFile(os.path.abspath(f'./temp/plotly_scatter{id}.html')))
            case 4:
                self.FloydStatistic.load(
                    QUrl.fromLocalFile(os.path.abspath(f'./temp/plotly_bar{id}.html')))
            case _:
                print('Invalid')

    def run_PR(self):
        implemented_start_time = time.time()
        rpv = self.pageR.run_Implemented_PageRank_algorithm(self.graph.matrix)
        implemented_end_time = time.time()
        implemented_elapsed_time = implemented_end_time - implemented_start_time
        lib_start_time = time.time()
        self.pageR.run_Lib_PageRank_algorithm(self.graph.matrix)
        lib_end_time = time.time()
        lib_elapsed_time = lib_end_time - lib_start_time
        val = []
        data = []
        for i in range(len(rpv)):
            val.append(rpv[i][2])
        for i in range(len(rpv)):
            data.append(rpv[i][1])
        self.showPlotlyFig(list(range(1, len(rpv) + 1)), val, 2, 3, data)
        for i in range(len(rpv)):
            self.PRtable.insertRow(int(self.PRtable.rowCount()))
            self.PRtable.setItem(self.PR_tableIndex, 0, QTableWidgetItem(str(data[i])))
            self.PRtable.setItem(self.PR_tableIndex, 1, QTableWidgetItem(str(rpv[i][2])))
            self.PR_tableIndex += 1
        return implemented_elapsed_time, lib_elapsed_time

    def clearMatrixTable(self):
        for i in range(self.graph.MAX_NODE_SIZES, -1, -1):
            self.matrixTable.removeRow(i)
        for i in range(self.graph.MAX_NODE_SIZES, -1, -1):
            self.matrixTable.removeColumn(i)

    def clearPRTable(self):
        for i in range(self.PR_tableIndex, 0, -1):
            self.PRtable.removeRow(i - 1)
        self.PR_tableIndex = 0

    def clearFloydTable(self):
        for i in range(self.graph.MAX_NODE_SIZES, -1, -1):
            self.floydTable.removeRow(i)
        for i in range(self.graph.MAX_NODE_SIZES, -1, -1):
            self.floydTable.removeColumn(i)

    def turnNeg(self):
        if self.btn_nw.isChecked():
            self.graph.MIN_WEIGHT = -9
        else:
            self.graph.MIN_WEIGHT = 1

    # 析构函数，每次结束都删除这些冗余的html文件
    def __del__(self):
        if os.path.exists('./temp/plotly_bar1.html'):
            os.remove('./temp/plotly_bar1.html')
        if os.path.exists('./temp/plotly_bar2.html'):
            os.remove('./temp/plotly_bar2.html')
        if os.path.exists('./temp/plotly_scatter3.html'):
            os.remove('./temp/plotly_scatter3.html')
        if os.path.exists('./temp/DAG_SP.png'):
            os.remove('./temp/DAG_SP.png')
        if os.path.exists('./temp/UDG_SP.png'):
            os.remove('./temp/UDG_SP.png')
        if os.path.exists('./temp/plotly_bar4.html'):
            os.remove('./temp/plotly_bar4.html')
        if os.path.exists('./temp/plotly_scatter5.html'):
            os.remove('./temp/plotly_scatter5.html')

    def sideBarChange(self, index):
        match index:
            case 0:
                self.footerAnim(0)
                self.sideBarAnim(0)
                self.cur = 1
            case 1:
                self.footerAnim(0)
                self.sideBarAnim(0)
                self.cur = 1
            case 2:
                self.footerAnim(0)
                self.sideBarAnim(0)
                self.cur = 1
            case 3:
                self.footerAnim(0)
                self.sideBarAnim(0)
                self.cur = 1
            case 4:
                self.footerAnim(1)
                self.sideBarAnim(1)
                self.cur = 0
            case 5:
                self.footerAnim(1)
                self.sideBarAnim(1)
                self.cur = 0
            case _:
                self.footerAnim(0)
                self.sideBarAnim(0)
                self.cur = 1

    def sideBarAnim(self, val):
        if val == 1:
            if self.cur == 0:
                return
            self.sidebarAnima = QPropertyAnimation(self.sideBar, b"maximumWidth")
            self.sidebarAnima.setDuration(300)
            self.sidebarAnima.setStartValue(220)
            self.sidebarAnima.setEndValue(0)
            self.sidebarAnima.start()
        else:
            if self.cur == 1:
                return
            self.sidebarAnima = QPropertyAnimation(self.sideBar, b"maximumWidth")
            self.sidebarAnima.setDuration(300)
            self.sidebarAnima.setStartValue(0)
            self.sidebarAnima.setEndValue(220)
            self.sidebarAnima.start()

    def footerAnim(self, val):
        if val == 1:
            if self.cur == 0:
                return
            self.footerAnima = QPropertyAnimation(self.footer, b"maximumHeight")
            self.footerAnima.setDuration(300)
            self.footerAnima.setStartValue(42)
            self.footerAnima.setEndValue(0)
            self.footerAnima.start()
        else:
            if self.cur == 1:
                return
            self.footerAnima = QPropertyAnimation(self.footer, b"maximumHeight")
            self.footerAnima.setDuration(300)
            self.footerAnima.setStartValue(0)
            self.footerAnima.setEndValue(42)
            self.footerAnima.start()

    def activateHLM(self):
        print("on")
        self.hlmlauncher = HLMLauncher.HLMLauncher()
        self.hlmThread = QThread()
        self.hlmlauncher.progress.connect(self.updateProgress)
        self.hlmlauncher.complete.connect(self.isComplete)
        self.glob.connect(self.hlmlauncher.work)
        self.hlmlauncher.moveToThread(self.hlmThread)
        self.hlmThread.start()
        self.btn_activHLM.hide()
        self.HLMmaskinmask.show()
        n = 5
        self.HLMprogressbar.setMaximum(n)
        self.glob.emit(n)

    def updateProgress(self, v):
        self.HLMprogressbar.setValue(v)
        match v:
            case 1:
                self.loadingLabel.setText("Loading...: Launching Neo4j")
            case 2:
                self.loadingLabel.setText("Loading...: Generating Knowledge Graph")
            case 3:
                self.loadingLabel.setText("Loading...: Generating WordClouds")
            case 4:
                self.loadingLabel.setText("Parsing...")
            case _:
                self.loadingLabel.setText("")

    def isComplete(self, v):
        self.PaperMask.show()
        self.PaperTable.hide()
        self.papermaskinmask.hide()
        self.btn_activPaper.show()
        self.HLMprogressbar.setValue(v)
        self.HLmask.hide()
        self.KGtabs.show()
        self.showWC()
        self.hlmThread.quit()
        self.hlmThread.wait()

    def showWC(self):
        img = QImage(f"./WordClouds/graphics/HLM_word_cloud.png")
        pixmap = QPixmap.fromImage(img)
        self.wcLabel.setPixmap(pixmap)

    def activatePaper(self):
        self.paperLauncher = PaperLauncher.PaperLauncher()
        self.paperThread = QThread()
        self.paperLauncher.progress.connect(self.updatePaperProgress)
        self.paperLauncher.complete.connect(self.isPaperComplete)
        self.globPaper.connect(self.paperLauncher.work)
        self.paperLauncher.moveToThread(self.paperThread)
        self.paperThread.start()
        self.btn_activPaper.hide()
        self.papermaskinmask.show()
        n = 5
        self.PaperprogressBar.setMaximum(n)
        self.globPaper.emit(n)

    def updatePaperProgress(self, v):
        self.PaperprogressBar.setValue(v)
        match v:
            case 1:
                self.Paperlabel.setText("Loading...: Launching Neo4j")
            case 2:
                self.Paperlabel.setText("Loading...: Generating Knowledge Graph")
            case 3:
                self.Paperlabel.setText("Loading...: Parsing PageRank")
            case 4:
                self.Paperlabel.setText("Loading...: Drawing Chart")
            case _:
                self.Paperlabel.setText("")

    def isPaperComplete(self, v):
        self.HLmask.show()
        self.KGtabs.hide()
        self.btn_activHLM.show()
        self.HLMmaskinmask.hide()
        self.PaperprogressBar.setValue(v)
        self.PaperScatterView.load(
            QUrl.fromLocalFile(os.path.abspath(f'./temp/plotly_scatter5.html')))
        self.paperPRShow()
        self.PaperMask.hide()
        self.PaperTable.show()
        self.paperThread.quit()
        self.paperThread.wait()

    def paperPRShow(self):
        mat = PMat.build_paper_matrix()
        rpv = self.pageR.run_Implemented_PageRank_algorithm(mat)
        val = []
        dirname = os.listdir('./Thesis/resources')
        data = []
        for filename in dirname:
            data.append(filename[:len(filename) - 4])
        finaldata = []
        for i in range(len(rpv)):
            finaldata.append(data[rpv[i][1] - 1])
        for i in range(len(rpv)):
            val.append(rpv[i][2])
        for i in range(len(rpv)):
            self.PageRankView.insertRow(int(self.PageRankView.rowCount()))
            self.PageRankView.setItem(self.PaperPR_tableIndex, 0, QTableWidgetItem(str(finaldata[i])))
            self.PageRankView.setItem(self.PaperPR_tableIndex, 1, QTableWidgetItem(str(rpv[i][2])))
            self.PaperPR_tableIndex += 1

    def bindComboBox(self):
        dirname = os.listdir('./CharactersImages')
        for filename in dirname:
            self.comboBox.addItem(filename[:len(filename)-4])

    def showRelationship(self):
        ind = self.comboBox.currentIndex()
        dirname = os.listdir('./CharactersImages')
        lis = []
        for filename in dirname:
            lis.append(filename)
        img = QImage(f"./CharactersImages/{lis[ind]}")
        pixmap = QPixmap.fromImage(img)
        self.relationView.setPixmap(pixmap)


def run():
    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml')
    window = Frame()
    window.show()
    sys.exit(app.exec_())
