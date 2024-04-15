import os

from PySide6.QtCore import QObject, Signal

import KnowledgeGraph.build_knowledge_graph as KG
import WordClouds.build_HLM_wordclouds as WC
import neochecker


class HLMLauncher(QObject):
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
        kg.build_HLM_knowledge_graph()
        self.progress.emit(3)
        wc = WC.WordClouds()
        wc.run_word_cloud()
        self.progress.emit(4)
        self.complete.emit(5)
