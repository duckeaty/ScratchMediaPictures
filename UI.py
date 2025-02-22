import sys
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("视频帧提取器")
        MainWindow.resize(788, 590)
        sizePolicy_h = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy_h.setHorizontalStretch(1)
        sizePolicy_v = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy_v.setVerticalStretch(1)
        sizePolicy_hv = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy_hv.setHorizontalStretch(1)
        sizePolicy_hv.setVerticalStretch(1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy_hv)
        MainWindow.setMinimumSize(QtCore.QSize(788, 590))
        #MainWindow.setMaximumSize(QtCore.QSize(788, 590))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


#=======================layout===========================
        self.main_layout = QtWidgets.QVBoxLayout(MainWindow)
        self.main_layout.setContentsMargins(10, 10, 10, 10)


        self.main_layout.setObjectName("main_layout")
        #self.Layout_Widget.setSizePolicy(sizePolicy_hv)
        self.centralwidget.setLayout(self.main_layout)
        self.setCentralWidget(self.centralwidget)


#=======================   上   ===============================
    #--------------------------groupBox-----------------------
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        #self.groupBox.setGeometry(QtCore.QRect(0, 0, 750, 40))
        self.groupBox_1.setObjectName("groupBox_1")
        self.groupBox_1.setTitle("视频列表")
        self.groupBox_1lay = QtWidgets.QHBoxLayout(self.groupBox_1)
        # self.groupBox.setGeometry(QtCore.QRect(0, 0, 750, 40))
        self.groupBox_1lay.setObjectName("groupBox_1lay")
        self.groupBox_1lay.setContentsMargins(0,0,0,0)


        self.groupBox_b1 = QtWidgets.QGroupBox(self.groupBox_1)
        #self.groupBox_b1.setGeometry(QtCore.QRect(10, 40, 751, 381))
        self.groupBox_b1.setFixedSize(240,30)
        self.groupBox_b1.setTitle("")
        self.groupBox_b1.setObjectName("groupBox_b1")
        self.groupBox_b1.setStyleSheet("""
            QGroupBox {
                border: none;  /* 去掉边框 */
                background-color: transparent;
            }
        """)
        self.groupBox_b11 = QtWidgets.QGroupBox(self.groupBox_b1)
        # self.groupBox_b1.setGeometry(QtCore.QRect(10, 40, 751, 381))
        self.groupBox_b11.setFixedSize(120, 30)
        self.groupBox_b11.setTitle("")
        self.groupBox_b11.setObjectName("groupBox_b1")
        self.groupBox_b11.setStyleSheet("""
                    QGroupBox {
                        border: none;  /* 去掉边框 */
                        background-color: transparent;
                    }
                """)
        self.groupBox_b12 = QtWidgets.QGroupBox(self.groupBox_b1)
        # self.groupBox_b1.setGeometry(QtCore.QRect(10, 40, 751, 381))
        self.groupBox_b12.setFixedSize(100, 30)
        self.groupBox_b12.setTitle("")
        self.groupBox_b12.setObjectName("groupBox_b1")
        self.groupBox_b12.setStyleSheet("""
                    QGroupBox {
                        border: none;  /* 去掉边框 */
                        background-color: transparent;
                    }
                """)
        self.button_addfile = QtWidgets.QToolButton(self.groupBox_b1)
        self.button_addfile.setGeometry(QtCore.QRect(10, 6, 67, 18))
        self.button_addfile.setObjectName("button_addfile")
        self.button_piclayer_open = QtWidgets.QToolButton(self.groupBox_b1)
        self.button_piclayer_open.setGeometry(QtCore.QRect(82, 6, 67, 18))
        self.button_piclayer_open.setObjectName("button_piclayer_open")
        self.button_1button = QtWidgets.QToolButton(self.groupBox_b1)
        self.button_1button.setGeometry(QtCore.QRect(154, 6, 67, 18))
        self.button_1button.setObjectName("button_1button")

        self.label_format = QtWidgets.QLabel(self.groupBox_b11)
        self.label_format.setGeometry(QtCore.QRect(0, 9, 27, 12))
        self.label_format.setObjectName("label_format")
        self.radioButton_png = QtWidgets.QRadioButton(self.groupBox_b11)
        self.radioButton_png.setGeometry(QtCore.QRect(30, 7, 41, 16))
        self.radioButton_png.setObjectName("radioButton_png")
        self.radioButton_jpg = QtWidgets.QRadioButton(self.groupBox_b11)
        self.radioButton_jpg.setGeometry(QtCore.QRect(74, 7, 41, 16))
        self.radioButton_jpg.setObjectName("radioButton_jpg")
        self.radioButton_jpg.setChecked(True)

        self.label_hv = QtWidgets.QLabel(self.groupBox_b12)
        self.label_hv.setGeometry(QtCore.QRect(0, 9, 27, 12))
        self.label_hv.setObjectName("label_hv")  # 封面图横竖
        self.radioButton_o_h = QtWidgets.QRadioButton(self.groupBox_b12)
        self.radioButton_o_h.setGeometry(QtCore.QRect(30, 7, 41, 16))
        self.radioButton_o_h.setObjectName("radioButton_o_h")
        self.radioButton_o_v = QtWidgets.QRadioButton(self.groupBox_b12)
        self.radioButton_o_v.setGeometry(QtCore.QRect(67, 7, 41, 16))
        self.radioButton_o_v.setObjectName("radioButton_o_v")
        self.radioButton_o_h.setChecked(True)

        self.groupBox_b2 = QtWidgets.QGroupBox(self.groupBox_1)
        # self.groupBox_b1.setGeometry(QtCore.QRect(10, 40, 751, 381))
        self.groupBox_b2.setFixedSize(168, 30)
        self.groupBox_b2.setTitle("")
        self.groupBox_b2.setObjectName("groupBox_b2")
        self.groupBox_b2.setStyleSheet("""
                    QGroupBox {
                        border: none;  /* 去掉边框 */
                        background-color: transparent;
                    }
                """)

        self.button_delfiles = QtWidgets.QToolButton(self.groupBox_b2)
        self.button_delfiles.setGeometry(QtCore.QRect(0, 6, 81, 18))
        #self.button_delfiles.setFixedSize(67, 18)
        self.button_delfiles.setObjectName("button_delfiles")
        self.button_clear = QtWidgets.QToolButton(self.groupBox_b2)
        self.button_clear.setGeometry(QtCore.QRect(91, 6, 67, 18))
        #self.button_clear.setFixedSize(67, 18)
        self.button_clear.setObjectName("button_clear")
    #--------------------------------------------------------------
        self.groupBox_1lay.addWidget(self.groupBox_b1)
        self.groupBox_1lay.addWidget(self.groupBox_b11)
        self.groupBox_1lay.addWidget(self.groupBox_b12)
        self.groupBox_1lay.addStretch(1)
        self.groupBox_1lay.addWidget(self.groupBox_b2)

        self.main_layout.addWidget(self.groupBox_1)

#===================================================================

# =======================layout_2===========================
        # --------------------------groupBox_list-----------------------
        self.groupBox_list = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_list.setObjectName("groupBox_list")
        self.groupBox_list.setContentsMargins(0, 0, 0, 0)
        self.groupBox_list.setGeometry(QtCore.QRect(0, 0, 768, 394))

        self.table_lists = QtWidgets.QHBoxLayout(self.groupBox_list)

        self.table_lists.setObjectName("table_lists")
        self.table_lists.setContentsMargins(0, 0, 0, 0)

        self.tableWidget_lists = QtWidgets.QTableWidget(self.groupBox_list)
        #self.tableWidget_lists.setSizePolicy(sizePolicy_hv)
        self.tableWidget_lists.setGeometry(QtCore.QRect(0, 0, 768, 394))
        self.tableWidget_lists.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_lists.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget_lists.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget_lists.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget_lists.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget_lists.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_lists.setCornerButtonEnabled(True)
        self.tableWidget_lists.setObjectName("tableWidget_lists")
        self.tableWidget_lists.setColumnCount(5)
        self.tableWidget_lists.setRowCount(0)
        table_width = self.tableWidget_lists.width()
        self.tableWidget_lists.setColumnWidth(0, int((table_width - 258) * 0.50))
        self.tableWidget_lists.setColumnWidth(1, int((table_width - 258) * 0.50))
        self.tableWidget_lists.setColumnWidth(2, 70)
        self.tableWidget_lists.setColumnWidth(3, 100)
        self.tableWidget_lists.setColumnWidth(4, 58)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_lists.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_lists.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_lists.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_lists.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_lists.setHorizontalHeaderItem(4, item)

        self.table_lists.addWidget(self.tableWidget_lists)
        self.main_layout.addWidget(self.groupBox_list)
    # --------------------------------------------------------------
# ===================================================================
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2lay = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.groupBox_2lay.setObjectName("groupBox_2lay")
        self.groupBox_2lay.setContentsMargins(0, 0, 0, 0)

        self.groupBox_b3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_b3.setFixedSize(120, 35)
        self.groupBox_b3.setTitle("")
        self.groupBox_b3.setObjectName("groupBox_b3")
        self.groupBox_b3.setStyleSheet("""
                            QGroupBox {
                                border: none;  /* 去掉边框 */
                                background-color: transparent;
                            }
                        """)



        self.groupBox_b4 = QtWidgets.QGroupBox(self.groupBox_2)
        # self.groupBox_b1.setGeometry(QtCore.QRect(10, 40, 751, 381))
        self.groupBox_b4.setFixedSize(150, 35)
        self.groupBox_b4.setTitle("")
        self.groupBox_b4.setObjectName("groupBox_b4")
        self.groupBox_b4.setStyleSheet("""
                                    QGroupBox {
                                        border: none;  /* 去掉边框 */
                                        background-color: transparent;
                                    }
                                """)



        self.groupBox_b5 = QtWidgets.QGroupBox(self.groupBox_2)
        # self.groupBox_b1.setGeometry(QtCore.QRect(10, 40, 751, 381))
        self.groupBox_b5.setFixedSize(455, 35)
        self.groupBox_b5.setTitle("")
        self.groupBox_b5.setObjectName("groupBox_b5")
        self.groupBox_b5.setStyleSheet("""
                                    QGroupBox {
                                        border: none;  /* 去掉边框 */
                                        background-color: transparent;
                                    }
                                """)

        self.radio_getposter = QtWidgets.QRadioButton(self.groupBox_b3)
        self.radio_getposter.setGeometry(QtCore.QRect(20, 9, 86, 16))
        self.radio_getposter.setObjectName("radio_getposter")
        self.radio_getframe_num = QtWidgets.QRadioButton(self.groupBox_b4)
        self.radio_getframe_num.setGeometry(QtCore.QRect(20, 9, 86, 16))
        self.radio_getframe_num.setObjectName("radio_getframe_num")
        self.radio_getframe_random = QtWidgets.QRadioButton(self.groupBox_b5)
        self.radio_getframe_random.setGeometry(QtCore.QRect(20, 9, 86, 16))
        self.radio_getframe_random.setChecked(True)
        self.radio_getframe_random.setObjectName("radio_getframe_random")
        self.line_limitTime1 = QtWidgets.QLineEdit(self.groupBox_b5)
        self.line_limitTime1.setGeometry(QtCore.QRect(115, 9, 51, 16))
        self.line_limitTime1.setMaxLength(6)
        self.line_limitTime1.setCursorPosition(0)
        self.line_limitTime1.setReadOnly(False)
        self.line_limitTime1.setObjectName("line_limitTime1")
        self.line_limitTime2 = QtWidgets.QLineEdit(self.groupBox_b5)
        self.line_limitTime2.setGeometry(QtCore.QRect(199, 9, 51, 16))
        self.line_limitTime2.setMaxLength(6)
        self.line_limitTime2.setReadOnly(False)
        self.line_limitTime2.setClearButtonEnabled(False)
        self.line_limitTime2.setObjectName("line_limitTime2")
        self.line_frame_random_num = QtWidgets.QLineEdit(self.groupBox_b5)
        self.line_frame_random_num.setGeometry(QtCore.QRect(381, 9, 41, 16))
        self.line_frame_random_num.setMaxLength(5)
        self.line_frame_random_num.setCursorPosition(0)
        self.line_frame_random_num.setObjectName("line_frame_random_num")
        self.line_frame_num = QtWidgets.QLineEdit(self.groupBox_b4)
        self.line_frame_num.setGeometry(QtCore.QRect(90, 9, 61, 16))
        self.line_frame_num.setObjectName("line_frame_num")
        self.label_3 = QtWidgets.QLabel(self.groupBox_b5)
        self.label_3.setGeometry(QtCore.QRect(330, 6, 108, 21))
        self.label_3.setObjectName("label_3")
        self.label_isLimitTime = QtWidgets.QLabel(self.groupBox_b5)
        self.label_isLimitTime.setGeometry(QtCore.QRect(101, 9, 186, 16))
        self.label_isLimitTime.setObjectName("label_isLimitTime")
        self.button_confirm = QtWidgets.QToolButton(self.groupBox_b5)
        self.button_confirm.setGeometry(QtCore.QRect(273, 9, 37, 16))
        self.button_confirm.setObjectName("button_confirm")
        self.radio_getposter.raise_()
        self.radio_getframe_num.raise_()
        self.radio_getframe_random.raise_()
        self.label_isLimitTime.raise_()
        self.line_limitTime1.raise_()
        self.line_limitTime2.raise_()
        self.line_frame_num.raise_()
        self.label_3.raise_()
        self.line_frame_random_num.raise_()

        self.groupBox_2lay.addWidget(self.groupBox_b3)
        self.groupBox_2lay.addStretch(1)
        self.groupBox_2lay.addWidget(self.groupBox_b4)
        self.groupBox_2lay.addStretch(1)
        self.groupBox_2lay.addWidget(self.groupBox_b5)
        self.main_layout.addWidget(self.groupBox_2)

#=========================================================================================
        self.groupBox_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setContentsMargins(0, 0, 0, 0)

        self.groupBox_b6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_b6.setFixedSize(620, 51)
        self.groupBox_b6.setTitle("")
        self.groupBox_b6.setObjectName("groupBox_b6")

        self.button_getOutPath = QtWidgets.QToolButton(self.groupBox_b6)
        self.button_getOutPath.setGeometry(QtCore.QRect(470, 10, 41, 31))
        self.button_getOutPath.setObjectName("button_getOutPath")
        self.line_outPath = QtWidgets.QLineEdit(self.groupBox_b6)
        self.line_outPath.setGeometry(QtCore.QRect(104, 10, 361, 31))
        self.line_outPath.setReadOnly(True)
        self.line_outPath.setPlaceholderText("./outImage")
        self.line_outPath.setObjectName("line_outPath")
        self.label = QtWidgets.QLabel(self.groupBox_b6)
        self.label.setGeometry(QtCore.QRect(21, 19, 81, 16))
        self.label.setObjectName("label")
        self.button_openOutPath = QtWidgets.QToolButton(self.groupBox_b6)
        self.button_openOutPath.setGeometry(QtCore.QRect(513, 10, 91, 31))
        self.button_openOutPath.setObjectName("button_openOutPath")

        self.groupBox_b7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_b7.setFixedSize(111, 51)
        self.groupBox_b7.setTitle("")
        self.groupBox_b7.setObjectName("groupBox_b7")
        self.groupBox_b7.setStyleSheet("""
            QGroupBox {
                border: none;  /* 去掉边框 */
                background-color: transparent;
                }
        """)

        self.button_start = QtWidgets.QToolButton(self.groupBox_b7)
        self.button_start.setGeometry(QtCore.QRect(0, 0, 111, 51))
        self.button_start.setStyleSheet("font: 87 14pt;")
        self.button_start.setObjectName("button_start")
        self.button_stop = QtWidgets.QToolButton(self.groupBox_b7)
        self.button_stop.setGeometry(QtCore.QRect(0, 0, 111, 51))
        self.button_stop.setStyleSheet("font: 87 14pt;")
        self.button_stop.setObjectName("button_stop")
        self.button_stop.setHidden(True)

        self.groupBox_3.addWidget(self.groupBox_b6)
        self.groupBox_3.addStretch(1)
        self.groupBox_3.addWidget(self.groupBox_b7)

        self.main_layout.addLayout(self.groupBox_3)

#=========================================================================
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4.setFixedHeight(19)

        self.groupBox_4lay = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.groupBox_4lay.setObjectName("groupBox_2lay")
        self.groupBox_4lay.setContentsMargins(0, 0, 0, 0)

        self.toolButton = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 31, 19))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setFixedHeight(19)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser.setSizePolicy(sizePolicy_h)
        self.textBrowser.setFixedHeight(18)
        #self.textBrowser.setGeometry(QtCore.QRect(40, 0, 741, 18))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("font: 8pt;background-color: rgba(255, 255, 255, 0); background-color: rgba(255, 255, 255, 0);")
        self.groupBox_4.raise_()
        self.textBrowser.raise_()
        self.toolButton.raise_()

        self.groupBox_4lay.addWidget(self.toolButton)
        self.groupBox_4lay.addSpacing(-8)
        self.groupBox_4lay.addWidget(self.textBrowser)

        self.main_layout.addWidget(self.groupBox_4)


#---------------------图片处理层--------------
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_list)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 768, 394))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.tableWidget_piclayer = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_piclayer.setGeometry(QtCore.QRect(310, 0, 458, 394))
        self.tableWidget_piclayer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_piclayer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_piclayer.horizontalHeader().setVisible(False)
        self.tableWidget_piclayer.verticalHeader().setVisible(False)
        self.tableWidget_piclayer.setAutoScroll(True)
        self.tableWidget_piclayer.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget_piclayer.setLineWidth(0)
        self.tableWidget_piclayer.setObjectName("tableWidget_piclayer")
        self.tableWidget_piclayer.setColumnCount(2)
        self.tableWidget_piclayer.setRowCount(0)
        self.tableWidget_piclayer.setColumnWidth(0, 220)
        self.tableWidget_piclayer.setColumnWidth(1, 220)
        self.toolButton_piclayer = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_piclayer.setGeometry(QtCore.QRect(748, 0, 20, 20))
        self.toolButton_piclayer.setObjectName("toolButton_piclayer")
        self.tableWidget_piclist = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_piclist.setGeometry(QtCore.QRect(0, 0, 311, 394))
        self.tableWidget_piclist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_piclist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_piclist.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_piclist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_piclist.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget_piclist.setObjectName("tableWidget_piclist")
        self.tableWidget_piclist.setColumnCount(2)
        self.tableWidget_piclist.setRowCount(0)
        self.tableWidget_piclist.setColumnWidth(0, 242)
        self.tableWidget_piclist.setColumnWidth(1, 40)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_piclist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_piclist.setHorizontalHeaderItem(1, item)
#-------------------------------------------------------------
#---------------------------图片批量处理-------------------------------
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_list)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 0, 768, 394))
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_6.setContentsMargins(0, 0, 0, 0)

        self.tableWidget_piclayer2 = QtWidgets.QTableWidget(self.groupBox_6)
        self.tableWidget_piclayer2.setGeometry(QtCore.QRect(0, 26, 768, 364))
        self.tableWidget_piclayer2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_piclayer2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_piclayer2.horizontalHeader().setVisible(False)
        self.tableWidget_piclayer2.verticalHeader().setVisible(False)
        self.tableWidget_piclayer2.setAutoScroll(True)
        self.tableWidget_piclayer2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget_piclayer2.setLineWidth(0)
        self.tableWidget_piclayer2.setObjectName("tableWidget_piclayer2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_piclayer2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_piclayer2.setHorizontalHeaderItem(1, item)

        self.groupBox_6b = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_6b.setGeometry(QtCore.QRect(0, 0, 768, 26))
        self.groupBox_6b.setObjectName("groupBox_6b")
        self.groupBox_6b.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6b.setStyleSheet("""
            QGroupBox {
                background-color: lightgray;
            }
        """)

        self.groupBox_6b_bg = QtWidgets.QHBoxLayout(self.groupBox_6b)
        self.groupBox_6b_bg.setObjectName("groupBox_6b_bg")
        self.groupBox_6b_bg.setContentsMargins(0, 0, 0, 0)
        self.button_poster_1h = QtWidgets.QToolButton(self.groupBox_6b)
        self.button_poster_1h.setGeometry(QtCore.QRect(0, 4, 67, 18))
        self.button_poster_1h.setObjectName("button_poster_1h")
        self.button_poster_1v = QtWidgets.QToolButton(self.groupBox_6b)
        self.button_poster_1v.setGeometry(QtCore.QRect(0, 4, 67, 18))
        self.button_poster_1v.setObjectName("button_poster_1v")
        self.button_thumb_1h = QtWidgets.QToolButton(self.groupBox_6b)
        self.button_thumb_1h.setGeometry(QtCore.QRect(0, 4, 67, 18))
        self.button_thumb_1h.setObjectName("button_thumb_1h")
        self.button_thumb_1v = QtWidgets.QToolButton(self.groupBox_6b)
        self.button_thumb_1v.setGeometry(QtCore.QRect(0, 4, 67, 18))
        self.button_thumb_1v.setObjectName("button_thumb_1h")
        self.toolButton_piclayer2 = QtWidgets.QToolButton(self.groupBox_6b)
        self.toolButton_piclayer2.setGeometry(QtCore.QRect(0, 4, 18, 18))
        self.toolButton_piclayer2.setObjectName("toolButton_piclayer2")

        self.groupBox_6b_bg.addStretch(1)
        self.groupBox_6b_bg.addSpacing(18)
        self.groupBox_6b_bg.addWidget(self.button_poster_1h)
        self.groupBox_6b_bg.addSpacing(5)
        self.groupBox_6b_bg.addWidget(self.button_thumb_1h)
        self.groupBox_6b_bg.addSpacing(20)
        self.groupBox_6b_bg.addWidget(self.button_poster_1v)
        self.groupBox_6b_bg.addSpacing(5)
        self.groupBox_6b_bg.addWidget(self.button_thumb_1v)
        self.groupBox_6b_bg.addStretch(1)
        self.groupBox_6b_bg.addWidget(self.toolButton_piclayer2)
#=====================================================================

#==============================修改图片=================================
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_list)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 0, 768, 394))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_7.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_piclayer3 = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_piclayer3.setGeometry(QtCore.QRect(0, 26, 768, 364))
        self.tableWidget_piclayer3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_piclayer3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_piclayer3.horizontalHeader().setVisible(False)
        self.tableWidget_piclayer3.verticalHeader().setVisible(False)
        self.tableWidget_piclayer3.setAutoScroll(True)
        self.tableWidget_piclayer3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget_piclayer3.setLineWidth(0)
        self.tableWidget_piclayer3.setObjectName("tableWidget_piclayer3")
        self.tableWidget_piclayer3.setColumnCount(2)
        self.tableWidget_piclayer3.setRowCount(0)
        self.tableWidget_piclayer3.setColumnWidth(0, 220)
        self.tableWidget_piclayer3.setColumnWidth(1, 220)
        self.toolButton_piclayer3 = QtWidgets.QToolButton(self.groupBox_7)
        self.toolButton_piclayer3.setGeometry(QtCore.QRect(748, 0, 20, 20))
        self.toolButton_piclayer3.setObjectName("toolButton_piclayer3")

        self.groupBox_7b = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_7b.setGeometry(QtCore.QRect(0, 0, 768, 26))
        self.groupBox_7b.setObjectName("groupBox_7b")
        self.groupBox_7b.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7b.setStyleSheet("""
                    QGroupBox {
                        background-color: lightgray;
                    }
                """)

        self.groupBox_7b_bg = QtWidgets.QHBoxLayout(self.groupBox_7b)
        self.groupBox_7b_bg.setObjectName("groupBox_7b_bg")
        self.groupBox_7b_bg.setContentsMargins(0, 0, 0, 0)

        self.groupBox_7b_lable = QtWidgets.QLabel(self.groupBox_7b)
        self.groupBox_7b_lable.setGeometry(QtCore.QRect(0, 0, 768, 18))
        self.groupBox_7b_lable.setObjectName("groupBox_7b_lable")

        self.groupBox_7b_bg.addStretch(1)
        self.groupBox_7b_bg.addSpacing(18)
        self.groupBox_7b_bg.addWidget(self.groupBox_7b_lable)
        self.groupBox_7b_bg.addStretch(1)
        self.groupBox_7b_bg.addWidget(self.toolButton_piclayer3)


#-------------------------------------------------------------------
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setLayout(self.main_layout)
        #MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.button_addfile, self.button_piclayer_open)
        MainWindow.setTabOrder(self.button_piclayer_open, self.button_1button)
        MainWindow.setTabOrder(self.button_1button, self.radioButton_png)
        MainWindow.setTabOrder(self.radioButton_png, self.radioButton_jpg)
        MainWindow.setTabOrder(self.radioButton_jpg, self.radioButton_o_h)
        MainWindow.setTabOrder(self.radioButton_o_h, self.radioButton_o_v)
        MainWindow.setTabOrder(self.radioButton_o_v, self.button_delfiles)
        # MainWindow.setTabOrder(self.button_addpath, self.button_delfiles)
        MainWindow.setTabOrder(self.button_delfiles, self.button_clear)
        MainWindow.setTabOrder(self.button_clear, self.tableWidget_lists)
        MainWindow.setTabOrder(self.tableWidget_lists, self.radio_getposter)
        MainWindow.setTabOrder(self.radio_getposter, self.radio_getframe_num)
        MainWindow.setTabOrder(self.radio_getframe_num, self.line_frame_num)
        MainWindow.setTabOrder(self.line_frame_num, self.radio_getframe_random)
        MainWindow.setTabOrder(self.radio_getframe_random, self.line_limitTime1)
        MainWindow.setTabOrder(self.line_limitTime1, self.line_limitTime2)
        MainWindow.setTabOrder(self.line_limitTime2, self.line_frame_random_num)
        MainWindow.setTabOrder(self.line_frame_random_num, self.line_outPath)
        MainWindow.setTabOrder(self.line_outPath, self.button_getOutPath)
        MainWindow.setTabOrder(self.button_getOutPath, self.button_openOutPath)
        MainWindow.setTabOrder(self.button_openOutPath, self.button_start)
        MainWindow.setTabOrder(self.button_start, self.button_stop)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频帧提取器v1.5"))
        #self.groupBox.setTitle(_translate("MainWindow", "视频列表"))
        item = self.tableWidget_lists.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件"))
        item = self.tableWidget_lists.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "输出地址"))
        item = self.tableWidget_lists.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "帧数/时长"))
        item = self.tableWidget_lists.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "提取区间"))
        item = self.tableWidget_lists.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "状态"))
        self.button_delfiles.setText(_translate("MainWindow", "删除已选视频"))
        self.button_clear.setText(_translate("MainWindow", "清空表格"))
        #self.button_addpath.setText(_translate("MainWindow", "添加视频目录"))
        self.button_addfile.setText(_translate("MainWindow", "添加视频"))
        self.radio_getposter.setText(_translate("MainWindow", "提取封面图片"))
        self.radio_getframe_num.setText(_translate("MainWindow", "抽指定帧"))
        self.radio_getframe_random.setText(_translate("MainWindow", "随机抽帧"))
        self.line_limitTime1.setText(_translate("MainWindow", "0"))
        self.line_limitTime1.setPlaceholderText(_translate("MainWindow", "0"))
        self.line_limitTime2.setText(_translate("MainWindow", "100"))
        self.line_limitTime2.setPlaceholderText(_translate("MainWindow", "100"))
        self.line_frame_num.setText(_translate("MainWindow", "1"))
        self.line_frame_random_num.setText(_translate("MainWindow", "1"))
        self.line_frame_random_num.setPlaceholderText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "随机抽取        张"))
        self.label_isLimitTime.setText(_translate("MainWindow", "从         %帧到         %帧"))
        self.button_confirm.setText(_translate("MainWindow", "确认"))
        self.button_getOutPath.setText(_translate("MainWindow", "浏览"))
        self.line_outPath.setText(_translate("MainWindow", "./outImage"))
        self.label.setText(_translate("MainWindow", "图片保存地址："))
        self.button_openOutPath.setText(_translate("MainWindow", "打开文件夹"))
        self.button_start.setText(_translate("MainWindow", "开始提取"))
        self.button_stop.setText(_translate("MainWindow", "停止提取"))
        self.textBrowser.setText(_translate("MainWindow", "信息栏"))
        self.toolButton.setText(_translate("MainWindow", "打开"))
        self.radioButton_png.setText(_translate("MainWindow", "PNG"))
        self.radioButton_jpg.setText(_translate("MainWindow", "JPG"))
        self.radioButton_o_h.setText(_translate("MainWindow", "横"))
        self.radioButton_o_v.setText(_translate("MainWindow", "竖"))
        self.label_format.setText(_translate("MainWindow", "格式："))
        self.label_hv.setText(_translate("MainWindow", "版式："))
        self.toolButton_piclayer.setText(_translate("MainWindow", "X"))
        self.toolButton_piclayer2.setText(_translate("MainWindow", "X"))
        self.toolButton_piclayer3.setText(_translate("MainWindow", "X"))
        self.button_piclayer_open.setText(_translate("MainWindow", "图片处理"))
        self.button_1button.setText(_translate("MainWindow", "批量处理"))
        self.button_poster_1h.setText(_translate("MainWindow", "批量横封"))
        self.button_poster_1v.setText(_translate("MainWindow", "批量竖封"))
        self.button_thumb_1h.setText(_translate("MainWindow", "批量横缩"))
        self.button_thumb_1v.setText(_translate("MainWindow", "批量竖缩"))

        item = self.tableWidget_piclist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "视频文件"))
        item = self.tableWidget_piclist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "图数"))



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(230, 120)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 80, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accepted)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.rejected)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "啥也不是"))

class Ui_Dialog_Log(object):
    def setupUi(self, Dialog_Log):
        Dialog_Log.setObjectName("Dialog_Log")
        Dialog_Log.resize(712, 365)
        self.textBrowser_log = QtWidgets.QTextBrowser(Dialog_Log)
        self.textBrowser_log.setGeometry(QtCore.QRect(10, 10, 691, 311))
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.textBrowser_log.setStyleSheet("font: 7pt;")
        self.toolButton_close = QtWidgets.QToolButton(Dialog_Log)
        self.toolButton_close.setGeometry(QtCore.QRect(370, 330, 90, 30))
        self.toolButton_close.setObjectName("toolButton_close")
        self.toolButton = QtWidgets.QToolButton(Dialog_Log)
        self.toolButton.setGeometry(QtCore.QRect(260, 330, 90, 30))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Dialog_Log)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Log)

    def retranslateUi(self, Dialog_Log):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Log.setWindowTitle(_translate("Dialog_Log", "Dialog"))
        self.toolButton_close.setText(_translate("Dialog_Log", "关闭"))
        self.toolButton.setText(_translate("Dialog_Log", "保存"))