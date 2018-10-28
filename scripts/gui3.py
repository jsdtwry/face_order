#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import cv2
 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import os


#faceCascade = cv2.CascadeClassifier(r'configs/haarcascade_frontalface_default.xml')
#faceCascade = cv2.CascadeClassifier(r'D:\\work\project\face_detection\scripts\configs\haarcascade_frontalface_default.xml')

path = os.getcwd()
#print(r'D:\\work\project\face_detection\scripts\configs\haarcascade_frontalface_default.xml')
#print(path+'\configs\haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(path+'\configs\haarcascade_frontalface_default.xml')

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
 
        # self.face_recong = face.Recognition()
        self.camnum = 0
        self.timer_camera = QtCore.QTimer()
        self.CAM_NUM = 0
        self.set_ui()
        self.slot_init()
        self.__flag_work = 0
        self.x =0
        self.count = 0
        self.person_count = 0

    def onActivated(self, text):
        #self.label_count.setText(text)
        if text=='Cam 0':
            self.camnum = 0
        if text=='Cam 1':
            self.camnum = 1



    def center(self):     
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def set_ui(self):
 
        self.__layout_main = QtWidgets.QHBoxLayout()
        self.__layout_fun_button = QtWidgets.QVBoxLayout()
        self.__layout_data_show = QtWidgets.QVBoxLayout()

        self.combo = QComboBox(self)
        self.combo.addItem('Cam 0')
        self.combo.addItem('Cam 1')
        self.combo.move(20,420)
        self.combo.activated[str].connect(self.onActivated)

        self.button_open_camera = QtWidgets.QPushButton(u'打开相机')
 
        self.button_order = QtWidgets.QPushButton(u'开始点名')
 
 
        #Button 的颜色修改
        button_color = [self.button_open_camera, self.button_order]
        for i in range(2):
            button_color[i].setStyleSheet("QPushButton{color:black}"
                                          "QPushButton:hover{color:red}"
                                          "QPushButton{background-color:rgb(255,255,255)}"
                                          "QPushButton{border:2px}"
                                          "QPushButton{border-radius:10px}"
                                          "QPushButton{padding:2px 4px}")
 
 
        self.button_open_camera.setMinimumHeight(30)
        self.button_order.setMinimumHeight(30)
 
        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        self.move(300, 300)
 
        # 信息显示
        self.label_show_camera = QtWidgets.QLabel()
        self.label_move = QtWidgets.QLabel()
        self.label_move.setFixedSize(100, 100)
 
        self.label_show_camera.setFixedSize(641, 481)
        self.label_show_camera.setAutoFillBackground(False)

        self.label_count = QtWidgets.QLabel('点名人数: ', self)
        self.label_count.move(20,20)
        self.label_count.setFixedSize(200,100)

        self.__layout_fun_button.addWidget(self.button_open_camera)
        self.__layout_fun_button.addWidget(self.button_order)
        self.__layout_fun_button.addWidget(self.label_move)
 
        self.__layout_main.addLayout(self.__layout_fun_button)
        self.__layout_main.addWidget(self.label_show_camera)
 
        self.setLayout(self.__layout_main)
        self.label_move.raise_()
        self.center()
        self.setWindowTitle(u'点名系统')
 
        '''
        # 设置背景图片
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
        self.setPalette(palette1)
        '''
        
 
    def slot_init(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_order.clicked.connect(self.order)


    def order(self):
        #print("person_count: ",self.person_count)
        if self.timer_camera.isActive() == False:
            self.label_count.setText('请先打开相机再开始点名')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.button_open_camera.setText(u'打开相机')
            self.label_count.setText('点名人数: '+str(self.person_count))
 
    def button_open_camera_click(self):
        self.cap = cv2.VideoCapture(self.camnum)
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok,
                                                defaultButton=QtWidgets.QMessageBox.Ok)
            # if msg==QtGui.QMessageBox.Cancel:
            #                     pass
            else:
                self.timer_camera.start(30)
 
                self.button_open_camera.setText(u'关闭相机')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText(u'打开相机')
 
 
    def show_camera(self):
        flag, self.image = self.cap.read()
        # face = self.face_detect.align(self.image)
        # if face:
        #     pass
        #show = cv2.resize(self.image, (640, 480))
        #gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        frame = self.image
        show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #'''
        faces = faceCascade.detectMultiScale(
            show,
            scaleFactor=1.15,
            minNeighbors=5,
            minSize=(5, 5),
            #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        self.person_count = len(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(show, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #'''
        # print(show.shape[1], show.shape[0])
        #show.shape[1] = 640, show.shape[0] = 480
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        # self.x += 1
        # self.label_move.move(self.x,100)
 
        # if self.x ==320:
        #     self.label_show_camera.raise_()
 
 
    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()
 
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")
 
        msg.addButton(ok,QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        # msg.setDetailedText('sdfsdff')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            #             self.socket_client.send_command(self.socket_client.current_user_command)
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()
 
 
 
if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(App.exec_())

