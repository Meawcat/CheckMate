# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataset_dialogiPLOzJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_dataset_dialog(object):
    def setupUi(self, dataset_dialog):
        if not dataset_dialog.objectName():
            dataset_dialog.setObjectName(u"dataset_dialog")
        dataset_dialog.resize(517, 364)
        dataset_dialog.setStyleSheet(u"QDialog{\n"
"	background-color: #fff;\n"
"}\n"
"QPushButton {\n"
"	background-color: #313a46;\n"
"	color: #fff;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"	width: 120px;\n"
"	height: 60px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(86,101,115,0.5);\n"
"	color:  #fff;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(dataset_dialog)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.combobox_label = QLabel(dataset_dialog)
        self.combobox_label.setObjectName(u"combobox_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_label.sizePolicy().hasHeightForWidth())
        self.combobox_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.combobox_label.setFont(font)
        self.combobox_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.combobox_label, 0, Qt.AlignHCenter)

        self.comboBox = QComboBox(dataset_dialog)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setKerning(False)
        self.comboBox.setFont(font1)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.comboBox, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ratio_label = QLabel(dataset_dialog)
        self.ratio_label.setObjectName(u"ratio_label")
        font2 = QFont()
        font2.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font2.setPointSize(13)
        self.ratio_label.setFont(font2)
        self.ratio_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.ratio_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.train_label = QLabel(dataset_dialog)
        self.train_label.setObjectName(u"train_label")
        font3 = QFont()
        font3.setPointSize(13)
        self.train_label.setFont(font3)
        self.train_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.train_label)

        self.train_ratio = QLabel(dataset_dialog)
        self.train_ratio.setObjectName(u"train_ratio")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.train_ratio.setFont(font4)
        self.train_ratio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.train_ratio)

        self.train_slider = QSlider(dataset_dialog)
        self.train_slider.setObjectName(u"train_slider")
        self.train_slider.setMinimum(60)
        self.train_slider.setMaximum(80)
        self.train_slider.setSingleStep(5)
        self.train_slider.setPageStep(5)
        self.train_slider.setOrientation(Qt.Horizontal)
        self.train_slider.setTickPosition(QSlider.TicksBelow)
        self.train_slider.setTickInterval(5)

        self.verticalLayout_3.addWidget(self.train_slider)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.valid_label = QLabel(dataset_dialog)
        self.valid_label.setObjectName(u"valid_label")
        self.valid_label.setFont(font3)
        self.valid_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.valid_label)

        self.valid_ratio = QLabel(dataset_dialog)
        self.valid_ratio.setObjectName(u"valid_ratio")
        self.valid_ratio.setFont(font4)
        self.valid_ratio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.valid_ratio)

        self.valid_slider = QSlider(dataset_dialog)
        self.valid_slider.setObjectName(u"valid_slider")
        self.valid_slider.setMinimum(10)
        self.valid_slider.setMaximum(20)
        self.valid_slider.setSingleStep(5)
        self.valid_slider.setPageStep(5)
        self.valid_slider.setValue(20)
        self.valid_slider.setOrientation(Qt.Horizontal)
        self.valid_slider.setTickPosition(QSlider.TicksBelow)
        self.valid_slider.setTickInterval(5)

        self.verticalLayout_2.addWidget(self.valid_slider)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.test_label = QLabel(dataset_dialog)
        self.test_label.setObjectName(u"test_label")
        self.test_label.setFont(font3)
        self.test_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.test_label)

        self.test_ratio = QLabel(dataset_dialog)
        self.test_ratio.setObjectName(u"test_ratio")
        self.test_ratio.setFont(font4)
        self.test_ratio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.test_ratio)

        self.test_slider = QSlider(dataset_dialog)
        self.test_slider.setObjectName(u"test_slider")
        self.test_slider.setMinimum(10)
        self.test_slider.setMaximum(20)
        self.test_slider.setSingleStep(5)
        self.test_slider.setPageStep(5)
        self.test_slider.setValue(20)
        self.test_slider.setOrientation(Qt.Horizontal)
        self.test_slider.setTickPosition(QSlider.TicksBelow)
        self.test_slider.setTickInterval(5)

        self.verticalLayout_4.addWidget(self.test_slider)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.split_button = QPushButton(dataset_dialog)
        self.split_button.setObjectName(u"split_button")
        font5 = QFont()
        font5.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font5.setPointSize(12)
        self.split_button.setFont(font5)
        self.split_button.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.split_button, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.retranslateUi(dataset_dialog)

        QMetaObject.connectSlotsByName(dataset_dialog)
    # setupUi

    def retranslateUi(self, dataset_dialog):
        dataset_dialog.setWindowTitle(QCoreApplication.translate("dataset_dialog", u"Dialog", None))
        self.combobox_label.setText(QCoreApplication.translate("dataset_dialog", u"\ub370\uc774\ud130 \ubd84\ud560\uc744 \uc6d0\ud558\ub294 \ubb3c\ud488\uc744 \uc120\ud0dd\ud574 \uc8fc\uc138\uc694", None))
        self.ratio_label.setText(QCoreApplication.translate("dataset_dialog", u"\ub370\uc774\ud130 \ubd84\ud560 \ube44\uc728\uc744 \uc870\uc815\ud574 \uc8fc\uc138\uc694", None))
        self.train_label.setText(QCoreApplication.translate("dataset_dialog", u"\ud6c8\ub828: Train", None))
        self.train_ratio.setText(QCoreApplication.translate("dataset_dialog", u"60", None))
        self.valid_label.setText(QCoreApplication.translate("dataset_dialog", u"\uac80\uc99d: Valid", None))
        self.valid_ratio.setText(QCoreApplication.translate("dataset_dialog", u"20", None))
        self.test_label.setText(QCoreApplication.translate("dataset_dialog", u"\uc2dc\ud5d8: Test", None))
        self.test_ratio.setText(QCoreApplication.translate("dataset_dialog", u"20", None))
        self.split_button.setText(QCoreApplication.translate("dataset_dialog", u"\ubd84\ud560", None))
    # retranslateUi

