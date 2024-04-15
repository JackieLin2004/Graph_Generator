# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generator_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1170, 750)
        Form.setMinimumSize(QSize(400, 750))
        Form.setMaximumSize(QSize(14214, 135135))
        self.horizontalLayout_8 = QHBoxLayout(Form)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.sideBar = QFrame(Form)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMaximumSize(QSize(220, 16777215))
        self.sideBar.setFrameShape(QFrame.StyledPanel)
        self.sideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sideBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.sideBar)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 2))
        self.groupBox.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_UDG = QRadioButton(self.groupBox)
        self.btn_UDG.setObjectName(u"btn_UDG")

        self.verticalLayout.addWidget(self.btn_UDG)

        self.btn_DAG = QRadioButton(self.groupBox)
        self.btn_DAG.setObjectName(u"btn_DAG")

        self.verticalLayout.addWidget(self.btn_DAG)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.widget = QWidget(self.sideBar)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_addEdge = QPushButton(self.widget_3)
        self.btn_addEdge.setObjectName(u"btn_addEdge")
        self.btn_addEdge.setMinimumSize(QSize(0, 0))
        self.btn_addEdge.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_addEdge)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_delEdge = QPushButton(self.widget_3)
        self.btn_delEdge.setObjectName(u"btn_delEdge")
        self.btn_delEdge.setMinimumSize(QSize(0, 0))
        self.btn_delEdge.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_delEdge)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.btn_generate = QPushButton(self.widget)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setMinimumSize(QSize(140, 150))
        self.btn_generate.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.btn_generate)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.sideBar)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.node_num = QLineEdit(self.widget_2)
        self.node_num.setObjectName(u"node_num")
        self.node_num.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4.addWidget(self.node_num)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.edge_num = QLineEdit(self.widget_2)
        self.edge_num.setObjectName(u"edge_num")
        self.edge_num.setMaximumSize(QSize(16777215, 16777215))
        self.edge_num.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.edge_num)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_confirm = QPushButton(self.widget_2)
        self.btn_confirm.setObjectName(u"btn_confirm")
        font = QFont()
        font.setPointSize(9)
        self.btn_confirm.setFont(font)

        self.verticalLayout_6.addWidget(self.btn_confirm)

        self.btn_qspawn = QPushButton(self.widget_2)
        self.btn_qspawn.setObjectName(u"btn_qspawn")
        self.btn_qspawn.setFont(font)

        self.verticalLayout_6.addWidget(self.btn_qspawn)

        self.btn_exit = QPushButton(self.widget_2)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setFont(font)

        self.verticalLayout_6.addWidget(self.btn_exit)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.btn_nw = QCheckBox(self.widget_2)
        self.btn_nw.setObjectName(u"btn_nw")

        self.verticalLayout_4.addWidget(self.btn_nw)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout_8.addWidget(self.sideBar)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.Gtab = QWidget()
        self.Gtab.setObjectName(u"Gtab")
        self.horizontalLayout_10 = QHBoxLayout(self.Gtab)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_4 = QWidget(self.Gtab)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_7.addWidget(self.label_3)

        self.view = QLabel(self.widget_4)
        self.view.setObjectName(u"view")
        self.view.setMinimumSize(QSize(500, 300))
        self.view.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.view)


        self.horizontalLayout_10.addWidget(self.widget_4)

        self.dockWidget = QDockWidget(self.Gtab)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMaximumSize(QSize(450, 524287))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout_4 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.widget_5 = QWidget(self.dockWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.edgelistframe = QTableWidget(self.widget_5)
        self.edgelistframe.setObjectName(u"edgelistframe")
        self.edgelistframe.setMinimumSize(QSize(100, 0))
        self.edgelistframe.setMaximumSize(QSize(340, 16777215))
        self.edgelistframe.setBaseSize(QSize(264, 0))

        self.verticalLayout_8.addWidget(self.edgelistframe)


        self.horizontalLayout_4.addWidget(self.widget_5)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout_10.addWidget(self.dockWidget)

        self.tabWidget.addTab(self.Gtab, "")
        self.Matrixtab = QWidget()
        self.Matrixtab.setObjectName(u"Matrixtab")
        self.horizontalLayout_2 = QHBoxLayout(self.Matrixtab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.matrixTable = QTableWidget(self.Matrixtab)
        self.matrixTable.setObjectName(u"matrixTable")

        self.horizontalLayout_2.addWidget(self.matrixTable)

        self.tabWidget.addTab(self.Matrixtab, "")
        self.SPtab = QWidget()
        self.SPtab.setObjectName(u"SPtab")
        self.horizontalLayout_5 = QHBoxLayout(self.SPtab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget_2 = QTabWidget(self.SPtab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.floydTable = QTableWidget(self.tab_5)
        self.floydTable.setObjectName(u"floydTable")

        self.horizontalLayout_13.addWidget(self.floydTable)

        self.dockWidget_4 = QDockWidget(self.tab_5)
        self.dockWidget_4.setObjectName(u"dockWidget_4")
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayout_14 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.FloydStatistic = QWebEngineView(self.dockWidgetContents_4)
        self.FloydStatistic.setObjectName(u"FloydStatistic")
        self.FloydStatistic.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_14.addWidget(self.FloydStatistic)

        self.dockWidget_4.setWidget(self.dockWidgetContents_4)

        self.horizontalLayout_13.addWidget(self.dockWidget_4)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_8 = QWidget(self.tab_6)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_9 = QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_7 = QWidget(self.widget_8)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.start_point = QLineEdit(self.widget_7)
        self.start_point.setObjectName(u"start_point")

        self.horizontalLayout_9.addWidget(self.start_point)

        self.end_point = QLineEdit(self.widget_7)
        self.end_point.setObjectName(u"end_point")

        self.horizontalLayout_9.addWidget(self.end_point)

        self.btn_runSP = QPushButton(self.widget_7)
        self.btn_runSP.setObjectName(u"btn_runSP")

        self.horizontalLayout_9.addWidget(self.btn_runSP)


        self.verticalLayout_9.addWidget(self.widget_7)

        self.SPFAview = QLabel(self.widget_8)
        self.SPFAview.setObjectName(u"SPFAview")

        self.verticalLayout_9.addWidget(self.SPFAview)

        self.SPFAreport = QLabel(self.widget_8)
        self.SPFAreport.setObjectName(u"SPFAreport")
        self.SPFAreport.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_9.addWidget(self.SPFAreport)


        self.horizontalLayout_11.addWidget(self.widget_8)

        self.frame_2 = QFrame(self.tab_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.dockWidget_2 = QDockWidget(self.frame_2)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_11 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.SPFAStatistic = QWebEngineView(self.dockWidgetContents_2)
        self.SPFAStatistic.setObjectName(u"SPFAStatistic")
        self.SPFAStatistic.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_11.addWidget(self.SPFAStatistic)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)

        self.verticalLayout_10.addWidget(self.dockWidget_2)


        self.horizontalLayout_11.addWidget(self.frame_2)

        self.tabWidget_2.addTab(self.tab_6, "")

        self.horizontalLayout_5.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.SPtab, "")
        self.PRtab = QWidget()
        self.PRtab.setObjectName(u"PRtab")
        self.horizontalLayout_12 = QHBoxLayout(self.PRtab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_9 = QWidget(self.PRtab)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_13 = QVBoxLayout(self.widget_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.webEngineView_3 = QWebEngineView(self.widget_9)
        self.webEngineView_3.setObjectName(u"webEngineView_3")
        self.webEngineView_3.setMinimumSize(QSize(650, 450))
        self.webEngineView_3.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_13.addWidget(self.webEngineView_3)

        self.PRtable = QTableWidget(self.widget_9)
        self.PRtable.setObjectName(u"PRtable")

        self.verticalLayout_13.addWidget(self.PRtable)


        self.horizontalLayout_12.addWidget(self.widget_9)

        self.dockWidget_3 = QDockWidget(self.PRtab)
        self.dockWidget_3.setObjectName(u"dockWidget_3")
        self.dockWidget_3.setMaximumSize(QSize(524287, 524287))
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_12 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.PRStatistic = QWebEngineView(self.dockWidgetContents_3)
        self.PRStatistic.setObjectName(u"PRStatistic")
        self.PRStatistic.setMaximumSize(QSize(16777215, 16777215))
        self.PRStatistic.setBaseSize(QSize(400, 0))
        self.PRStatistic.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_12.addWidget(self.PRStatistic)

        self.dockWidget_3.setWidget(self.dockWidgetContents_3)

        self.horizontalLayout_12.addWidget(self.dockWidget_3)

        self.tabWidget.addTab(self.PRtab, "")
        self.KGtab = QWidget()
        self.KGtab.setObjectName(u"KGtab")
        self.horizontalLayout_14 = QHBoxLayout(self.KGtab)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.HLmask = QWidget(self.KGtab)
        self.HLmask.setObjectName(u"HLmask")
        self.gridLayout = QGridLayout(self.HLmask)
        self.gridLayout.setObjectName(u"gridLayout")
        self.HLMmaskinmask = QWidget(self.HLmask)
        self.HLMmaskinmask.setObjectName(u"HLMmaskinmask")
        self.verticalLayout_15 = QVBoxLayout(self.HLMmaskinmask)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.loadingLabel = QLabel(self.HLMmaskinmask)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setMaximumSize(QSize(16777215, 30))
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.loadingLabel)

        self.HLMprogressbar = QProgressBar(self.HLMmaskinmask)
        self.HLMprogressbar.setObjectName(u"HLMprogressbar")
        self.HLMprogressbar.setMaximumSize(QSize(16777215, 16777215))
        self.HLMprogressbar.setValue(24)
        self.HLMprogressbar.setAlignment(Qt.AlignCenter)
        self.HLMprogressbar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_15.addWidget(self.HLMprogressbar)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)


        self.gridLayout.addWidget(self.HLMmaskinmask, 1, 0, 1, 1)

        self.btn_activHLM = QPushButton(self.HLmask)
        self.btn_activHLM.setObjectName(u"btn_activHLM")
        self.btn_activHLM.setMaximumSize(QSize(200, 100))
        self.btn_activHLM.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.btn_activHLM, 0, 0, 1, 1)


        self.horizontalLayout_14.addWidget(self.HLmask)

        self.KGtabs = QTabWidget(self.KGtab)
        self.KGtabs.setObjectName(u"KGtabs")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.webEngineView = QWebEngineView(self.tab_8)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_15.addWidget(self.webEngineView)

        self.KGtabs.addTab(self.tab_8, "")
        self.wordCloudsTable = QWidget()
        self.wordCloudsTable.setObjectName(u"wordCloudsTable")
        self.horizontalLayout_17 = QHBoxLayout(self.wordCloudsTable)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.wcLabel = QLabel(self.wordCloudsTable)
        self.wcLabel.setObjectName(u"wcLabel")
        self.wcLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.wcLabel)

        self.KGtabs.addTab(self.wordCloudsTable, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_20 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.widget_6 = QWidget(self.tab_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(130, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.widget_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.comboBox = QComboBox(self.widget_6)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_16.addWidget(self.comboBox)

        self.btn_search = QPushButton(self.widget_6)
        self.btn_search.setObjectName(u"btn_search")

        self.verticalLayout_16.addWidget(self.btn_search)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_6)


        self.horizontalLayout_20.addWidget(self.widget_6)

        self.relationView = QLabel(self.tab_4)
        self.relationView.setObjectName(u"relationView")

        self.horizontalLayout_20.addWidget(self.relationView)

        self.KGtabs.addTab(self.tab_4, "")

        self.horizontalLayout_14.addWidget(self.KGtabs)

        self.tabWidget.addTab(self.KGtab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_16 = QHBoxLayout(self.tab)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.PaperMask = QWidget(self.tab)
        self.PaperMask.setObjectName(u"PaperMask")
        self.gridLayout_2 = QGridLayout(self.PaperMask)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_activPaper = QPushButton(self.PaperMask)
        self.btn_activPaper.setObjectName(u"btn_activPaper")
        self.btn_activPaper.setMaximumSize(QSize(200, 100))
        self.btn_activPaper.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.btn_activPaper, 0, 0, 1, 1)

        self.papermaskinmask = QWidget(self.PaperMask)
        self.papermaskinmask.setObjectName(u"papermaskinmask")
        self.verticalLayout_17 = QVBoxLayout(self.papermaskinmask)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.Paperlabel = QLabel(self.papermaskinmask)
        self.Paperlabel.setObjectName(u"Paperlabel")
        self.Paperlabel.setMaximumSize(QSize(16777215, 30))
        self.Paperlabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.Paperlabel)

        self.PaperprogressBar = QProgressBar(self.papermaskinmask)
        self.PaperprogressBar.setObjectName(u"PaperprogressBar")
        self.PaperprogressBar.setValue(24)

        self.verticalLayout_17.addWidget(self.PaperprogressBar)

        self.verticalSpacer_5 = QSpacerItem(20, 231, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)


        self.gridLayout_2.addWidget(self.papermaskinmask, 1, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.PaperMask)

        self.PaperTable = QTabWidget(self.tab)
        self.PaperTable.setObjectName(u"PaperTable")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.PaperKGView = QWebEngineView(self.tab_2)
        self.PaperKGView.setObjectName(u"PaperKGView")
        self.PaperKGView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_18.addWidget(self.PaperKGView)

        self.PaperTable.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_19 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.PaperScatterView = QWebEngineView(self.tab_3)
        self.PaperScatterView.setObjectName(u"PaperScatterView")
        self.PaperScatterView.setMinimumSize(QSize(700, 0))
        self.PaperScatterView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_19.addWidget(self.PaperScatterView)

        self.PageRankView = QTableWidget(self.tab_3)
        self.PageRankView.setObjectName(u"PageRankView")
        self.PageRankView.setMaximumSize(QSize(600, 16777215))

        self.horizontalLayout_19.addWidget(self.PageRankView)

        self.PaperTable.addTab(self.tab_3, "")

        self.horizontalLayout_16.addWidget(self.PaperTable)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.footer = QWidget(Form)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_6 = QHBoxLayout(self.footer)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.footer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(300, 20))
        self.progressBar.setValue(24)

        self.horizontalLayout_6.addWidget(self.progressBar)


        self.verticalLayout_5.addWidget(self.footer)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(1)
        self.KGtabs.setCurrentIndex(2)
        self.PaperTable.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Select Graph Type", None))
        self.btn_UDG.setText(QCoreApplication.translate("Form", u"Undirected Graph", None))
        self.btn_DAG.setText(QCoreApplication.translate("Form", u"Directed Graph", None))
        self.btn_addEdge.setText(QCoreApplication.translate("Form", u"Add", None))
        self.btn_delEdge.setText(QCoreApplication.translate("Form", u"Del", None))
        self.btn_generate.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Node number", None))
        self.label.setText(QCoreApplication.translate("Form", u"Edge number", None))
        self.btn_confirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.btn_qspawn.setText(QCoreApplication.translate("Form", u"Quick Spawn", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"exit", None))
        self.btn_nw.setText(QCoreApplication.translate("Form", u"Negative Weight", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Graph Palette >", None))
        self.view.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Edge Table >", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gtab), QCoreApplication.translate("Form", u"Graph", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Matrixtab), QCoreApplication.translate("Form", u"Matrix", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Floyd (Multi-sources)", None))
        self.btn_runSP.setText(QCoreApplication.translate("Form", u"run", None))
        self.SPFAview.setText("")
        self.SPFAreport.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("Form", u"SPFA(Single-source)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SPtab), QCoreApplication.translate("Form", u"ShortestPath", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PRtab), QCoreApplication.translate("Form", u"PageRank", None))
        self.loadingLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_activHLM.setText(QCoreApplication.translate("Form", u"Activate", None))
        self.KGtabs.setTabText(self.KGtabs.indexOf(self.tab_8), QCoreApplication.translate("Form", u"Knowledge Graph", None))
        self.wcLabel.setText("")
        self.KGtabs.setTabText(self.KGtabs.indexOf(self.wordCloudsTable), QCoreApplication.translate("Form", u"Word Cloud", None))
        self.btn_search.setText(QCoreApplication.translate("Form", u"search", None))
        self.relationView.setText("")
        self.KGtabs.setTabText(self.KGtabs.indexOf(self.tab_4), QCoreApplication.translate("Form", u"relationships", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.KGtab), QCoreApplication.translate("Form", u"HLM Analysis", None))
        self.btn_activPaper.setText(QCoreApplication.translate("Form", u"Activate", None))
        self.Paperlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.PaperTable.setTabText(self.PaperTable.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Knowledge Graph", None))
        self.PaperTable.setTabText(self.PaperTable.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Pagerank", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Paper Analysis", None))
    # retranslateUi

