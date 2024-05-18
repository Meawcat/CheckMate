# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'label_dialogIWJfjC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_label_dialog(object):
    def setupUi(self, label_dialog):
        if not label_dialog.objectName():
            label_dialog.setObjectName(u"label_dialog")
        label_dialog.resize(552, 380)
        label_dialog.setStyleSheet(u"QDialog{\n"
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
        self.label_label = QLabel(label_dialog)
        self.label_label.setObjectName(u"label_label")
        self.label_label.setGeometry(QRect(20, 80, 511, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_label.sizePolicy().hasHeightForWidth())
        self.label_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_label.setFont(font)
        self.label_label.setAlignment(Qt.AlignCenter)
        self.item_combo = QComboBox(label_dialog)
        self.item_combo.setObjectName(u"item_combo")
        self.item_combo.setGeometry(QRect(200, 170, 141, 32))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.item_combo.sizePolicy().hasHeightForWidth())
        self.item_combo.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setKerning(False)
        self.item_combo.setFont(font1)
        self.item_combo.setLayoutDirection(Qt.LeftToRight)
        self.label_button = QPushButton(label_dialog)
        self.label_button.setObjectName(u"label_button")
        self.label_button.setGeometry(QRect(210, 310, 120, 41))
        self.label_button.setMaximumSize(QSize(120, 16777215))
        font2 = QFont()
        font2.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font2.setPointSize(12)
        self.label_button.setFont(font2)
        self.label_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_button.setLayoutDirection(Qt.LeftToRight)
        self.label_button.setStyleSheet(u"")

        self.retranslateUi(label_dialog)

        QMetaObject.connectSlotsByName(label_dialog)
    # setupUi

    def retranslateUi(self, label_dialog):
        label_dialog.setWindowTitle(QCoreApplication.translate("label_dialog", u"Dialog", None))
        self.label_label.setText(QCoreApplication.translate("label_dialog", u"\ub77c\ubca8\ub9c1\ud560 \ub370\uc774\ud130 \ubb3c\ud488\uc744 \uc120\ud0dd\ud574 \uc8fc\uc138\uc694", None))
        self.label_button.setText(QCoreApplication.translate("label_dialog", u"\ud655\uc778", None))
    # retranslateUi

