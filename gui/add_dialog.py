# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_dialogIXwZzr.ui'
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
        add_dialog.resize(550, 400)
        add_dialog.setMaximumSize(QSize(16777215, 16777215))
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
        self.horizontalLayout = QHBoxLayout(add_dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verlay2 = QVBoxLayout()
        self.verlay2.setObjectName(u"verlay2")
        self.verlay1 = QVBoxLayout()
        self.verlay1.setObjectName(u"verlay1")
        self.item_label = QLabel(add_dialog)
        self.item_label.setObjectName(u"item_label")
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

        self.verlay1.addWidget(self.item_label, 0, Qt.AlignHCenter)

        self.item_name = QTextEdit(add_dialog)
        self.item_name.setObjectName(u"item_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.item_name.sizePolicy().hasHeightForWidth())
        self.item_name.setSizePolicy(sizePolicy1)
        self.item_name.setMaximumSize(QSize(300, 30))
        self.item_name.setLineWidth(0)
        self.item_name.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verlay1.addWidget(self.item_name, 0, Qt.AlignHCenter)


        self.verlay2.addLayout(self.verlay1)

        self.horlay1 = QHBoxLayout()
        self.horlay1.setObjectName(u"horlay1")
        self.file_label = QLabel(add_dialog)
        self.file_label.setObjectName(u"file_label")
        sizePolicy.setHeightForWidth(self.file_label.sizePolicy().hasHeightForWidth())
        self.file_label.setSizePolicy(sizePolicy)
        self.file_label.setMaximumSize(QSize(16777215, 30))
        self.file_label.setFont(font)

        self.horlay1.addWidget(self.file_label)

        self.file_button = QPushButton(add_dialog)
        self.file_button.setObjectName(u"file_button")
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(10)
        self.file_button.setFont(font1)
        self.file_button.setStyleSheet(u"")

        self.horlay1.addWidget(self.file_button)


        self.verlay2.addLayout(self.horlay1)

        self.scrollArea = QScrollArea(add_dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: transparent;\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 524, 162))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(526, 166))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.selected = QLabel(self.scrollAreaWidgetContents)
        self.selected.setObjectName(u"selected")
        self.selected.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.selected)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verlay2.addWidget(self.scrollArea)

        self.add_button = QPushButton(add_dialog)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMaximumSize(QSize(120, 16777215))
        font2 = QFont()
        font2.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font2.setPointSize(12)
        self.add_button.setFont(font2)
        self.add_button.setContextMenuPolicy(Qt.NoContextMenu)
        self.add_button.setLayoutDirection(Qt.LeftToRight)
        self.add_button.setStyleSheet(u"")

        self.verlay2.addWidget(self.add_button, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verlay2)


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
        self.file_label.setText(QCoreApplication.translate("add_dialog", u"\ucd94\uac00\ud560 \ub370\uc774\ud130 \ud30c\uc77c\ub4e4\uc744 \uc120\ud0dd\ud574 \uc8fc\uc138\uc694", None))
        self.file_button.setText(QCoreApplication.translate("add_dialog", u"\ud30c\uc77c \ucc3e\uae30", None))
        self.selected.setText("")
        self.add_button.setText(QCoreApplication.translate("add_dialog", u"\ud655\uc778", None))
    # retranslateUi

