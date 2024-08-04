# -*- coding:utf-8 -*-
"""
制作人：duckeaty
时间：2023.11.08
v1.3更新：2024.08.04
"""

import configparser
import math
import os
import random
import re
import sys
import shutil
#reload(sys)
#sys.setdefaultencoding('utf-8')
import json
from math import ceil
import time
#import magic
import cv2
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt, QDateTime, QDir
from UI import Ui_MainWindow, Ui_Dialog, Ui_Dialog_Log
from collections import OrderedDict
import threading

# =====================================================================================================
isStart = 0
isThreadAlive = 0
is_log = 0
path_files =[]
file_data_path = "data.json"
piclayer_list_data = []
#[0]=video_oripath
#[1]=video_outpath
#[2]=pic_num
#[3]=pic_paths

perVideo_frames = 1
limit_time1 = 0.0
limit_time2 = 100.0
is_jpg = 1
is_horizon = 1
out_path_save = ""
get_image_type = 3
#1:提取封面
#2:抽指定
#3:随机抽帧
get_image_frame = 1
video_list_data = []
v_poster = "poster"
v_thumb = "thumb"

# [i,video_info]
# video_info
# [0]=video_oripath
# [1]=video_fps
# [2]=video_width
# [3]=video_height
# [4]=video_length
# [5]=video_outpath
# [6]=video_status
# [7]=video_limitframe1
# [8]=video_limitframe2
# 列表数据

# =====================================================================================================


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    statusSignal = pyqtSignal(int,str)
    tableSignal = pyqtSignal(int)

    def __init__(self):
        global perVideo_frames, limit_time1, limit_time2, is_jpg, out_path_save, get_image_type, get_image_frame, video_list_data
        super(MainWindow, self).__init__()
        #self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.groupBox_5.setHidden(True)
        self.button_delfiles.clicked.connect(lambda: self.thread_it(self.d_delfiles))
        self.button_clear.clicked.connect(lambda: self.thread_it(self.d_clear))
        #self.button_addfile.clicked.connect(lambda: self.thread_it(self.d_addfile))
        self.button_addfile.clicked.connect(self.d_addfile)
        #self.button_addpath.clicked.connect(lambda: self.thread_it(self.d_addpath))
        self.radio_getposter.clicked.connect(self.table_refresh)
        self.radio_getframe_num.clicked.connect(self.table_refresh)
        self.radio_getframe_random.clicked.connect(self.table_refresh)
        # self.line_limitTime1.clicked.connect(self.d_limitTime1)
        # self.line_limitTime2.clicked.connect(self.d_limitTime2)
        # self.line_frame_random_num.clicked.connect(self.d_frame_random_num)
        # self.label_isLimitTime.clicked.connect(self.d_clear)
        self.button_getOutPath.clicked.connect(self.d_setOutPath)
        self.button_openOutPath.clicked.connect(self.d_openOutPath)
        self.button_start.clicked.connect(lambda: self.thread_it(self.d_start))
        self.button_stop.clicked.connect(lambda: self.thread_it(self.d_stop("1")))
        self.button_confirm.clicked.connect(lambda: self.thread_it(self.setLimitArea))
        self.line_outPath.textChanged.connect(lambda: self.thread_it(self.d_outPathChange))
        self.toolButton.clicked.connect(self.openLog)
        self.radioButton_png.clicked.connect(self.d_set_png)
        self.radioButton_jpg.clicked.connect(self.d_set_jpg)
        self.radioButton_o_h.clicked.connect(self.d_set_horizon)
        self.radioButton_o_v.clicked.connect(self.d_set_vertical)
        self.button_piclayer_open.clicked.connect(self.d_open_piclayer)
        self.toolButton_piclayer.clicked.connect(self.d_close_piclayer)




        self.setButton_enabled(0)
        self.button_openOutPath.setEnabled(0)
        self.button_start.setEnabled(0)
        #初始化数据-读取配置
        self.dataFile_read()
        self.line_frame_random_num.setText(str(perVideo_frames))
        self.line_limitTime1.setText(str(limit_time1))
        self.line_limitTime2.setText(str(limit_time2))
        if is_jpg == 0:
            self.radioButton_png.setChecked(True)
            self.radioButton_jpg.setChecked(False)
        else:
            self.radioButton_png.setChecked(False)
            self.radioButton_jpg.setChecked(True)
        if is_horizon == 0:
            self.radioButton_o_v.setChecked(True)
            self.radioButton_o_h.setChecked(False)
        else:
            self.radioButton_o_v.setChecked(False)
            self.radioButton_o_h.setChecked(True)
        if out_path_save == "":
            self.line_outPath.setText("./outImage")
        else:
            self.line_outPath.setText(out_path_save)
        if get_image_type == 1:
            self.radio_getposter.setChecked(True)
            self.radio_getframe_num.setChecked(False)
            self.radio_getframe_random.setChecked(False)
        elif get_image_type == 2:
            self.radio_getposter.setChecked(False)
            self.radio_getframe_num.setChecked(True)
            self.radio_getframe_random.setChecked(False)
        else:
            self.radio_getposter.setChecked(False)
            self.radio_getframe_num.setChecked(False)
            self.radio_getframe_random.setChecked(True)
        self.line_frame_num.setText(str(get_image_frame))
        self.table_refresh(1)
        self.setButton_enabled(1)
        self.button_openOutPath.setEnabled(1)
        self.button_start.setEnabled(1)





    def thread_it(self, func, *args):
        global isThreadAlive
        """ 将函数打包进线程 """
        self.myThread = threading.Thread(target=func, args=args)
        self.myThread .daemon = True # 主线程退出就直接让子线程跟随退出,不论是否运行完成。
        self.myThread .start()
        isThreadAlive = self.myThread.is_alive()

    def openLog(self):
        myLog.show()

    def d_open_piclayer(self):
        self.setButton_enabled(0)
        self.button_start.setEnabled(0)
        self.groupBox_5.setHidden(False)
        self.thread_it(self.pic_setList())

    def d_close_piclayer(self):
        global piclayer_list_data
        piclayer_list_data.clear()
        self.groupBox_5.setHidden(True)
        self.setButton_enabled(1)
        self.button_start.setEnabled(1)

    def pic_setList(self):
        global video_list_data, piclayer_list_data
        piclayer_list_data.clear()
        #图片处理层列表生成
        for i in range(len(video_list_data)):
            temp_file = self.getPicNum(video_list_data[i][5])
            temp_data = [video_list_data[i][0], video_list_data[i][5], temp_file[0], temp_file[1]]
            piclayer_list_data.append(temp_data)
        piclayer_list_data.sort()
        #开始生成列表
        self.tableWidget_piclist.setRowCount(0)
        self.tableWidget_piclist.setStyleSheet("font: 7pt;")
        # print(video_list_data)
        for i in range(len(piclayer_list_data)):
            self.tableWidget_piclist.setRowCount(i + 1)
            self.tableWidget_piclist.setItem(i, 0, QtWidgets.QTableWidgetItem(piclayer_list_data[i][0]))
            self.tableWidget_piclist.setItem(i, 1, QtWidgets.QTableWidgetItem(str(piclayer_list_data[i][2])))
            self.tableWidget_piclist.item(i, 1).setTextAlignment(-4)

            QtWidgets.QApplication.processEvents()
        self.tableWidget_piclist.itemClicked.connect(self.showPics)

    def showPics(self, Item):
        global piclayer_list_data
        try:
            row = Item.row()
        except Exception as e:
            #print("获取点击失败！")
            row = 0
        self.tableWidget_piclayer.setRowCount(0)
        #print("row"+str(row))
        pic_num = piclayer_list_data[row][2]
        pic_oripath = os.path.dirname(piclayer_list_data[row][0])
        pic_paths = piclayer_list_data[row][3]
        #print(pic_num)
        #print(pic_oripath)
        #print(pic_paths)
        i_row = math.floor(pic_num / 2)+1
        l_col = pic_num % 2
        #print(l_col)
        #print("-----------------")
        #print(piclayer_list_data)
        for i in range(i_row):
            #print(i)
            if i == i_row - 1:
                i_col = l_col
            else:
                i_col = 2
            #print(i_col)

            for j in range(i_col):
                #print(str(i) + "/" + str(j))
                #print(pic_paths[i*2+j])
                t = i*2+j
                pixmap = QtGui.QPixmap(pic_paths[t])
                pix = pixmap.scaled(210, 119, Qt.KeepAspectRatio)
                p_widget = QtWidgets.QWidget()
                p_widget.setGeometry(QtCore.QRect(0, 0, 210, 119))
                #widget.setObjectName("widget")
                p_toolButton = QtWidgets.QToolButton(p_widget)
                p_toolButton.setGeometry(QtCore.QRect(178, 100, 15, 15))
                p_toolButton.setText("封")
                p_toolButton.setStyleSheet("font:7pt;")
                p_toolButton.clicked.connect(lambda :self.p_send_poster(row))
                #toolButton.setObjectName("toolButton")
                p_toolButton_2 = QtWidgets.QToolButton(p_widget)
                p_toolButton_2.setGeometry(QtCore.QRect(194, 100, 15, 15))
                p_toolButton_2.setText("缩")
                p_toolButton_2.setStyleSheet("font:7pt;")
                p_toolButton_2.clicked.connect(lambda :self.p_send_thumb(row))
                #toolButton_2.setObjectName("toolButton_2")
                p_label = QtWidgets.QLabel(p_widget)
                p_label.setGeometry(QtCore.QRect(0, 0, 210, 119))
                p_label.setPixmap(pix)
                #label.setObjectName("label")
                p_label.raise_()
                p_toolButton.raise_()
                p_toolButton_2.raise_()
                self.tableWidget_piclayer.setRowCount(i+1)
                self.tableWidget_piclayer.setRowHeight(i,119)
                self.tableWidget_piclayer.setCellWidget(i,j,p_widget)

    def p_send_poster(self, v_index):
        global piclayer_list_data
        button = self.sender()
        p_row = self.tableWidget_piclayer.indexAt(button.parentWidget().pos()).row()
        p_col = self.tableWidget_piclayer.indexAt(button.parentWidget().pos()).column()
        p_index = p_row*2+p_col
        #print("v_index/row/col/p_index:"+str(v_index)+":"+str(p_row)+"/"+str(p_col)+"/"+str(p_index))
        file_old = piclayer_list_data[v_index][3][p_index]
        file_ext = os.path.splitext(file_old)[-1]
        file_name, ext = os.path.splitext(piclayer_list_data[v_index][0])
        file_name_new = file_name+"-poster"+file_ext
        shutil.copyfile(file_old,file_name_new)
        myLog.msgSignal.emit("成功导出封面文件: [ "+file_name_new+" ]")

    def p_send_thumb(self, v_index):
        global piclayer_list_data
        button = self.sender()
        p_row = self.tableWidget_piclayer.indexAt(button.parentWidget().pos()).row()
        p_col = self.tableWidget_piclayer.indexAt(button.parentWidget().pos()).column()
        p_index = p_row * 2 + p_col
        file_old = piclayer_list_data[v_index][3][p_index]
        file_ext = os.path.splitext(file_old)[-1]
        file_name, ext = os.path.splitext(piclayer_list_data[v_index][0])
        file_name_new = file_name + "-thumb" + file_ext
        shutil.copyfile(file_old, file_name_new)
        myLog.msgSignal.emit("成功导出缩略图文件: [ " + file_name_new + " ]")

    def getPicNum(self,path):
        if os.path.isdir(path):
            #temp_data = [f for f in os.listdir(path) if os.path.isfile(f)]
            temp_data = os.listdir(path)
            temp_num = 0
            temp_filename = []
            #print(temp_data)
            for i in range(len(temp_data)):
                file_name = temp_data[i].split(".")
                file_type = file_name[len(file_name) - 1]
                if file_type == "jpg" or file_type == "png":
                    temp_num = temp_num + 1
                    temp_filename.append(path+"/"+temp_data[i])
            return [temp_num, temp_filename]
        else:
            return [0,[]]



    def dataFile_read(self):
        global file_data_path, perVideo_frames, limit_time1, limit_time2, is_jpg, is_horizon, out_path_save, get_image_type, get_image_frame, v_poster, v_thumb, video_list_data
        #数据读取
        if os.path.exists(file_data_path):
            with open(file_data_path, "r") as file:
                file_data = json.load(file)
                file.close()
                perVideo_frames = file_data[0]
                limit_time1 = file_data[1]
                limit_time2 = file_data[2]
                is_jpg = file_data[3]
                is_horizon = file_data[4]
                out_path_save = file_data[5]
                get_image_type = file_data[6]
                get_image_frame = file_data[7]
                v_poster = file_data[8]
                v_thumb = file_data[9]
                video_list_data = file_data[10]

    def dataFile_write(self):
        global file_data_path, perVideo_frames, limit_time1, limit_time2, is_jpg, is_horizon, out_path_save, get_image_type, get_image_frame, v_poster, v_thumb, video_list_data
        #file_data = []
        file_data = [perVideo_frames, limit_time1, limit_time2, is_jpg, is_horizon, out_path_save, get_image_type, get_image_frame, v_poster, v_thumb, video_list_data]

        #数据写入
        with open(file_data_path, "w") as file:
            json.dump(file_data,file)
            file.close()

    def setButton_enabled(self,isEnable):
        global get_image_frame, perVideo_frames
        self.button_delfiles.setEnabled(isEnable)
        self.button_clear.setEnabled(isEnable)
        self.button_addfile.setEnabled(isEnable)
        self.radio_getposter.setEnabled(isEnable)
        self.radio_getframe_num.setEnabled(isEnable)
        self.radio_getframe_random.setEnabled(isEnable)
        self.line_limitTime1.setEnabled(isEnable)
        self.line_limitTime2.setEnabled(isEnable)
        self.line_frame_random_num.setEnabled(isEnable)
        self.label_3.setEnabled(isEnable)
        self.label.setEnabled(isEnable)
        self.label_isLimitTime.setEnabled(isEnable)
        self.button_getOutPath.setEnabled(isEnable)
        #self.button_openOutPath.setEnabled(isEnable)
        #self.button_start.setEnabled(isEnable)
        self.button_confirm.setEnabled(isEnable)
        self.line_outPath.setEnabled(isEnable)
        self.radioButton_png.setEnabled(isEnable)
        self.radioButton_jpg.setEnabled(isEnable)
        self.label_format.setEnabled(isEnable)
        self.groupBox_hv.setEnabled(isEnable)
        #self.button_addpath.setEnabled(isEnable)


    def changeStatus(self,row,status):
        #状态列信息更新
        self.tableWidget_lists.setItem(row, 4, QtWidgets.QTableWidgetItem(status))
        self.tableWidget_lists.item(row, 4).setTextAlignment(-4)


    def table_refresh(self,isFresh):
        #列表刷新信号处理
        if isFresh == "":
            isFresh = 1
        global limit_time1, limit_time2, video_list_data, perVideo_frames, get_image_frame, get_image_type
        out_path = self.getOutPath()
        temp_1 = self.line_frame_random_num.text()
        temp_2 = self.line_frame_num.text()
        if self.radio_getposter.isChecked() == True:
            get_image_type = 1
        elif self.radio_getframe_num.isChecked() == True:
            get_image_type = 2
        else:
            get_image_type = 3

        if temp_1.isdigit():
            perVideo_frames = int(temp_1)
        else:
            perVideo_frames = 1
        if temp_2.isdigit():
            get_image_frame = int(temp_2)
        else:
            get_image_frame = 1


        if isFresh:
            self.tableWidget_lists.setRowCount(0)
            self.tableWidget_lists.setStyleSheet("font: 7pt;")
            #print(video_list_data)
            for i in range(len(video_list_data)):
                temp_path = out_path + "/" + os.path.basename(video_list_data[i][0])[:os.path.basename(video_list_data[i][0]).rfind(".")]
                temp_path = temp_path.replace("//", "/outImage/")
                temp_path = temp_path.replace("\\", "/")
                #print(temp_path)
                self.tableWidget_lists.setRowCount(i + 1)
                limit_frame1 = round(float(self.line_limitTime1.text()) / 100 * video_list_data[i][4])
                limit_frame2 = round(float(self.line_limitTime2.text()) / 100 * video_list_data[i][4])
                video_list_data[i][5] = temp_path
                video_list_data[i][7] = limit_frame1
                video_list_data[i][8] = limit_frame2
                self.tableWidget_lists.setItem(i, 0, QtWidgets.QTableWidgetItem(video_list_data[i][0]))
                self.tableWidget_lists.setItem(i, 1, QtWidgets.QTableWidgetItem(temp_path))
                temp_time = video_list_data[i][4] / video_list_data[i][1]
                temp_time_hms = str(self.sec_to_time(temp_time))
                self.tableWidget_lists.setItem(i, 2, QtWidgets.QTableWidgetItem(str(round(video_list_data[i][4])) + "帧\n" + temp_time_hms))
                self.tableWidget_lists.item(i, 2).setTextAlignment(-4)
                temp_frame_config = str(limit_frame1) + " - " + str(limit_frame2) + "帧"

                temp_time1 = self.sec_to_time(limit_frame1 / video_list_data[i][1])
                temp_time2 = self.sec_to_time(limit_frame2 / video_list_data[i][1])
                temp_time1 = str(temp_time1)
                temp_time2 = str(temp_time2)
                temp_frame_config = temp_frame_config + "\n" + temp_time1 + " - " + temp_time2
                if self.radio_getposter.isChecked():
                    temp_frame_config = "提取封面"
                elif self.radio_getframe_num.isChecked():
                    temp_frame_config = self.line_frame_num.text()
                    if temp_frame_config == "":
                        temp_frame_config = "1"
                        self.line_frame_num.setText("1")
                    if int(temp_frame_config) > video_list_data[i][4]:
                        temp_frame_config = str(video_list_data[i][4])
                        self.line_frame_num.setText(str(video_list_data[i][4]))
                self.tableWidget_lists.setItem(i, 3, QtWidgets.QTableWidgetItem(temp_frame_config))
                self.tableWidget_lists.item(i, 3).setTextAlignment(-4)
                self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem(video_list_data[i][6]))
                self.tableWidget_lists.item(i, 4).setTextAlignment(-4)
                QtWidgets.QApplication.processEvents()
            self.dataFile_write()



    def d_delfiles(self):
        global video_list_data
        self.setButton_enabled(0)
        # 在列表中清除选定文件
        #row_count = self.tableWidget_lists.model().rowCount()

        selected_rows = self.tableWidget_lists.selectionModel().selectedRows()
        selected_rows.sort(reverse=True)
        for index in selected_rows:
            row_index = index.row()
            myLog.msgSignal.emit("清除项目[ " + video_list_data[row_index][0] + " ]")
            del video_list_data[row_index]
        #self.table_refresh(1)
        self.dataFile_write()
        self.tableSignal.emit(1)
        self.setButton_enabled(1)

    def d_outPathChange(self):
        global video_list_data
        self.setButton_enabled(0)
        #self.table_refresh(1)
        self.tableSignal.emit(1)
        #myLog.msgSignal.emit("导出目录变更为：[ "+self.line_outPath.text()+" ]")
        self.setButton_enabled(1)

    def d_clear(self):
        global video_list_data
        self.setButton_enabled(0)
        # 清空列表
        if self.button_start.isHidden() == False:
            self.tableWidget_lists.setRowCount(0)
            video_list_data = []
            myLog.msgSignal.emit("清空列表")
            self.dataFile_write()
        self.setButton_enabled(1)

    def d_addfile(self):
        global video_list_data
        self.setButton_enabled(0)
        self.button_start.setEnabled(0)

        # 添加文件
        # 获取提取目录
        out_path = self.getOutPath()
        file_path_list, _ = QtWidgets.QFileDialog.getOpenFileNames(None, '打开文件', '', 'Video files (*.mp4 *.mkv *.mpg *.mpeg *.avi *.rmvb *.wmv *.mov *.flv *.ts *.webm *.m4v *.m2ts *.asf);;All files (*.*)')
        # print("file_path_list:"+file_path_list[0])
        #path_list_count = len(file_path_list)
        #print(path_list_count)
        #for i in range(path_list_count):
        #    list_data.append(file_path_list[i])
        #print(list_data)
        #list_data2 = list(set(list_data))
        #list_data2.sort(key=list_data.index)
        self.thread_it(self.setNewList(out_path,file_path_list))
        #self.setList(out_path, list_data2)
        self.tableSignal.emit(1)
        self.setButton_enabled(1)
        self.button_start.setEnabled(1)

    #def d_addpath(self):
    #    self.setButton_enabled(0)
    #    # 添加目录
    #    folder_dialog = QtWidgets.QFileDialog()
    #    folder_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
    #    folder_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
    #    folder_dialog.setDirectory('./')  # 设置默认文件夹路径
    #    if folder_dialog.exec_() == QtWidgets.QFileDialog.Accepted:
    #        folder_path = folder_dialog.selectedFiles()[0]
    #        print("选择的文件夹路径：", folder_path)
    #    self.setButton_enabled(1)

    def setNewList(self, out_path, listdata):
        global limit_time1
        global limit_time2
        global video_list_data
        self.setButton_enabled(0)
        row_count_exist = len(video_list_data)
        #listdata去重
        templist = []
        for i in range(row_count_exist):
            templist.append(video_list_data[i][0])
        for i in range(len(listdata)):
            templist.append(listdata[i])
        #print(templist)
        templist2 = list(OrderedDict.fromkeys(templist))
        #print(templist2)
        for i in range(row_count_exist):
            del templist2[0]
        #self.tableWidget_lists.setRowCount(0)
        #self.tableWidget_lists.setStyleSheet("font: 7pt;")
        #self.tableWidget_lists.horizontalHeader().setStyleSheet("")
        # video_list_data.clear()
        for j in range(len(templist2)):
            i = row_count_exist + j
            QtWidgets.QApplication.processEvents()
            # print(str(i+1)+"|"+list_data2[i]+"|"+"输出"+"|"+"未提取")
            self.tableWidget_lists.setRowCount(i + 1)

            temp_data = self.getVideoInfo(templist2[j])
            #self.tableWidget_lists.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
            self.tableWidget_lists.setItem(i, 0, QtWidgets.QTableWidgetItem(templist2[j]))
            temp_path = out_path + "/" + QDir.fromNativeSeparators(os.path.basename(templist2[j])[:os.path.basename(templist2[j]).rfind(".")])
            temp_path = temp_path.replace("//", "/outImage/")
            temp_path = temp_path.replace("\\","/")
            self.tableWidget_lists.setItem(i, 1, QtWidgets.QTableWidgetItem(temp_path))
            temp_data.append(temp_path)
            temp_frames = round(temp_data[4])
            temp_info = str(temp_frames)
            temp_time = temp_data[4] / temp_data[1]
            temp_time_hms = str(self.sec_to_time(temp_time))
            # print(temp_time_hms)
            self.tableWidget_lists.setItem(i, 2, QtWidgets.QTableWidgetItem(temp_info + "帧\n" + temp_time_hms))
            self.tableWidget_lists.item(i, 2).setTextAlignment(-4)
            self.tableWidget_lists.setItem(i, 2, QtWidgets.QTableWidgetItem(temp_info + "帧\n" + temp_time_hms))

            temp_frame1 = round(limit_time1 / 100 * temp_frames)
            temp_frame2 = round(limit_time2 / 100 * temp_frames)
            temp_frame_config = str(temp_frame1) + " - " + str(temp_frame2) + "帧"
            temp_time1 = self.sec_to_time(temp_frame1 / temp_data[1])
            temp_time2 = self.sec_to_time(temp_frame2 / temp_data[1])
            temp_time1 = str(temp_time1)
            temp_time2 = str(temp_time2)
            temp_frame_config = temp_frame_config + "\n" + temp_time1 + " - " + temp_time2
            if self.radio_getposter.isChecked():
                temp_frame_config = "提取封面"
            elif self.radio_getframe_num.isChecked():
                temp_frame_config = self.line_frame_num.text()
                if temp_frame_config == "":
                    temp_frame_config = "1"
                    self.line_frame_num.setText("1")
                if int(temp_frame_config) > temp_frames:
                    temp_frame_config = str(temp_frames)
                    self.line_frame_num.setText(str(temp_frames))

            self.tableWidget_lists.setItem(i, 3, QtWidgets.QTableWidgetItem(temp_frame_config))
            self.tableWidget_lists.item(i, 3).setTextAlignment(-4)
            temp_status = "未提取"
            self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem(temp_status))
            temp_data.append(temp_status)
            temp_data.append(temp_frame1)
            temp_data.append(temp_frame2)
            self.tableWidget_lists.item(i, 4).setTextAlignment(-4)
            video_list_data.append(temp_data)
            myLog.msgSignal.emit("增加项目" + str(i + 1) + ": [ " + temp_data[0] + " ] 成功")
            QtWidgets.QApplication.processEvents()
        myLog.msgSignal.emit("本次共增加项目：" + str(len(templist2)) + "个")
        self.dataFile_write()
        self.setButton_enabled(1)

    def d_setOutPath(self):
        global out_path_save
        self.setButton_enabled(0)
        # 设置输出目录
        folder_dialog = QtWidgets.QFileDialog()
        folder_dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        folder_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
        folder_dialog.setDirectory('./')  # 设置默认文件夹路径
        if folder_dialog.exec_() == QtWidgets.QFileDialog.Accepted:
            folder_path = folder_dialog.selectedFiles()[0]
            folder_path = folder_path + "/outImage"
            folder_path = folder_path.replace("//", "/")
            folder_path = folder_path.replace("\\", "/")
            #print("选择的文件夹路径：", folder_path)
            self.line_outPath.setText(folder_path)
            out_path_save = folder_path
            myLog.msgSignal.emit("导出目录变更为：[ " + folder_path + " ]")
        self.dataFile_write()
        self.setButton_enabled(1)

    def d_openOutPath(self):
        #self.setButton_enabled(0)
        # 打开输出目录
        out_path = self.getOutPath()
        out_path2 = self.replace_last(out_path, "/outImage", "")
        # print("new_path :"+out_path2)
        if os.path.isdir(out_path):
            os.startfile(out_path)  # 如果是文件夹则打开
            myLog.msgSignal.emit("打开目录：[ " + out_path + " ]")
        elif os.path.isdir(out_path2):
            os.startfile(out_path2)
            myLog.msgSignal.emit("所选目录未创建，打开上级目录：[ " + out_path2 + " ]")
        else:
            #print("不是文件夹路径:" + out_path)
            myLog.msgSignal.emit("打开目录失败：[ " + out_path + " ]目录非法")
        #self.setButton_enabled(1)


    def d_start(self):
        self.setButton_enabled(0)
        global isStart
        isStart = 1
        self.button_stop.setHidden(False)
        self.button_start.setHidden(True)
        #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        if self.radio_getposter.isChecked():
            myLog.msgSignal.emit("开始提取图片，模式: [提取封面]")
            aa = self.d_start_poster()
        elif self.radio_getframe_num.isChecked():
            myLog.msgSignal.emit("开始提取图片，模式: [提取指定帧]")
            aa = self.d_start_frame()
        elif self.radio_getframe_random.isChecked():
            myLog.msgSignal.emit("开始提取图片，模式: [提取随机帧]")
            aa = self.d_start_area()
        else:
            return True
        if aa == True:
            #print("提取完成！")
            myLog.msgSignal.emit("提取完成")
            # time.sleep(1)
            isStart = 0
            self.d_stop("3")
            #self.table_refresh(1)
            #self.tableSignal.emit(1)
            #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
        self.dataFile_write()
        self.setButton_enabled(1)

    def d_start_poster(self):
        global isStart
        global perVideo_frames
        global video_list_data
        isStart = 1
        image_format = self.get_image_format()
        image_hv = self.get_image_hv()
        # 开始提取图片
        #print(video_list_data)
        out_path = self.getOutPath()
        #print(out_path)
        # 开始处理
        # 获取每视频提取张数
        temp_nums = 1
        for i in range(len(video_list_data)):
            if isStart == 0:
                break
            # 状态栏设置
            self.statusSignal.emit(i,"0/1")
            #self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("0/1"))
            video_list_data[i][6] = "0/1"  # 更新video_list_data对应的状态
            # 创建目录
            is_mkdir = self.mkdir(video_list_data[i][5])
            # 判断目录是否创建成功
            if not is_mkdir:
                self.d_stop("2")
                myDiag.ui.setMsg("目录 [:" + video_list_data[i][5] + "] 创建失败，停止提取！")
                return False
            ori_path = video_list_data[i][0]
            out_path = video_list_data[i][5]
            isImage_success = self.getImage(ori_path, out_path, 1, image_format, image_hv)
            if isImage_success:
                #print("提取成功！")
                myLog.msgSignal.emit("[ " + out_path + "/1"+image_format+" ] 提取成功")
                self.statusSignal.emit(i, "完成")
                # self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("1/1"))
                video_list_data[i][6] = "完成"
            else:
                #print("提取失败！")
                myLog.msgSignal.emit("[ " + out_path + "/1"+image_format+" ] 提取失败")
                self.statusSignal.emit(i, "失败")
                # self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("1/1"))
                video_list_data[i][6] = "失败"
            # 状态栏更新
            #self.statusSignal.emit(i,"完成")
            #self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("1/1"))
            #video_list_data[i][6] = "完成"
            QtWidgets.QApplication.processEvents()
        return True

    def d_start_frame(self):
        global isStart
        global perVideo_frames
        global video_list_data
        isStart = 1
        image_format = self.get_image_format()
        image_hv = self.get_image_hv()
        # 开始提取图片
        #print(video_list_data)
        out_path = self.getOutPath()
        #print(out_path)
        # 开始处理
        # 获取每视频提取张数
        temp_nums = int(self.line_frame_num.text())
        for i in range(len(video_list_data)):
            if isStart == 0:
                break
            if temp_nums >= video_list_data[i][4]:
                temp_nums = video_list_data[i][4] - 1
            # 状态栏设置
            self.statusSignal.emit(i,"0/1")
            #self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("0/1"))
            video_list_data[i][6] = "0/1"  # 更新video_list_data对应的状态
            # 创建目录
            is_mkdir = self.mkdir(video_list_data[i][5])
            # 判断目录是否创建成功
            if not is_mkdir:
                self.d_stop("2")
                myDiag.ui.setMsg("目录 [:" + video_list_data[i][5] + "] 创建失败，停止提取！")
                return False
            ori_path = video_list_data[i][0]
            out_path = video_list_data[i][5]
            #print("ori_path:" + ori_path + "/out_path:" + out_path + "/frames:" + str(temp_nums))
            isImage_success = self.getImage(ori_path, out_path, temp_nums, image_format, image_hv)
            if isImage_success:
                #print("提取成功！")
                myLog.msgSignal.emit("[ " + out_path + "/" + str(temp_nums) +image_format+" ] 提取成功")
                self.statusSignal.emit(i, "成功\n帧" + str(temp_nums))
                # self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("1/1"))
                video_list_data[i][6] = "成功\n帧" + str(temp_nums)
            else:
                #print("提取失败！")
                myLog.msgSignal.emit("[ " + out_path + "/" + str(temp_nums) +image_format+" ] 提取失败")
                self.statusSignal.emit(i, "失败\n帧" + str(temp_nums))
                # self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("1/1"))
                video_list_data[i][6] = "失败\n帧" + str(temp_nums)
            # 状态栏更新
            #self.statusSignal.emit(i,"成功\n帧"+str(temp_nums))
            #self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("1/1"))
            #video_list_data[i][6] = "成功\n帧"+str(temp_nums)
            QtWidgets.QApplication.processEvents()
        return True

    def d_start_area(self):
        global isStart
        global perVideo_frames
        global video_list_data
        isStart = 1
        #threads = []
        # 开始处理
        # 获取每视频提取张数
        temp_nums = self.line_frame_random_num.text()
        if temp_nums.isdigit():
            perVideo_frames = int(temp_nums)
        else:
            self.line_frame_random_num.setText(str(perVideo_frames))
        #print("提取张数：" + str(perVideo_frames))
        myLog.msgSignal.emit("每视频提取 " + str(perVideo_frames) + " 帧")
        for i in range(len(video_list_data)):
            if isStart == 0:
                break
            self.d_start_area_getImage(i,perVideo_frames)
        #    thread = threading.Thread(target=self.d_start_area_getImage, args=(i, temp_nums,))
        #    threads.append(thread)
        #    thread.start()
        #for thread in threads:
        #    thread.join()
        return True

    def d_start_area_getImage(self, i, temp_nums):
        global isStart
        global perVideo_frames
        global video_list_data
        out_path = self.getOutPath()
        image_format = self.get_image_format()
        image_hv = self.get_image_hv()
        num_success = 0
        num_failed = 0
        #if isStart == 0:
        #    print("暂停！")
        #    return True
        # 状态栏设置

        #self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem("0/" + str(perVideo_frames)))
        self.statusSignal.emit(i,"0/" + str(perVideo_frames))
        video_list_data[i][6] = "0/" + str(perVideo_frames)  # 更新video_list_data对应的状态
        # 创建目录
        is_mkdir = self.mkdir(video_list_data[i][5])
        # 判断目录是否创建成功
        if not is_mkdir:
            self.d_stop("2")
            myDiag.ui.setMsg("目录 [:" + video_list_data[i][5] + "] 创建失败，停止提取！")
            myLog.msgSignal.emit("[ " + out_path + " ] 提取失败")
            return False
        for j in range(perVideo_frames):
            if isStart == 0:
                break
            #QtWidgets.QApplication.processEvents()
            # 提取
            ori_path = video_list_data[i][0]
            out_path = video_list_data[i][5]
            limit_frame1 = video_list_data[i][7]
            limit_frame2 = video_list_data[i][8]
            if limit_frame2 >= video_list_data[i][4]:
                limit_frame2 = limit_frame2 - 1
            frame_random_num = self.getRandom(limit_frame1, limit_frame2)
            isImage_success = self.getImage(ori_path, out_path, frame_random_num, image_format, image_hv)
            if isImage_success:
                num_success = num_success + 1
                #print("第 " + str(j + 1) + " 张提取成功！")
                myLog.msgSignal.emit("第 "+str(j+1)+" 张: [ " + out_path +"/"+ str(frame_random_num) + image_format+" ] 提取成功")
            else:
                num_failed = num_failed + 1
                #print("第 " + str(j + 1) + " 张提取失败！")
                myLog.msgSignal.emit("第 "+str(j+1)+" 张: [ " + out_path +"/"+ str(frame_random_num) + image_format+" ] 提取失败")
            # 状态栏更新
            #self.changeStatus(i,str(j + 1) + "/" + str(perVideo_frames))
            self.statusSignal.emit(i,str(j + 1) + "/" + str(perVideo_frames))
            #self.tableWidget_lists.setItem(i, 4, QtWidgets.QTableWidgetItem(str(j + 1) + "/" + str(perVideo_frames)))
            video_list_data[i][6] = str(j) + "/" + str(perVideo_frames)
            if perVideo_frames == j + 1:
                #self.changeStatus(i,"完成\n" + str(perVideo_frames))
                #self.statusSignal.emit(i, "完成\n" + str(perVideo_frames))
                self.statusSignal.emit(i,"完成\n" + str(num_success) + "/" + str(perVideo_frames))
                myLog.msgSignal.emit("[ " + out_path +" ] 成功提取"+str(num_success) + "/" + str(perVideo_frames) + "张")
                video_list_data[i][6] = "完成\n" + str(num_success) + "/" + str(perVideo_frames)
            QtWidgets.QApplication.processEvents()

    def getImage(self, ori_path, out_path, num_random, image_format, image_hv):
        video = cv2.VideoCapture(ori_path)
        video.set(cv2.CAP_PROP_POS_FRAMES, num_random)
        save_path = out_path + "/" + str(num_random) + image_format
        #print(save_path)
        success, image = video.read()
        if success == False:
            video.release()
            return False
        p_size = image.shape
        v_width = p_size[1]
        v_height = p_size[0]
        t_width = 0
        t_height = 0
        if image_hv == "h":
            if v_width / v_height >= 16 / 9:
                t_width = round(16 / 9 * v_height)
                t_height = v_height
            else:
                t_width = v_width
                t_height = round(9 / 16 * v_width)
            t_x = round((v_width - t_width) / 2)
            t_y = round((v_height - t_height) / 2)
            image_crop_h = image[t_y:(t_height + t_y), t_x:(t_width + t_x)]
        else:
            if v_width / v_height >= 9 / 16:
                t_width = round(9 / 16 * v_height)
                t_height = v_height
            else:
                t_width = v_width
                t_height = round(16 / 9 * v_width)
            t_x = round((v_width - t_width) / 2)
            t_y = round((v_height - t_height) / 2)
            image_crop_v = image[t_y:(t_height + t_y), t_x:(t_width + t_x)]
            if v_width / v_height >= 16 / 9:
                t_width = round(16 / 9 * v_height)
                t_height = v_height
            else:
                t_width = v_width
                t_height = round(9 / 16 * v_width)
            t_x = round((v_width - t_width) / 2)
            t_y = round((v_height - t_height) / 2)
            image_crop_h = image[t_y:(t_height + t_y), t_x:(t_width + t_x)]
        #print(str(t_x)+","+str(t_y)+"/"+str(t_width+t_x)+","+str(t_height+t_y))
        if image_hv == "h":
            save_path_h = out_path + "/1_" + str(num_random) + "_h" + image_format
            cv2.imencode(image_format, image_crop_h)[1].tofile(save_path_h)
        else:
            save_path_h = out_path + "/0_" + str(num_random) + "_h" + image_format
            save_path_v = out_path + "/0_" + str(num_random) + "_v" + image_format
            cv2.imencode(image_format, image_crop_h)[1].tofile(save_path_h)
            cv2.imencode(image_format, image_crop_v)[1].tofile(save_path_v)
        video.release()
        is_success = False
        if image_hv == "h":
            if os.path.exists(save_path_h):
                is_success = True
        else:
            if os.path.exists(save_path_h) and os.path.exists(save_path_v):
                is_success = True
        return is_success

    def d_set_jpg(self):
        global is_jpg
        is_jpg = 1
        self.dataFile_write()
        myLog.msgSignal.emit("图片保存格式更改为：JPG")

    def d_set_png(self):
        global is_jpg
        is_jpg = 0
        self.dataFile_write()
        myLog.msgSignal.emit("图片保存格式更改为：PNG")

    def d_set_horizon(self):
        global is_horizon
        is_horizon = 1
        self.dataFile_write()
        myLog.msgSignal.emit("封面图片保存版式更改为：横版")

    def d_set_vertical(self):
        global is_horizon
        is_horizon = 0
        self.dataFile_write()
        myLog.msgSignal.emit("封面图片保存版式更改为：竖版")

    def get_image_format(self):
        global is_jpg
        if is_jpg == 0:
            return ".png"
        elif is_jpg == 1:
            return ".jpg"
        else:
            return ".png"

    def get_image_hv(self):
        global is_horizon
        if is_horizon == 0:
            return "v"
        elif is_horizon == 1:
            return "h"
        else:
            return "h"
    def mkdir(self, path):
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            #print("目录 [" + path + "] 创建成功！")
            myLog.msgSignal.emit("目录 [ " + path + " ] 创建成功")
        else:
            #print("目录 [" + path + "] 已经存在！")
            myLog.msgSignal.emit("目录 [ " + path + " ] 已经存在，跳过创建")
        return True

    def d_stop(self,type):
        global isStart
        global isCapCompleted
        # 停止处理
        if type != "2" and type !="3":
            isStart = 0
            myLog.msgSignal.emit("用户停止提取")
            self.button_stop.setEnabled(False)
        elif type == "2" or type == "3":
            isStart = 0
            self.button_stop.setEnabled(True)
            self.button_stop.setHidden(True)
            self.button_start.setHidden(False)
            self.tableWidget_lists.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
            if type == "2":
                myLog.msgSignal.emit("提取中断，成功停止提取进程")
            elif type == "3":
                myLog.msgSignal.emit("提取完成，提取进程结束")
            self.setButton_enabled(1)

    def getOutPath(self):
        current_path = os.getcwd()
        # print(current_path)
        out_path = self.line_outPath.text()
        if out_path == "./outImage":
            out_path_2 = current_path + "/outImage"
            return out_path_2
        else:
            return out_path


    def getVideoInfo(self, ori_path):
        video_file = cv2.VideoCapture(ori_path)
        video_fps = video_file.get(cv2.CAP_PROP_FPS)
        video_width = int(video_file.get(cv2.CAP_PROP_FRAME_WIDTH))
        video_height = int(video_file.get(cv2.CAP_PROP_FRAME_HEIGHT))
        video_length = round(video_file.get(cv2.CAP_PROP_FRAME_COUNT))
        video_info = []
        video_info.append(ori_path)
        video_info.append(video_fps)
        video_info.append(video_width)
        video_info.append(video_height)
        video_info.append(video_length)
        video_file.release()
        return video_info


    def replace_last(self, string, old, new):
        #print(string)
        index = string.rfind(old)
        if index == -1:
            return string
        else:
            return string[:index] + new + string[index + len(old):]

    def sec_to_time(self, sec):
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        return "%02d:%02d:%02d" % (h, m, s)

    def getLImitArea(self):
        limit_time1 = self.line_limitTime1.text()
        limit_time2 = self.line_limitTime1.text()
        limit_time = [limit_time1, limit_time2]
        return (limit_time)

    def setLimitArea(self):
        self.setButton_enabled(0)
        global limit_time1, limit_time2, perVideo_frames, get_image_frame
        pattern_float = "^[0-9]+(.[0-9]+)?$"
        #print("time1:" + self.line_limitTime1.text() + "/time2:" + self.line_limitTime2.text())

        # 处理time1
        if self.line_limitTime1.text() == "":
            self.line_limitTime1.setText("0")
            limit_time1 = 0
        if self.line_limitTime2.text() == "":
            self.line_limitTime2.setText("100")
            limit_time2 = 100.00
        if re.match(pattern_float, self.line_limitTime1.text()):
            if float(self.line_limitTime1.text()) < 0:
                self.line_limitTime1.setText("0")
                limit_time1 = 0
            if float(self.line_limitTime1.text()) > 99.00:
                self.line_limitTime1.setText("99")
                limit_time1 = 99.00
            self.line_limitTime1.setText(str(self.line_limitTime1.text().replace("+", "")))
            limit_time1 = float(self.line_limitTime1.text().replace("+", ""))
        else:
            self.line_limitTime1.setText(str(limit_time1))
            # myDiag.ui.setMsg("请输出0-100间的数字！")

        # 处理time2
        if re.match(pattern_float, self.line_limitTime2.text()):
            if float(self.line_limitTime2.text()) < 1.00:
                self.line_limitTime2.setText("1")
                limit_time2 = 1.00
            if float(self.line_limitTime2.text()) > 100.00:
                self.line_limitTime2.setText("100")
                limit_time2 = 100.00
            self.line_limitTime2.setText(str(self.line_limitTime2.text().replace("+", "")))
            limit_time2 = float(self.line_limitTime2.text().replace("+", ""))
        else:
            self.line_limitTime2.setText(str(limit_time2))
            # myDiag.ui.setMsg("请输出0-100间的数字！")

        # 处理区间
        if float(self.line_limitTime1.text()) >= float(self.line_limitTime2.text()):
            self.line_limitTime1.setText(str(float(self.line_limitTime1.text()) - 1))
            limit_time1 = float(self.line_limitTime1.text()) - 1
        if float(self.line_limitTime1.text()) < 0:
            self.line_limitTime1.setText(str(float(self.line_limitTime1.text()) + 1))
            self.line_limitTime2.setText(str(float(self.line_limitTime2.text()) + 1))
            limit_time1 = float(self.line_limitTime1.text()) + 1
            limit_time1 = float(self.line_limitTime1.text()) + 1
        #print("global:" + str(limit_time1) + "/" + str(limit_time2))
        #self.table_refresh(1)
        temp_1 = self.line_frame_random_num.text()
        temp_2 = self.line_frame_num.text()
        if temp_1.isdigit():
            perVideo_frames = int(temp_1)
        else:
            perVideo_frames = 1
        if temp_2.isdigit():
            get_image_frame = int(temp_2)
        else:
            get_image_frame = 1

        self.dataFile_write()
        self.tableSignal.emit(1)
        self.setButton_enabled(1)

    def getRandom(self, num1, num2):
        rand_num = random.randint(num1, num2)
        return rand_num

    def getPathFiles(self,path):
        global path_files
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                #print("文件夹：", file_path)
                self.getPathFiles(file_path)
            else:
                #print("文件：", file_path)
                path_files.append(file_path)

    def dragEnterEvent(self, evn):
        if evn.mimeData().hasUrls():
            evn.accept()
        else:
            evn.ignore()
        #print('鼠标拖入窗口')
        # self.QLabl.setText('文件路径：\n' + evn.mimeData().text())
        # 鼠标放开函数事件
        #evn.accept()

    def dropEvent(self, evn):
        temp_url = evn.mimeData().urls()
        self.thread_it(self.addMultiFiles(temp_url))
        #print(path_files)

        #print(f'鼠标放开 {evn.posF()}')
        #path = str(evn.mimeData().text())
        #path = path.replace("file:///","")
        #print('文件路径：\n' + path)

    def dragMoveEvent(self, evn):
        pass
        # print('鼠标移动')

    def addMultiFiles(self,urls):
        global path_files
        #print(urls)
        for url in urls:
            file_path = url.toLocalFile()
            if os.path.isfile(file_path):
                path_files.append(file_path)
            elif os.path.isdir(file_path):
                self.getPathFiles(file_path)
            else:
                pass
                #print(file_path+"不是文件或目录")
        #print(path_files)
        temp_files = []
        for i in range(len(path_files)):
            file_name = path_files[i].split(".")
            file_type = file_name[len(file_name)-1]
            if file_type == "mp4" or file_type == "mkv" or file_type == "mpg" or file_type == "mpeg" or file_type == "avi" or file_type == "rmvb" or file_type == "wmv" or file_type == "mov" or file_type == "flv" or file_type == "ts" or file_type == "webm" or file_type == "m4v" or file_type == "m2ts" or file_type == "asf" or file_type == "MP4" or file_type == "MKV" or file_type == "MPG" or file_type == "MPEG" or file_type == "AVI" or file_type == "RMVB" or file_type == "WMV" or file_type == "MOV" or file_type == "FLV" or file_type == "TS" or file_type == "WEBM" or file_type == "M4V" or file_type == "M2TS" or file_type == "ASF":
                temp_files.append(QDir.fromNativeSeparators(path_files[i]))
        path_files = []
        out_path = self.getOutPath()
        self.setNewList(out_path,temp_files)


class MainDiag(QtWidgets.QDialogButtonBox):
    def __init__(self):
        super(QtWidgets.QDialogButtonBox, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def setMsg(self, content):
        # print("setMSG" + content)
        myDiag.ui.label.setText(content)
        myDiag.show()


class MainLog(QtWidgets.QDialog, Ui_Dialog_Log):
    msgSignal = pyqtSignal(str)

    def __init__(self):
        super(MainLog, self).__init__()
        #self.ui = Ui_Dialog_Log()
        self.setupUi(self)
        self.toolButton.clicked.connect(self.save_text)
        self.toolButton_close.clicked.connect(self.closeLog)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)


    def sendMsg(self, content):
        # print("setMSG" + content)
        # 获取当前日期时间
        datetime = QtCore.QDateTime.currentDateTime()
        # 格式化日期时间
        time_now = datetime.toString('yyyy-MM-dd HH:mm:ss')
        #self.textBrowser_log.setText("["+time_now+"]:"+content+"\n")
        self.textBrowser_log.append("["+time_now+"]:"+content+"\n")
        myWin.textBrowser.setText("["+time_now+"]:"+content)


    def save_text(self):
        datetime = QtCore.QDateTime.currentDateTime()
        # 格式化日期时间
        time_now = datetime.toString('yyyyMMdd_HHmmss')
        save_path = myWin.getOutPath()
        save_path2 = save_path
        #save_path2 =os.path.dirname(save_path)+"/log"
        save_path = save_path+"/log_"+ time_now +".txt"
        #print(save_path)
        if save_path is not None:
            if myWin.mkdir(save_path2):
                with open(file=save_path, mode='a+', encoding='utf-8') as file:
                    file.write(self.textBrowser_log.toPlainText())
                    file.close()
                #print('已保存！')
                self.msgSignal.emit("记录文件 [ " + save_path + " ] 已保存")


    def closeLog(self):
        self.close()



if __name__ == '__main__':
    # 加载配置文件，初始化
    #file_config = dispose_ini("./config.ini")
    #config_data = file_config.get_sections
    #print("...........")
    #print(config_data)
    current_path = os.getcwd()
    # 解决控件显示不完全
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    myapp = QtWidgets.QApplication(sys.argv)
    myWin = MainWindow()
    myWin.statusSignal.connect(myWin.changeStatus)
    myWin.tableSignal.connect(myWin.table_refresh)
    myWin.show()
    # QtWidgets.QApplication.processEvents()
    myDiag = MainDiag()
    # myDiag.show()
    myLog = MainLog()
    myLog.msgSignal.connect(myLog.sendMsg)
    #myLog.show()
    sys.exit(myapp.exec_())
