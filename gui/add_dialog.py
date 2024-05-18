# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_dialogfrkcVg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_add_dialog(object):
    def setupUi(self, add_dialog):
        if not add_dialog.objectName():
            add_dialog.setObjectName(u"add_dialog")
        add_dialog.resize(551, 379)
        add_dialog.setStyleSheet(u"QDialog{\n"
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
        self.item_label = QLabel(add_dialog)
        self.item_label.setObjectName(u"item_label")
        self.item_label.setGeometry(QRect(20, 10, 505, 60))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_label.sizePolicy().hasHeightForWidth())
        self.item_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.item_label.setFont(font)
        self.item_name = QTextEdit(add_dialog)
        self.item_name.setObjectName(u"item_name")
        self.item_name.setGeometry(QRect(130, 70, 300, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.item_name.sizePolicy().hasHeightForWidth())
        self.item_name.setSizePolicy(sizePolicy1)
        self.item_name.setMaximumSize(QSize(300, 30))
        self.item_name.setLineWidth(0)
        self.item_name.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea = QScrollArea(add_dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(11, 174, 531, 131))
        self.scrollArea.setStyleSheet(u"background-color: transparent;\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 526, 129))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(526, 166))
        self.selected = QLabel(self.scrollAreaWidgetContents)
        self.selected.setObjectName(u"selected")
        self.selected.setGeometry(QRect(10, 10, 511, 111))
        self.selected.setStyleSheet(u"")
        self.scrollArea.setWidget(self.selected)
        self.button_box = QPushButton(add_dialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setGeometry(QRect(210, 320, 120, 41))
        self.button_box.setMaximumSize(QSize(120, 16777215))
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(12)
        self.button_box.setFont(font1)
        self.button_box.setContextMenuPolicy(Qt.NoContextMenu)
        self.button_box.setLayoutDirection(Qt.LeftToRight)
        self.button_box.setStyleSheet(u"")
        self.file_label = QLabel(add_dialog)
        self.file_label.setObjectName(u"file_label")
        self.file_label.setGeometry(QRect(20, 120, 409, 30))
        sizePolicy.setHeightForWidth(self.file_label.sizePolicy().hasHeightForWidth())
        self.file_label.setSizePolicy(sizePolicy)
        self.file_label.setMaximumSize(QSize(16777215, 30))
        self.file_label.setFont(font)
        self.file_button = QPushButton(add_dialog)
        self.file_button.setObjectName(u"file_button")
        self.file_button.setGeometry(QRect(430, 116, 111, 41))
        font2 = QFont()
        font2.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font2.setPointSize(10)
        self.file_button.setFont(font2)
        self.file_button.setStyleSheet(u"")

        self.retranslateUi(add_dialog)

        QMetaObject.connectSlotsByName(add_dialog)
    # setupUi

    def retranslateUi(self, add_dialog):
        add_dialog.setWindowTitle(QCoreApplication.translate("add_dialog", u"Dialog", None))
        self.item_label.setText(QCoreApplication.translate("add_dialog", u"\ucd94\uac00\ud560 \ub370\uc774\ud130\uc758 \uc774\ub984\uc744 \uc601\ubb38\uc73c\ub85c \uc791\uc131\ud574 \uc8fc\uc138\uc694", None))
        self.item_name.setHtml(QCoreApplication.translate("add_dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\ub9d1\uc740 \uace0\ub515';\"><br /></p></body></html>", None))
        self.selected.setText("")
        self.button_box.setText(QCoreApplication.translate("add_dialog", u"\ud655\uc778", None))
        self.file_label.setText(QCoreApplication.translate("add_dialog", u"\ucd94\uac00\ud560 \ub370\uc774\ud130 \ud30c\uc77c\ub4e4\uc744 \uc120\ud0dd\ud574 \uc8fc\uc138\uc694", None))
        self.file_button.setText(QCoreApplication.translate("add_dialog", u"\ud30c\uc77c \ucc3e\uae30", None))
    # retranslateUi

