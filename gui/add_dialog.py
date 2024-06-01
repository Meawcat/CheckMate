# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/add_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_dialog(object):
    def setupUi(self, add_dialog):
        add_dialog.setObjectName("add_dialog")
        add_dialog.resize(537, 448)
        add_dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        add_dialog.setStyleSheet("QDialog{\n"
"    background-color: #fff;\n"
"}\n"
"QPushButton {\n"
"    background-color: #DBE2EF;\n"
"    color: #112D4E;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    width: 120px;\n"
"    height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #fff;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(add_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verlay2 = QtWidgets.QVBoxLayout()
        self.verlay2.setObjectName("verlay2")
        self.verlay1 = QtWidgets.QVBoxLayout()
        self.verlay1.setObjectName("verlay1")
        self.item_label = QtWidgets.QLabel(add_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_label.sizePolicy().hasHeightForWidth())
        self.item_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.item_label.setFont(font)
        self.item_label.setObjectName("item_label")
        self.verlay1.addWidget(self.item_label, 0, QtCore.Qt.AlignHCenter)
        self.item_name = QtWidgets.QTextEdit(add_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_name.sizePolicy().hasHeightForWidth())
        self.item_name.setSizePolicy(sizePolicy)
        self.item_name.setMaximumSize(QtCore.QSize(300, 30))
        self.item_name.setLineWidth(0)
        self.item_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.item_name.setObjectName("item_name")
        font.setPointSize(9)
        self.item_name.setFont(font)
        self.verlay1.addWidget(self.item_name, 0, QtCore.Qt.AlignHCenter)
        self.verlay2.addLayout(self.verlay1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.file_label = QtWidgets.QLabel(add_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_label.sizePolicy().hasHeightForWidth())
        self.file_label.setSizePolicy(sizePolicy)
        self.file_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.file_label.setFont(font)
        self.file_label.setObjectName("file_label")
        self.gridLayout.addWidget(self.file_label, 0, 0, 1, 1)
        self.file_button = QtWidgets.QPushButton(add_dialog)
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(10)
        self.file_button.setFont(font)
        self.file_button.setStyleSheet("")
        self.file_button.setObjectName("file_button")
        self.gridLayout.addWidget(self.file_button, 0, 1, 1, 1)
        self.verlay2.addLayout(self.gridLayout)
        self.scrollArea = QtWidgets.QScrollArea(add_dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("border: none; background-color: #F9F7F7;")
        self.scrollArea.verticalScrollBar().setStyleSheet(
                "QScrollBar:vertical { border: none; background-color: #3F72AF; }"
        )
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 511, 210))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.selected = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.selected.setText("")
        self.selected.setObjectName("selected")
        self.selected.setFont(font)
        self.gridLayout_3.addWidget(self.selected, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verlay2.addWidget(self.scrollArea)
        self.add_button = QtWidgets.QPushButton(add_dialog)
        self.add_button.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(12)
        self.add_button.setFont(font)
        self.add_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.add_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_button.setStyleSheet("")
        self.add_button.setObjectName("add_button")
        self.verlay2.addWidget(self.add_button, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.verlay2, 0, 0, 1, 1)

        self.retranslateUi(add_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_dialog)

    def retranslateUi(self, add_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_dialog.setWindowTitle(_translate("add_dialog", "Dialog"))
        self.item_label.setText(_translate("add_dialog", "추가할 데이터의 이름을 영문으로 작성해 주세요"))
        self.item_name.setHtml(_translate("add_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Noto Sans KR\';\"><br /></p></body></html>"))
        self.file_label.setText(_translate("add_dialog", "추가할 데이터 파일들을 선택해 주세요"))
        self.file_button.setText(_translate("add_dialog", "파일 찾기"))
        self.add_button.setText(_translate("add_dialog", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_dialog = QtWidgets.QDialog()
    ui = Ui_add_dialog()
    ui.setupUi(add_dialog)
    add_dialog.show()
    sys.exit(app.exec_())
