from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QWidget, QVBoxLayout, QPushButton, QMessageBox, QLabel, QMainWindow, QDialog, QHBoxLayout
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import os
import gui.anomaly_detect_window as anomaly_detection_window
from subprocess import run


class DetectionThread(QThread):
    detection_finished = pyqtSignal(list)

    def __init__(self, image_paths, weights_path, parent=None):
        super().__init__(parent)
        self.image_paths = image_paths
        self.weights_path = weights_path

    def get_latest_results_dir(self):
        base_path = '../yolov5/runs/detect'
        all_subdirs = [os.path.join(base_path, subdir) for subdir in os.listdir(base_path) if
                       os.path.isdir(os.path.join(base_path, subdir))]
        if not all_subdirs:
            return None
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        return latest_subdir

    def run(self):
        result_directories = []
        for image_path in self.image_paths:
            command = f'python ../yolov5/detect.py --source "{image_path}" --weights "{self.weights_path}" --conf 0.5 --project ../yolov5/runs/detect --name exp'
            print(f"Running command: {command}")
            run(command, shell=True)
            result_directories.append(self.get_latest_results_dir())
        self.detection_finished.emit(result_directories)


class Ui_YoloDetectImageWindow(object):
    def setupUi(self, YoloDetectImageWindow):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        YoloDetectImageWindow.setObjectName("YoloDetectImageWindow")
        YoloDetectImageWindow.resize(424, 321)
        YoloDetectImageWindow.setStyleSheet("background-color: #fff;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        YoloDetectImageWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(YoloDetectImageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.image_upload_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setBold(True)
        font.setWeight(75)
        self.image_upload_button.setFont(font)
        self.image_upload_button.setStyleSheet("QPushButton:hover {\n"
                                               "    color: #fff;\n"
                                               "}\n"
                                               "QPushButton {\n"
                                               "    border: none;\n"
                                               "    border-radius: 5px;\n"
                                               "    padding: 1px 5px;\n"
                                               "    background-color: #DBE2EF;\n"
                                               "    color: #112D4E;\n"
                                               "}")
        self.image_upload_button.setObjectName("image_upload_button")
        self.gridLayout.addWidget(self.image_upload_button, 0, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.yolo_detect_start_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setBold(True)
        font.setWeight(75)
        self.yolo_detect_start_button.setFont(font)
        self.yolo_detect_start_button.setStyleSheet("QPushButton:hover {\n"
                                                    "    color: #fff;\n"
                                                    "}\n"
                                                    "QPushButton {\n"
                                                    "    border: none;\n"
                                                    "    border-radius: 5px;\n"
                                                    "    padding: 1px 5px;\n"
                                                    "    background-color: #DBE2EF;\n"
                                                    "    color: #112D4E;\n"
                                                    "}")
        # Add a layout for the image list
        self.image_list_layout = QVBoxLayout()
        self.verticalLayout.addLayout(self.image_list_layout)

        self.yolo_detect_start_button.setObjectName("yolo_detect_start_button")
        self.verticalLayout.addWidget(self.yolo_detect_start_button)
        YoloDetectImageWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(YoloDetectImageWindow)
        QtCore.QMetaObject.connectSlotsByName(YoloDetectImageWindow)
        self.image_upload_button.clicked.connect(self.add_image)
        self.yolo_detect_start_button.clicked.connect(self.start_detection)

        # Initialize image_paths to store selected images
        self.image_paths = []
        self.image_paths.clear()
        self.weights_path = None
        self.update_image_list()

    def get_latest_results_dir(self):
        base_path = '../yolov5/runs/detect'
        all_subdirs = [os.path.join(base_path, subdir) for subdir in os.listdir(base_path) if
                       os.path.isdir(os.path.join(base_path, subdir))]
        if not all_subdirs:
            return None
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        return latest_subdir

    def start_detection(self):
        detect_base_path = '../yolov5/runs/detect'
        train_base_path = '../yolov5/runs/train'

        latest_train_dir = os.path.join(train_base_path, self.model_name)
        # Set weights_path to the best.pt file in the latest training directory
        if latest_train_dir:
            self.weights_path = os.path.join(latest_train_dir, 'weights', 'best.pt')
        else:
            self.weights_path = None

        # Debugging output for weights path
        print(f"Weights path: {self.weights_path}")
        print(f"Weights file exists: {os.path.exists(self.weights_path)}")

        # Check if image paths and weights file exist
        if not self.image_paths:
            print(
                "Condition failed. Either image paths are missing, weights path is not set, or the weights file does not exist.")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("경고")
            msg.setText("이미지를 추가하세요.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        elif not self.weights_path or not os.path.exists(self.weights_path):
            print(
                "Condition failed. Either image paths are missing, weights path is not set, or the weights file does not exist.")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("경고")
            msg.setText("해당 모델이 없습니다.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        # 비활성화하여 중복 실행 방지
        self.yolo_detect_start_button.setEnabled(False)

        # 비동기로 탐지 작업을 실행
        self.detection_thread = DetectionThread(self.image_paths, self.weights_path)
        self.detection_thread.detection_finished.connect(self.display_results)
        self.detection_thread.start()

    def retranslateUi(self, YoloDetectImageWindow):
        _translate = QtCore.QCoreApplication.translate
        YoloDetectImageWindow.setWindowTitle(_translate("YoloDetectImageWindow", "이미지 검출"))
        self.image_upload_button.setText(_translate("YoloDetectImageWindow", "이미지 추가"))
        self.yolo_detect_start_button.setText(_translate("YoloDetectImageWindow", "검출 시작"))

    def setModel(self, str):
        self.model_name = str

    def update_image_list(self):
        # Remove all widgets from the layout
        while self.image_list_layout.count() > 0:
            item = self.image_list_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Add new labels for each image path
        for path in self.image_paths:
            label = QLabel(path)
            self.image_list_layout.addWidget(label)

    def display_results(self, folders):
        font = QFont()
        font.setFamily("Noto Sans KR")
        self.result_window = QWidget()
        self.result_window.setWindowTitle("검출 결과")
        self.result_layout = QVBoxLayout()
        self.result_window.setLayout(self.result_layout)
        self.result_window.setStyleSheet("background-color: #fff;")
        # Create a horizontal layout for navigation buttons
        self.navigation_layout = QHBoxLayout()

        self.prev_button = QPushButton("이전", self.result_window)
        self.prev_button.setStyleSheet(
        "QPushButton:hover { color: #fff; }"
        "QPushButton {"
        "    border: none;"
        "    border-radius: 5px;"
        "    padding: 1px 5px;"
        "    background-color: #DBE2EF;"
        "    color: #112D4E;"
        "}")
        self.prev_button.setFont(font)
        self.prev_button.clicked.connect(self.show_prev_image)
        self.navigation_layout.addWidget(self.prev_button)

        self.next_button = QPushButton("다음", self.result_window)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet(
        "QPushButton:hover { color: #fff; }"
        "QPushButton {"
        "    border: none;"
        "    border-radius: 5px;"
        "    padding: 1px 5px;"
        "    background-color: #DBE2EF;"
        "    color: #112D4E;"
        "}")
        self.next_button.clicked.connect(self.show_next_image)
        self.navigation_layout.addWidget(self.next_button)

        self.result_layout.addLayout(self.navigation_layout)

        self.anomaly_button = QPushButton("이상 탐지", self.result_window)
        self.anomaly_button.setFont(font)
        self.anomaly_button.setStyleSheet(
        "QPushButton:hover { color: #fff; }"
        "QPushButton {"
        "    border: none;"
        "    border-radius: 5px;"
        "    padding: 1px 5px;"
        "    background-color: #DBE2EF;"
        "    color: #112D4E;"
        "}")
        self.anomaly_button.clicked.connect(self.open_anomaly_detection_dialog)
        self.result_layout.addWidget(self.anomaly_button)

        self.result_images = []
        for folder in folders:
            if folder is None:
                continue
            self.result_images += [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.jpg', '.png'))]

        self.current_image_index = 0
        self.image_label = QLabel(self.result_window)
        self.result_layout.addWidget(self.image_label)

        # 초기 창 크기 설정
        self.result_window.resize(800, 600)
        self.result_window.show()
        self.show_image()

        # 검출이 완료되면 다시 활성화
        self.yolo_detect_start_button.setEnabled(True)

    def open_anomaly_detection_dialog(self):
        dialog = QDialog()
        ui = anomaly_detection_window.Ui_anomaly_detection_window()
        ui.setupUi(dialog)
        dialog.exec_()

    def show_image(self):
        if not self.result_images:
            QMessageBox.information(self.result_window, "정보", "나타 낼 이미지가 없습니다.")
            return

        img_path = self.result_images[self.current_image_index]
        pixmap = QtGui.QPixmap(img_path)

        # QLabel의 고정 크기 설정
        fixed_width = 800
        fixed_height = 600
        self.image_label.setFixedSize(fixed_width, fixed_height)

        # QLabel에 맞추어 이미지를 비율을 유지하며 조정
        scaled_pixmap = pixmap.scaled(fixed_width, fixed_height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

    def show_next_image(self):
        if self.current_image_index < len(self.result_images) - 1:
            self.current_image_index += 1
            self.show_image()

    def show_prev_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_image()

    def add_image(self):
        print(self.model_name)
        file_paths, _ = QFileDialog.getOpenFileNames(None, "Select Images", "", "Image files (*.jpg;*.jpeg;*.png);;All files (*)")
        if file_paths:
            self.image_paths.extend(file_paths)
            self.update_image_list()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YoloDetectImageWindow = QMainWindow()
    ui = Ui_YoloDetectImageWindow()
    ui.setupUi(YoloDetectImageWindow)
    YoloDetectImageWindow.show()
    sys.exit(app.exec_())
