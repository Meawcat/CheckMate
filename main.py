import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, QComboBox, QDialog
from PyQt5.QtGui import QIcon
from gui.main_window import Ui_MainWindow
from gui.data_window import DataPage as DP
from gui.yolo_learn_window import Ui_YoloLearnWindow # 학습에서 yolo 학습 추가
from gui.yolo_detect_image_window import Ui_YoloDetectImageWindow # 검출에서 yolo 이미지 추가
from gui.anomaly_learn_window import Ui_AnomalyLearnWindow
import gui.anomaly_detect_window as anomaly_detection_window
import os
import subprocess

class myMainWindow(QMainWindow):
    def __init__(self):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        super(myMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.combo = self.ui.comboBox
        self.initUI()
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)

        # 학습
        self.yolo_btn = self.ui.yolo_button
        self.efficientAD_btn = self.ui.efficientAD_button

        self.init_signal_slot1()

        # 데이터
        self.data_add_btn = self.ui.data_add_button
        self.data_label_btn = self.ui.data_label_button
        self.data_split_btn = self.ui.dataset_create_button

        self.init_data_btns()

        # 검출 + 수정함
        self.detect_image_btn = self.ui.detect_image_button
        self.detect_video_btn = self.ui.detect_video_button
        self.detect_push_btn = self.ui.pushButton
        self.detect_image_btn.clicked.connect(self.open_yolo_detect_image_window)
        self.detect_video_btn.clicked.connect(self.open_yolo_detect_live)
        self.detect_push_btn.clicked.connect(self.open_anomaly_detection_dialog)
        self.refresh = self.ui.refresh_button.clicked.connect(self.populate_directory_combo)

        # 시작화면을 홈화면으로
        self.ui.stackedWidget.setCurrentIndex(0)

    def init_data_btns(self):
        self.data_page = DP()
        self.data_add_btn.clicked.connect(self.data_page.open_add_data)
        self.data_label_btn.clicked.connect(self.data_page.open_label_data)
        self.data_split_btn.clicked.connect(self.data_page.open_create_dataset)

    def init_signal_slot1(self):
        self.yolo_btn.clicked.connect(self.start_yolo)
        self.efficientAD_btn.clicked.connect(self.start_efficientAD)

    def start_yolo(self):
        # yolo 학습 화면 띄우기
        self.yolo_window = QMainWindow()
        self.ui_yolo = Ui_YoloLearnWindow()
        self.ui_yolo.setupUi(self.yolo_window)
        self.yolo_window.show()
        self.populate_directory_combo()  # Ensure combo is updated after training

    def start_efficientAD(self):
        # EfficientAD 띄우기
        self.efficientAD = QMainWindow()
        self.ui_efficientAD = Ui_AnomalyLearnWindow()
        self.ui_efficientAD.setupUi(self.efficientAD)
        self.efficientAD.show()

    def open_yolo_detect_image_window(self):
        if not self.combo:
            QMessageBox.warning(None, "경고", "모델을 선택하세요.")
            return
        # 이미지 검출 페이지 연결
        print("open yolo detect image window")
        self.yolo_detect_image_window = QMainWindow()
        self.ui_yolo_detect_image = Ui_YoloDetectImageWindow()
        self.ui_yolo_detect_image.setModel(self.combo.currentText())
        self.ui_yolo_detect_image.setupUi(self.yolo_detect_image_window)
        self.yolo_detect_image_window.show()
        
    def open_anomaly_detection_dialog(self):
        dialog = QDialog()
        ui = anomaly_detection_window.Ui_anomaly_detection_window()
        ui.setupUi(dialog)
        dialog.exec_()

    def populate_directory_combo(self):
        # self.combo.clear()  # Clear all items from the combo box
        directory = 'yolov5/runs/train'
        if os.path.exists(directory) and os.path.isdir(directory):
            directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
            for d in directories:
                weights_path = os.path.join(directory, d, 'weights', 'best.pt')
                # 먼저 해당 weights 파일이 존재하는지 확인
                if os.path.exists(weights_path):
                    # combo에 이미 해당 이름의 아이템이 있는지 확인
                    is_already_added = False
                    for index in range(self.combo.count()):
                        if self.combo.itemText(index) == d:
                            is_already_added = True
                            break
                    # 동명의 아이템이 없는 경우에만 추가
                    if not is_already_added:
                        self.combo.addItem(d)

    def open_yolo_detect_live(self):
        combo_dir = 'yolov5/runs/train'
        model_name = self.combo.currentText()

        try:
            if os.path.exists(f"{combo_dir}/{model_name}/weights/best.pt"):
                command = f'python yolov5/detect.py --source 0 --weights {combo_dir}/{model_name}/weights/best.pt --conf 0.5'
                subprocess.Popen(command, shell=True)
            else:
                QMessageBox.information(None, "안내", "해당 파일에 학습 모델이 없습니다. 다시 선택하세요.")
                return
        except subprocess.CalledProcessError as e:
            # 오류 처리
            error_message = f"명령 실행 중 오류가 발생했습니다:\n{e.stderr.decode('utf-8')}"
            QMessageBox.critical(None, "오류", error_message)
        except Exception as e:
            # 예외 처리
            QMessageBox.warning(None, "오류", f"알 수 없는 오류가 발생했습니다: {e}")

    # 화면
    def initUI(self):
        self.setWindowTitle('체크메이트')
        self.setWindowIcon(QIcon('gui/icons/icon.png'))
        self.populate_directory_combo()  # Ensure combo is populated on startup
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
        self.populate_directory_combo() 

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
    window = myMainWindow()
    window.show()
    sys.exit(app.exec())
