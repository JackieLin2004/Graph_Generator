import os

from PySide6.QtCore import QObject, Signal
import Kernel.DrawChart as DC
import Kernel.PageRank as PR
import KnowledgeGraph.build_knowledge_graph as KG
import Thesis.Matrix as PMat
import neochecker


class PaperLauncher(QObject):
    progress = Signal(int)
    complete = Signal(int)

    def __init__(self):
        super().__init__()

    def work(self):
        self.progress.emit(1)
        if not neochecker.isNeoRun:
            os.system('neolauncher.bat')
            neochecker.isNeoRun = True
        self.progress.emit(2)
        kg = KG.KnowledgeGraph()
        kg.build_paper_knowledge_graph()
        self.progress.emit(3)
        pr = PR.PageRank()
        mat = PMat.build_paper_matrix()
        rpv = pr.run_Implemented_PageRank_algorithm(mat)
        print(rpv)
        val = []
        dirname = os.listdir('./Thesis/resources')
        data = []
        for filename in dirname:
            data.append(filename[:len(filename) - 4])
        finaldata = []
        for i in range(len(rpv)):
            finaldata.append(data[rpv[i][1]-1])
        print(finaldata)
        for i in range(len(rpv)):
            val.append(rpv[i][2])
        self.progress.emit(4)
        dc = DC.DrawChart()
        dc.drawScatter(list(range(1, len(rpv) + 1)), val, 5, finaldata)
        self.complete.emit(5)
