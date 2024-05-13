import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QFontDatabase, QIcon, QStandardItemModel, QStandardItem

from main_window import Ui_MainWindow
from PyQt5 import uic
from PyQt5.QtCore import *

class myMainWindow(QMainWindow):
    def __init__(self):
        super(myMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setFixedSize(QSize(800, 600))
        # self.setFixedWidth(600)
        # self.setFixedHeight(400)
        self.initUI()

        # 훈련
        self.folder_path1 = self.ui.lineEdit_2
        self.train_data_upload_btn = self.ui.train_data_upload_button
        self.yolo_btn = self.ui.yolo_button
        self.autoencoder_btn = self.ui.autoencoder_button

        self.init_signal_slot1()

    def init_signal_slot1(self):
        self.train_data_upload_btn.clicked.connect(self.get_folder_path1)
        self.yolo_btn.clicked.connect(self.start_yolo)
        self.autoencoder_btn.clicked.connect(self.start_autoencoder)

    def get_folder_path1(self):
        folder_path1 = str(QFileDialog.getExistingDirectory(self, "select Directory"))
        self.folder_path1.setText(folder_path1)

    def start_yolo(self):
        print("yolo")

    def start_autoencoder(self):
        print("autoencoder")    
        
        # 검출
        self.folder_path = self.ui.lineEdit
        self.upload_btn = self.ui.upload_button
        self.anomaly_btn= self.ui.anomaly_button

        self.init_signal_slot()

    def init_signal_slot(self):
        self.upload_btn.clicked.connect(self.get_folder_path)
        self.anomaly_btn.clicked.connect(self.start_detect)

    def get_folder_path(self):
        folder_path = str(QFileDialog.getExistingDirectory(self, "select Directory"))
        self.folder_path.setText(folder_path)

    def start_detect(self):
        print("detect")


    # 화면
    def initUI(self):
        self.setWindowTitle('체크메이트')
        self.setWindowIcon(QIcon('icons/icon.png'))
        #self.setGeometry(300, 300, 300, 200)
        self.show()
    # 버튼 클릭시 페이지 변경
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_home_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_data_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_learn_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_detect_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def on_helper_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)     



if __name__ == '__main__':
    app = QApplication(sys.argv)
    #fontDB = QFontDatabase()
    #fontDB.addApplicationFont('')
    window = myMainWindow()
    window.show()
    sys.exit(app.exec())
