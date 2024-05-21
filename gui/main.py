import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtGui import  QIcon

from main_window import Ui_MainWindow
from data_window import DataPage as DP
from yolo_learn_window import Ui_YoloLearnWindow # 학습에서 yolo 학습 추가
from yolo_detect_image_window import Ui_YoloDetectImageWindow # 검출에서 yolo 이미지 추가
from gui.anomaly_learn_window import Ui_AnomalyLearnWindow
import os

class myMainWindow(QMainWindow):
    def __init__(self):
        super(myMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setFixedSize(QSize(800, 600))
        # self.setFixedWidth(600)
        # self.setFixedHeight(400)
        self.initUI()
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)

        # 학습
        self.folder_path1 = self.ui.lineEdit_2
        self.train_data_upload_btn = self.ui.train_data_upload_button
        self.yolo_btn = self.ui.yolo_button
        self.efficientAD_btn = self.ui.efficientAD_button

        self.init_signal_slot1()

        # 데이터
        self.data_add_btn = self.ui.data_add_button
        self.data_label_btn = self.ui.data_label_button
        self.data_split_btn = self.ui.dataset_create_button

        self.init_data_btns()

        # 검출 + 수정함
        #self.folder_path = self.ui.lineEdit
        self.detect_image_btn = self.ui.detect_image_button
        self.detect_video_btn = self.ui.detect_video_button
        self.anomaly_detect_start_btn = self.ui.anomaly_detect_start_button


        self.init_signal_slot()

        # 시작화면을 홈화면으로
        self.ui.stackedWidget.setCurrentIndex(0)

    def init_data_btns(self):
        self.data_page = DP()
        self.data_add_btn.clicked.connect(self.data_page.open_add_data)
        self.data_label_btn.clicked.connect(self.data_page.open_label_data)
        self.data_split_btn.clicked.connect(self.data_page.open_create_dataset)

    def init_signal_slot1(self):
        self.train_data_upload_btn.clicked.connect(self.get_folder_path1)
        self.yolo_btn.clicked.connect(self.start_yolo)
        self.efficientAD_btn.clicked.connect(self.start_efficientAD)

    def get_folder_path1(self):
        folder_path1 = str(QFileDialog.getExistingDirectory(self, "select Directory"))
        self.folder_path1.setText(folder_path1)

    def start_yolo(self):
        # yolo 학습 화면 띄우기
        self.yolo_window = QMainWindow()
        self.ui_yolo = Ui_YoloLearnWindow()
        self.ui_yolo.setupUi(self.yolo_window)
        self.yolo_window.show()

    def start_efficientAD(self):
        # EfficientAD 띄우기
        self.efficientAD = QMainWindow()
        self.ui_efficientAD = Ui_AnomalyLearnWindow()
        self.ui_efficientAD.setupUi(self.efficientAD)
        self.efficientAD.show()

    def init_signal_slot(self):
        #self.upload_btn.clicked.connect(self.get_folder_path)
        self.detect_image_btn.clicked.connect(self.open_yolo_detect_image_window)
        self.detect_video_btn.clicked.connect(self.start_detect)
        self.anomaly_detect_start_btn.clicked.connect(self.start_detect)

    #def get_folder_path(self):
    #    folder_path = str(QFileDialog.getExistingDirectory(self, "select Directory"))
    #    self.folder_path.setText(folder_path)

    def open_yolo_detect_image_window(self):
        # 이미지 검출 페이지 연결
        print("open yolo detect image window")
        self.yolo_detect_image_window = QMainWindow()
        self.ui_yolo_detect_image = Ui_YoloDetectImageWindow()
        self.ui_yolo_detect_image.setupUi(self.yolo_detect_image_window)
        self.yolo_detect_image_window.show()

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
            # 버튼을 누르면 버튼의 배경 변경 추가
            btn.setStyleSheet("")
        active_button = btn_list[index]
        active_button.setStyleSheet("background-color: #a6aaaf")

    # 버튼 고정 추가
    def on_home_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.on_stackedWidget_currentChanged(0)
    def on_data_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.on_stackedWidget_currentChanged(1)
    def on_learn_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.on_stackedWidget_currentChanged(2)
    def on_detect_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.on_stackedWidget_currentChanged(3)
    def on_helper_button_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.on_stackedWidget_currentChanged(4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #fontDB = QFontDatabase()
    #fontDB.addApplicationFont('')
    window = myMainWindow()
    window.show()
    sys.exit(app.exec())
