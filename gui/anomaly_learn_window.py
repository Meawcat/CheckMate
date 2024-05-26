# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/anomaly_learn_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import shutil
import subprocess
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class TrainingThread(QtCore.QThread):
    update_progress = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        try:
            process = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')
            output = ""
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                output += line
                self.update_progress.emit(output)
                QtCore.QCoreApplication.processEvents()
            process.stdout.close()
            process.wait()
            if process.returncode == 0:
                self.finished.emit("학습이 완료되었습니다.")
            else:
                self.finished.emit("학습 중 오류가 발생했습니다.")
        except Exception as e:
            self.finished.emit(f"알 수 없는 오류가 발생했습니다: {e}")

class Ui_AnomalyLearnWindow(object):
    def __init__(self):
        self.thread = None

    def setupUi(self, AnomalyLearnWindow):
        self.is_training = False  # 학습이 진행 중인지 여부를 추적하는 플래그
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        AnomalyLearnWindow.setObjectName("AnomalyLearnWindow")
        AnomalyLearnWindow.resize(625, 443)
        AnomalyLearnWindow.setStyleSheet("font: 9pt \"맑은 고딕\";\n"
                                         "background-color: #fff;\n"
                                         "")
        self.centralwidget = QtWidgets.QWidget(AnomalyLearnWindow)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("QPushButton:hover {\n"
                                         "    color: #fff;\n"
                                         "    font: bold;\n"
                                         "}\n"
                                         "QPushButton {\n"
                                         "    border: 4px solid#a6aaaf;\n"
                                         "    border-radius: 5px;\n"
                                         "    padding: 1px 5px;\n"
                                         "    background-color: #a6aaaf;\n"
                                         "    font: bold;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.model_save = QtWidgets.QLabel(self.centralwidget)
        self.model_save.setAlignment(QtCore.Qt.AlignCenter)
        self.model_save.setObjectName("model_save")
        self.gridLayout.addWidget(self.model_save, 2, 0, 1, 1)
        self.item_name = QtWidgets.QLabel(self.centralwidget)
        self.item_name.setObjectName("item_name")
        self.gridLayout.addWidget(self.item_name, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
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
        self.gridLayout.addWidget(self.load_button, 2, 2, 1, 1)
        self.model_save_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_save_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
                                           "border-radius: 5px;\n"
                                           "padding: 1px 5px;\n"
                                           "\n"
                                           "")
        self.model_save_edit.setObjectName("model_save_edit")
        self.gridLayout.addWidget(self.model_save_edit, 2, 1, 1, 1)
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
        self.model_dir = QtWidgets.QLabel(self.centralwidget)
        self.model_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.model_dir.setObjectName("model_dir")
        self.gridLayout.addWidget(self.model_dir, 1, 0, 1, 1)
        self.model_dir_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.model_dir_edit.setStyleSheet("border: 2px solid#a6aaaf;\n"
                                          "border-radius: 5px;\n"
                                          "padding: 1px 5px;\n"
                                          "\n"
                                          "")
        self.model_dir_edit.setObjectName("model_dir_edit")
        self.gridLayout.addWidget(self.model_dir_edit, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.train_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 601, 257))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.process = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.process.setText("")
        self.process.setObjectName("process")
        self.verticalLayout.addWidget(self.process)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        AnomalyLearnWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AnomalyLearnWindow)
        QtCore.QMetaObject.connectSlotsByName(AnomalyLearnWindow)

        self.populate_directory_combo(self.comboBox)
        self.set_edit()
        self.load_button.clicked.connect(self.open_directory_dialog)
        self.comboBox.currentIndexChanged.connect(self.set_edit)
        self.train_button.clicked.connect(self.start_training)
        self.model_dir_edit.textChanged.connect(self.model_dir_changed)
        AnomalyLearnWindow.closeEvent = self.closeEvent
    def retranslateUi(self, AnomalyLearnWindow):
        _translate = QtCore.QCoreApplication.translate
        AnomalyLearnWindow.setWindowTitle(_translate("AnomalyLearnWindow", "EfficientAD 학습"))
        self.model_save.setText(_translate("AnomalyLearnWindow", "학습 모델 저장 위치"))
        self.item_name.setText(_translate("AnomalyLearnWindow", "물품 이름"))
        self.load_button.setText(_translate("AnomalyLearnWindow", "불러오기"))
        self.model_dir.setText(_translate("AnomalyLearnWindow", "학습 모델 폴더 이름"))
        self.train_button.setText(_translate("AnomalyLearnWindow", "학습 시작"))

    def closeEvent(self, event):
        if self.is_training:
            # 학습이 진행 중일 때 경고 메시지 박스를 띄움
            reply = QMessageBox.question(None, '경고', '학습이 진행 중입니다. 종료하시겠습니까?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()  # 이벤트를 수락하여 창을 닫음
            else:
                event.ignore()  # 이벤트를 무시하여 창을 닫지 않음
        else:
            event.accept()  # 이벤트를 수락하여 창을 닫음

    def model_dir_changed(self):
            combo_text = self.comboBox.currentText()
            model_dir_text = self.model_dir_edit.text()
            new_path = os.path.join("../EfficientAD-main/output", model_dir_text)
            self.model_save_edit.setText(new_path)

    def start_training(self):
        self.train_button.setEnabled(False)  # 버튼 비활성화
        self.is_training = True  # 학습이 진행 중임을 나타내는 플래그 설정
        model_save = self.model_save_edit.text()
        model_dir = self.model_dir_edit.text()
        model_dir_name = model_dir
        i = 1
        if not model_save or not model_dir:
            QMessageBox.warning(None, "경고", "모든 필드를 입력해 주세요")
            self.train_button.setEnabled(True)  # 오류가 발생하면 버튼을 다시 활성화
            self.is_training = False  # 플래그 초기화
            return

        if os.path.exists(model_save):
            choice = QMessageBox.question(None, "파일 덮어쓰기",
                                          f"파일 '{os.path.basename(model_save)}'가 이미 존재합니다. 덮어쓰시겠습니까?",
                                          QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                shutil.rmtree(model_save)  # Delete the existing directory
            elif choice == QMessageBox.No:
                while os.path.exists(model_save):
                    model_dir_name = f"{model_dir}_{i}"
                    i += 1
        self.model_dir_edit.setText(model_dir_name)
        self.model_dir_changed()

        command = f'python ../EfficientAD-main/efficientad.py --dataset mvtec_ad --subdataset {self.model_dir_edit.text()} --output_dir {self.model_save_edit.text()}'
        self.thread = TrainingThread(command)
        self.thread.update_progress.connect(self.update_progress)
        self.thread.finished.connect(self.training_finished)
        self.thread.start()


    def update_progress(self, output):
        self.process.setText(output)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

    def training_finished(self, result):
        self.show_message_box("완료", result, QMessageBox.Information)
        self.train_button.setEnabled(True)  # 학습이 완료된 후 버튼을 다시 활성화
        self.is_training = False  # 플래그 초기화

    def show_message_box(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def read_process_output(self):
        output_text = ""
        while True:
            line = self.process.stdout.readline()
            if not line:
                break
            output_text += line
            self.process.setText(output_text)
            QtWidgets.QApplication.processEvents()  # Immediate update of QLabel
            self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())

        self.process.stdout.close()
        self.process.wait()
        # self.close_loading_screen()
        if self.process.returncode == 0:
            self.show_message_box("완료", "학습이 완료되었습니다.", QMessageBox.Information)
        else:
            self.show_message_box("오류", "학습 중 오류가 발생했습니다.", QMessageBox.Critical)
        self.process = None

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.show_message_box("성공", "명령이 성공적으로 실행되었습니다:\n" + result.stdout.decode('utf-8'), QMessageBox.Information)
        except subprocess.CalledProcessError as e:
            error_message = f"명령 실행 중 오류가 발생했습니다:\n{e.stderr.decode('utf-8')}"
            self.show_message_box("오류", error_message, QMessageBox.Critical)
        except Exception as e:
            self.show_message_box("오류", f"알 수 없는 오류가 발생했습니다: {e}", QMessageBox.Warning)

    def set_edit(self):
        selected_model_dir = os.path.join("../EfficientAD-main/output")
        model_name = self.comboBox.currentText()
        self.model_dir_edit.setText(model_name)
        selected_model_save_dir = os.path.join(selected_model_dir, self.model_dir_edit.text())
        self.model_save_edit.setText(selected_model_save_dir)


    def populate_directory_combo(self, combo):
        # './data' 디렉터리에서 디렉터리 명들을 읽어와 콤보박스에 추가합니다.
        try:
            directory = "../data"
            directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
            combo.addItems(directories)
        except Exception as e:
            QMessageBox.Warning(None, "경고", "data가 없습니다. 다시 확인해 주세요.")

    # 디렉토리 열기 함수
    def open_directory_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        directory_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory", "", options=options)
        if directory_path:
            self.model_save_edit.setText(directory_path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnomalyLearnWindow = QtWidgets.QMainWindow()
    ui = Ui_AnomalyLearnWindow()
    ui.setupUi(AnomalyLearnWindow)
    AnomalyLearnWindow.show()
    sys.exit(app.exec_())
