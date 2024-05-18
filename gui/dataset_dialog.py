# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataset_dialogbrhtnK.ui'
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
        dataset_dialog.resize(550, 379)
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
        self.comboBox = QComboBox(dataset_dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 60, 141, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.combobox_label = QLabel(dataset_dialog)
        self.combobox_label.setObjectName(u"combobox_label")
        self.combobox_label.setGeometry(QRect(20, 10, 511, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combobox_label.sizePolicy().hasHeightForWidth())
        self.combobox_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setWeight(50)
        self.combobox_label.setFont(font1)
        self.combobox_label.setAlignment(Qt.AlignCenter)
        self.split_button = QPushButton(dataset_dialog)
        self.split_button.setObjectName(u"split_button")
        self.split_button.setGeometry(QRect(210, 320, 121, 41))
        font2 = QFont()
        font2.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font2.setPointSize(12)
        self.split_button.setFont(font2)
        self.split_button.setStyleSheet(u"")
        self.ratio_label = QLabel(dataset_dialog)
        self.ratio_label.setObjectName(u"ratio_label")
        self.ratio_label.setGeometry(QRect(100, 120, 340, 30))
        font3 = QFont()
        font3.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font3.setPointSize(13)
        self.ratio_label.setFont(font3)
        self.ratio_label.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(dataset_dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 170, 501, 121))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.train_label = QLabel(self.layoutWidget)
        self.train_label.setObjectName(u"train_label")
        font4 = QFont()
        font4.setPointSize(13)
        self.train_label.setFont(font4)
        self.train_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.train_label)

        self.train_ratio = QLabel(self.layoutWidget)
        self.train_ratio.setObjectName(u"train_ratio")
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setWeight(75)
        self.train_ratio.setFont(font5)
        self.train_ratio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.train_ratio)

        self.train_slider = QSlider(self.layoutWidget)
        self.train_slider.setObjectName(u"train_slider")
        self.train_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.train_slider)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.valid_label = QLabel(self.layoutWidget)
        self.valid_label.setObjectName(u"valid_label")
        self.valid_label.setFont(font4)
        self.valid_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.valid_label)

        self.valid_ratio = QLabel(self.layoutWidget)
        self.valid_ratio.setObjectName(u"valid_ratio")
        self.valid_ratio.setFont(font5)
        self.valid_ratio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.valid_ratio)

        self.valid_slider = QSlider(self.layoutWidget)
        self.valid_slider.setObjectName(u"valid_slider")
        self.valid_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.valid_slider)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.test_label = QLabel(self.layoutWidget)
        self.test_label.setObjectName(u"test_label")
        self.test_label.setFont(font4)
        self.test_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.test_label)

        self.test_ratio = QLabel(self.layoutWidget)
        self.test_ratio.setObjectName(u"test_ratio")
        self.test_ratio.setFont(font5)
        self.test_ratio.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.test_ratio)

        self.test_slider = QSlider(self.layoutWidget)
        self.test_slider.setObjectName(u"test_slider")
        self.test_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.test_slider)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(dataset_dialog)

        QMetaObject.connectSlotsByName(dataset_dialog)
    # setupUi

    def retranslateUi(self, dataset_dialog):
        dataset_dialog.setWindowTitle(QCoreApplication.translate("dataset_dialog", u"Dialog", None))
        self.combobox_label.setText(QCoreApplication.translate("dataset_dialog", u"\ub370\uc774\ud130 \ubd84\ud560\uc744 \uc6d0\ud558\ub294 \ubb3c\ud488\uc744 \uc120\ud0dd\ud574 \uc8fc\uc138\uc694", None))
        self.split_button.setText(QCoreApplication.translate("dataset_dialog", u"\ubd84\ud560", None))
        self.ratio_label.setText(QCoreApplication.translate("dataset_dialog", u"\ub370\uc774\ud130 \ubd84\ud560 \ube44\uc728\uc744 \uc870\uc815\ud574 \uc8fc\uc138\uc694", None))
        self.train_label.setText(QCoreApplication.translate("dataset_dialog", u"\ud6c8\ub828: Train", None))
        self.train_ratio.setText(QCoreApplication.translate("dataset_dialog", u"60", None))
        self.valid_label.setText(QCoreApplication.translate("dataset_dialog", u"\uac80\uc99d: Valid", None))
        self.valid_ratio.setText(QCoreApplication.translate("dataset_dialog", u"20", None))
        self.test_label.setText(QCoreApplication.translate("dataset_dialog", u"\uc2dc\ud5d8: Test", None))
        self.test_ratio.setText(QCoreApplication.translate("dataset_dialog", u"20", None))
    # retranslateUi

