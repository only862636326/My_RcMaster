# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Qtui/Qtui_frame_packInfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_FramInfo(object):
    def setupUi(self, Frame_FramInfo):
        Frame_FramInfo.setObjectName("Frame_FramInfo")
        Frame_FramInfo.resize(246, 328)
        self.comboBox = QtWidgets.QComboBox(Frame_FramInfo)
        self.comboBox.setGeometry(QtCore.QRect(9, 20, 221, 23))
        self.comboBox.setMinimumSize(QtCore.QSize(97, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.pushButton_save = QtWidgets.QPushButton(Frame_FramInfo)
        self.pushButton_save.setGeometry(QtCore.QRect(0, 250, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_set_pack = QtWidgets.QPushButton(Frame_FramInfo)
        self.pushButton_set_pack.setGeometry(QtCore.QRect(9, 280, 76, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_set_pack.setFont(font)
        self.pushButton_set_pack.setObjectName("pushButton_set_pack")
        self.pushButton_set_unpack = QtWidgets.QPushButton(Frame_FramInfo)
        self.pushButton_set_unpack.setGeometry(QtCore.QRect(127, 280, 76, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_set_unpack.setFont(font)
        self.pushButton_set_unpack.setObjectName("pushButton_set_unpack")
        self.widget = QtWidgets.QWidget(Frame_FramInfo)
        self.widget.setGeometry(QtCore.QRect(9, 60, 230, 161))
        self.widget.setMaximumSize(QtCore.QSize(262, 161))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 2)
        self.lineEdit_head2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_head2.setFont(font)
        self.lineEdit_head2.setText("")
        self.lineEdit_head2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_head2.setObjectName("lineEdit_head2")
        self.gridLayout.addWidget(self.lineEdit_head2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.lineEdit_end2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_end2.setFont(font)
        self.lineEdit_end2.setText("")
        self.lineEdit_end2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_end2.setObjectName("lineEdit_end2")
        self.gridLayout.addWidget(self.lineEdit_end2, 3, 2, 1, 1)
        self.lineEdit_pack_info = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_pack_info.setFont(font)
        self.lineEdit_pack_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pack_info.setObjectName("lineEdit_pack_info")
        self.gridLayout.addWidget(self.lineEdit_pack_info, 2, 1, 1, 2)
        self.lineEdit_end1 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_end1.setFont(font)
        self.lineEdit_end1.setText("")
        self.lineEdit_end1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_end1.setObjectName("lineEdit_end1")
        self.gridLayout.addWidget(self.lineEdit_end1, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_head1 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_head1.setFont(font)
        self.lineEdit_head1.setText("")
        self.lineEdit_head1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_head1.setObjectName("lineEdit_head1")
        self.gridLayout.addWidget(self.lineEdit_head1, 1, 1, 1, 1)

        self.retranslateUi(Frame_FramInfo)
        QtCore.QMetaObject.connectSlotsByName(Frame_FramInfo)
        Frame_FramInfo.setTabOrder(self.comboBox, self.lineEdit_name)
        Frame_FramInfo.setTabOrder(self.lineEdit_name, self.lineEdit_head1)
        Frame_FramInfo.setTabOrder(self.lineEdit_head1, self.lineEdit_head2)
        Frame_FramInfo.setTabOrder(self.lineEdit_head2, self.lineEdit_pack_info)
        Frame_FramInfo.setTabOrder(self.lineEdit_pack_info, self.lineEdit_end1)
        Frame_FramInfo.setTabOrder(self.lineEdit_end1, self.lineEdit_end2)
        Frame_FramInfo.setTabOrder(self.lineEdit_end2, self.pushButton_save)
        Frame_FramInfo.setTabOrder(self.pushButton_save, self.pushButton_set_pack)
        Frame_FramInfo.setTabOrder(self.pushButton_set_pack, self.pushButton_set_unpack)

    def retranslateUi(self, Frame_FramInfo):
        _translate = QtCore.QCoreApplication.translate
        Frame_FramInfo.setWindowTitle(_translate("Frame_FramInfo", "Frame"))
        self.pushButton_save.setText(_translate("Frame_FramInfo", "保存包信息"))
        self.pushButton_set_pack.setText(_translate("Frame_FramInfo", "设置打包"))
        self.pushButton_set_unpack.setText(_translate("Frame_FramInfo", "设置解包"))
        self.lineEdit_name.setText(_translate("Frame_FramInfo", "一二三四五六七八九十一二三"))
        self.label_3.setText(_translate("Frame_FramInfo", "帧尾"))
        self.label_2.setText(_translate("Frame_FramInfo", "帧头"))
        self.label.setText(_translate("Frame_FramInfo", "数据包\n"
"信息"))
        self.lineEdit_pack_info.setText(_translate("Frame_FramInfo", "HHHHHHHbb"))
        self.label_4.setText(_translate("Frame_FramInfo", "名称"))
