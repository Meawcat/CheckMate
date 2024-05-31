# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/dataset_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dataset_dialog(object):
    def setupUi(self, dataset_dialog):
        dataset_dialog.setObjectName("dataset_dialog")
        dataset_dialog.resize(517, 364)
        dataset_dialog.setStyleSheet("QDialog{\n"
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
"    color:  #fff;\n"
"}")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(dataset_dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.combobox_label = QtWidgets.QLabel(dataset_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_label.sizePolicy().hasHeightForWidth())
        self.combobox_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.combobox_label.setFont(font)
        self.combobox_label.setAlignment(QtCore.Qt.AlignCenter)
        self.combobox_label.setObjectName("combobox_label")
        self.verticalLayout.addWidget(self.combobox_label, 0, QtCore.Qt.AlignHCenter)
        self.comboBox = QtWidgets.QComboBox(dataset_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.ratio_label = QtWidgets.QLabel(dataset_dialog)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.ratio_label.setFont(font)
        self.ratio_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ratio_label.setObjectName("ratio_label")
        self.verticalLayout_6.addWidget(self.ratio_label)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.train_label = QtWidgets.QLabel(dataset_dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.train_label.setFont(font)
        self.train_label.setAlignment(QtCore.Qt.AlignCenter)
        self.train_label.setObjectName("train_label")
        self.verticalLayout_2.addWidget(self.train_label)
        self.train_ratio = QtWidgets.QLabel(dataset_dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.train_ratio.setFont(font)
        self.train_ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.train_ratio.setObjectName("train_ratio")
        self.verticalLayout_2.addWidget(self.train_ratio)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.valid_label = QtWidgets.QLabel(dataset_dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.valid_label.setFont(font)
        self.valid_label.setAlignment(QtCore.Qt.AlignCenter)
        self.valid_label.setObjectName("valid_label")
        self.verticalLayout_3.addWidget(self.valid_label)
        self.valid_ratio = QtWidgets.QLabel(dataset_dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.valid_ratio.setFont(font)
        self.valid_ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.valid_ratio.setObjectName("valid_ratio")
        self.verticalLayout_3.addWidget(self.valid_ratio)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.test_label = QtWidgets.QLabel(dataset_dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.test_label.setFont(font)
        self.test_label.setAlignment(QtCore.Qt.AlignCenter)
        self.test_label.setObjectName("test_label")
        self.verticalLayout_4.addWidget(self.test_label)
        self.test_ratio = QtWidgets.QLabel(dataset_dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.test_ratio.setFont(font)
        self.test_ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.test_ratio.setObjectName("test_ratio")
        self.verticalLayout_4.addWidget(self.test_ratio)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.train_slider = QtWidgets.QSlider(dataset_dialog)
        self.train_slider.setMinimum(60)
        self.train_slider.setMaximum(80)
        self.train_slider.setSingleStep(5)
        self.train_slider.setPageStep(5)
        self.train_slider.setOrientation(QtCore.Qt.Horizontal)
        self.train_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.train_slider.setTickInterval(5)
        self.train_slider.setObjectName("train_slider")
        self.verticalLayout_5.addWidget(self.train_slider)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.split_button = QtWidgets.QPushButton(dataset_dialog)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.split_button.setFont(font)
        self.split_button.setStyleSheet("")
        self.split_button.setObjectName("split_button")
        self.verticalLayout_6.addWidget(self.split_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(dataset_dialog)
        QtCore.QMetaObject.connectSlotsByName(dataset_dialog)

    def retranslateUi(self, dataset_dialog):
        _translate = QtCore.QCoreApplication.translate
        dataset_dialog.setWindowTitle(_translate("dataset_dialog", "Dialog"))
        self.combobox_label.setText(_translate("dataset_dialog", "데이터 분할을 원하는 물품을 선택해 주세요"))
        self.ratio_label.setText(_translate("dataset_dialog", "데이터 분할 비율을 조정해 주세요"))
        self.train_label.setText(_translate("dataset_dialog", "훈련: Train"))
        self.train_ratio.setText(_translate("dataset_dialog", "60"))
        self.valid_label.setText(_translate("dataset_dialog", "검증: Valid"))
        self.valid_ratio.setText(_translate("dataset_dialog", "20"))
        self.test_label.setText(_translate("dataset_dialog", "시험: Test"))
        self.test_ratio.setText(_translate("dataset_dialog", "20"))
        self.split_button.setText(_translate("dataset_dialog", "분할"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dataset_dialog = QtWidgets.QDialog()
    ui = Ui_dataset_dialog()
    ui.setupUi(dataset_dialog)
    dataset_dialog.show()
    sys.exit(app.exec_())
