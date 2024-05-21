# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yolo_learn_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os, subprocess
import threading
from PyQt5.QtWidgets import QMessageBox


class Ui_YoloLearnWindow(object):
    def setupUi(self, YoloLearnWindow):
        YoloLearnWindow.setObjectName("YoloLearnWindow")
        YoloLearnWindow.resize(625, 443)
        YoloLearnWindow.setStyleSheet("#YoloLearnWindow{\n"
"    font: 9pt \"맑은 고딕\";\n"
"    background-color: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(YoloLearnWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.find_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.find_button.setFont(font)
        self.find_button.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#a6aaaf;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #a6aaaf;\n"
"}")
        self.find_button.setObjectName("find_button")
        self.gridLayout.addWidget(self.find_button, 1, 2, 1, 1)
        self.model_dir_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_dir_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.model_dir_edit.setObjectName("model_dir_edit")
        self.gridLayout.addWidget(self.model_dir_edit, 2, 1, 1, 1)
        self.yaml_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.yaml_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.yaml_edit.setObjectName("yaml_edit")
        self.gridLayout.addWidget(self.yaml_edit, 1, 1, 1, 1)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.load_button.setFont(font)
        self.load_button.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#a6aaaf;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #a6aaaf;\n"
"}")
        self.load_button.setObjectName("load_button")
        self.gridLayout.addWidget(self.load_button, 3, 2, 1, 1)
        self.model_dir = QtWidgets.QLabel(self.centralwidget)
        self.model_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.model_dir.setObjectName("model_dir")
        self.gridLayout.addWidget(self.model_dir, 2, 0, 1, 1)
        self.model_save = QtWidgets.QLabel(self.centralwidget)
        self.model_save.setAlignment(QtCore.Qt.AlignCenter)
        self.model_save.setObjectName("model_save")
        self.gridLayout.addWidget(self.model_save, 3, 0, 1, 1)
        self.yaml_dir = QtWidgets.QLabel(self.centralwidget)
        self.yaml_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.yaml_dir.setObjectName("yaml_dir")
        self.gridLayout.addWidget(self.yaml_dir, 1, 0, 1, 1)
        self.model_save_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_save_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.model_save_edit.setObjectName("model_save_edit")
        self.gridLayout.addWidget(self.model_save_edit, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox.setStyleSheet("border: 2px solid #a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.item_name = QtWidgets.QLabel(self.centralwidget)
        self.item_name.setObjectName("item_name")
        self.gridLayout.addWidget(self.item_name, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.train_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.train_button.setFont(font)
        self.train_button.setStyleSheet("QPushButton:hover {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    border: 4px solid#a6aaaf;\n"
"    border-radius: 5px;\n"
"    padding: 1px 5px;\n"
"    background-color: #a6aaaf;\n"
"}")
        self.train_button.setObjectName("train_button")
        self.gridLayout_2.addWidget(self.train_button, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        YoloLearnWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(YoloLearnWindow)
        QtCore.QMetaObject.connectSlotsByName(YoloLearnWindow)


        self.populate_directory_combo(self.comboBox)
        self.set_edit()
        self.find_button.clicked.connect(self.open_file_dialog)
        self.load_button.clicked.connect(self.open_directory_dialog)
        self.comboBox.currentIndexChanged.connect(self.set_edit)
        self.train_button.clicked.connect(self.start_training)
        self.model_dir_edit.textChanged.connect(self.model_dir_changed)

    def retranslateUi(self, YoloLearnWindow):
        _translate = QtCore.QCoreApplication.translate
        YoloLearnWindow.setWindowTitle(_translate("YoloLearnWindow", "MainWindow"))
        self.find_button.setText(_translate("YoloLearnWindow", "찾아보기"))
        self.load_button.setText(_translate("YoloLearnWindow", "불러오기"))
        self.model_dir.setText(_translate("YoloLearnWindow", "학습 모델 폴더 이름"))
        self.model_save.setText(_translate("YoloLearnWindow", "학습 모델 저장 위치"))
        self.yaml_dir.setText(_translate("YoloLearnWindow", "../data.yaml 파일 위치"))
        self.item_name.setText(_translate("YoloLearnWindow", "물품 이름"))
        self.train_button.setText(_translate("YoloLearnWindow", "학습 시작"))

    def model_dir_changed(self):
        combo_text = self.comboBox.currentText()
        model_dir_text = self.model_dir_edit.text()
        new_path = os.path.join("../yolov5/runs/train", model_dir_text, "weights")
        self.model_save_edit.setText(new_path)
        
    def start_training(self):
        data_yaml = self.yaml_edit.text()
        model_name = self.model_dir_edit.text()
        save_dir = self.model_save_edit.text()
        if not data_yaml or not model_name or not save_dir:
            QMessageBox.warning(None, "경고", "모든 필드를 입력해 주세요")
            return
        epochs = 1
        command = f'python train.py --img 640 --batch 16 --epochs {epochs} --data {data_yaml} --cfg models/yolov5s.yaml --weights yolov5s.pt --name {model_name} --project {save_dir}'

        # 학습 중에 출력을 실시간으로 읽어오고, 진행 상황에 따라 프로그레스 바를 업데이트하는 코드
        def update_progress():
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            while process.poll() is None:
                line = process.stdout.readline()
                # "progress: XX%" 형식의 문자열에서 진행률 정보 추출.. 수정해야 할 듯
                if "progress:" in line:
                    progress = int(line.split("progress: ")[1].split("%")[0])
                    # 프로그레스 바 업데이트
                    self.update_progress_bar(progress)

        threading.Thread(target=update_progress).start()

    def update_progress_bar(self, progress):
        self.progressBar.setValue(progress)


    def set_edit(self):
        selected_item = self.comboBox.currentText()
        selected_dir = os.path.join("../data", selected_item)
        selected_yaml = os.path.join(selected_dir, "../data.yaml")
        selected_model_dir = os.path.join("../yolov5/runs/train")

        if not os.path.exists(selected_yaml):
            self.yaml_edit.setText("해당 파일이 존재하지 않습니다. 다시 확인해 주세요")
        else:
            self.yaml_edit.setText(selected_yaml)

        model_name = selected_item
        self.model_dir_edit.setText(model_name)

        selected_model_save_dir = os.path.join(selected_model_dir, self.model_dir_edit.text(), "weights")
        self.model_save_edit.setText(selected_model_save_dir)


    def populate_directory_combo(self, combo):
        # './../data' 디렉터리에서 디렉터리 명들을 읽어와 콤보박스에 추가합니다.
        directory = "../data"
        directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
        combo.addItems(directories)

    # 파일 열기 함수
    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select ../data.yaml file", "", "YAML Files (*.yaml);;All Files (*)", options=options)
        if file_path:
                self.yaml_edit.setText(file_path)

    # 디렉토리 열기 함수
    def open_directory_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        directory_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory", "", options=options)
        if directory_path:
            self.model_save_edit.setText(directory_path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YoloLearnWindow = QtWidgets.QMainWindow()
    ui = Ui_YoloLearnWindow()
    ui.setupUi(YoloLearnWindow)
    YoloLearnWindow.show()
    sys.exit(app.exec_())
