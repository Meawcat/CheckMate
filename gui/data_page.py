import random
from PyQt5.QtWidgets import (
    QMessageBox, QFileDialog, QDialogButtonBox,
    QRadioButton, QComboBox, QTextEdit
)
from PyQt5.QtGui import QFont, QFontDatabase
import os
import subprocess
import shutil
from yolo_crop import YoloCrop as YC
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
import split_dialog
class TutorialDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.currentPage = 1
        self.initUI()

    def initUI(self):
        font_id = QFontDatabase.addApplicationFont("Pretendard-SemiBold.ttf")
        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.setFont(QFont(self.font_family))
        self.setWindowTitle("설명서")
        self.layout = QVBoxLayout()
        self.resize(400, 500)
        self.labels = [
            "Open Dir로 라벨링을 원하는 물품 폴더의 good 또는 bad 폴더를 선택하세요.",
            "Change Save Dir로 라벨링을 원하는 물품 폴더의 labels 폴더를 선택해 주세요.",
            "PascalVOC를 눌러 YOLO로 바꾼다... 이거 맞음??"
            "Create Rect Box로 이미지를 지정해 class를 선택한 후 save 버튼 혹은 Ctrl+S를 눌러 사각형을 저장합니다.",
            "데이터 관리 화면으로 돌아와 해당 물품의 labels 폴더에 저장이 되었는지 확인합니다."
        ]
        self.label = QLabel(self.labels[self.currentPage - 1])
        self.layout.addWidget(self.label)

        # 페이지 수를 표시하는 레이아웃 추가
        self.page_layout = QHBoxLayout()
        self.page_layout.setAlignment(Qt.AlignCenter)
        self.layout.addLayout(self.page_layout)

        self.prev_button = QPushButton("이전")
        self.prev_button.clicked.connect(self.prevPage)
        self.page_layout.addWidget(self.prev_button)

        self.page_label = QLabel(f"페이지: {self.currentPage}/{len(self.labels)}")
        self.page_layout.addWidget(self.page_label)

        self.next_button = QPushButton("다음")
        self.next_button.clicked.connect(self.nextPage)
        self.page_layout.addWidget(self.next_button)

        self.setLayout(self.layout)

        # 다이얼로그를 오른쪽에 위치시킵니다.
        screen_geometry = QApplication.desktop().screenGeometry()
        dialog_geometry = self.geometry()
        self.move(screen_geometry.width() - dialog_geometry.width(),
                  int((screen_geometry.height() - dialog_geometry.height()) / 2))

    def nextPage(self):
        self.currentPage += 1
        if self.currentPage <= len(self.labels):
            self.label.setText(self.labels[self.currentPage - 1])
            self.page_label.setText(f"페이지: {self.currentPage}/{len(self.labels)}")
        else:
            self.currentPage = len(self.labels)

    def prevPage(self):
        self.currentPage -= 1
        if self.currentPage >= 1:
            self.label.setText(self.labels[self.currentPage - 1])
            self.page_label.setText(f"페이지: {self.currentPage}/{len(self.labels)}")
        else:
            self.currentPage = 1



class DataPage(QDialog):
    def __init__(self):
        super().__init__()

    def open_ratio_data(self):
        dialog = QDialog()
        ui = split_dialog.Ui_split_dialog()
        ui.setupUi(dialog)

        self.layout = ui.layoutWidget
        self.combo_label = ui.combobox_label
        self.directory_combo = ui.comboBox
        self.populate_directory_combo()
        self.verLay5 = ui.verticalLayout_5
        self.horLay = ui.horizontalLayout
        self.verLay3 = ui.verticalLayout_3
        self.train_label = ui.train_label
        self.train_ratio = ui.train_ratio
        self.train_slider = ui.train_slider
        self.train_slider.setRange(60, 80)
        self.train_slider.setTickInterval(10)
        self.verLay2 = ui.verticalLayout_2
        self.valid_label = ui.valid_label
        self.valid_ratio = ui.valid_ratio
        self.valid_slider = ui.valid_slider
        self.valid_slider.setRange(10, 20)
        self.valid_slider.setTickInterval(10)
        self.verLay4 = ui.verticalLayout_4
        self.test_label = ui.test_label
        self.test_ratio = ui.test_ratio
        self.test_slider = ui.test_slider
        self.test_slider.setRange(10, 20)
        self.test_slider.setTickInterval(10)
        self.ratio_label = ui.ratio_label
        self.split_button = ui.split_button
        self.split_button.clicked.connect(self.split_data)

        # 각 슬라이더의 값 변경 시 해당 라벨을 업데이트합니다.
        self.train_slider.valueChanged.connect(self.update_train_label)
        self.valid_slider.valueChanged.connect(self.update_valid_label)
        self.test_slider.valueChanged.connect(self.update_test_label)

        dialog.exec_()

    def populate_directory_combo(self):
        # './data' 디렉터리에서 디렉터리 명들을 읽어와 콤보박스에 추가합니다.
        directory = './data'
        directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
        self.directory_combo.addItems(directories)

    def split_data(self):
        directory_name = self.directory_combo.currentText()
        directory = os.path.join('data', directory_name)

        image_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
        if not image_files:
            QMessageBox.warning(self, "경고", "이미지가 없어 분할을 진행할 수 없습니다.")
            return

        random.shuffle(image_files)  # 이미지 파일들을 랜덤으로 섞음

        label_files = [f[:-4] + '.txt' for f in image_files if f[:-4] + '.txt' in os.listdir(directory)]
        if len(label_files) != len(image_files):
            QMessageBox.warning(self, "경고", "이미지와 레이블 파일의 수가 일치하지 않습니다.")
            return

        # train_slider, valid_slider, test_slider의 값으로 데이터셋을 분할하도록 수정합니다.
        train_ratio = self.train_slider.value() / 100
        valid_ratio = self.valid_slider.value() / 100
        test_ratio = self.test_slider.value() / 100

        total = train_ratio + valid_ratio + test_ratio
        if total != 1:  # 합이 1이 되도록 조정
            QMessageBox.warning(self, "경고", "슬라이더 값의 합이 1이 되어야 합니다.")
            return

        try:
            # 디렉터리 생성
            train_dir = os.path.join(directory, 'train')
            valid_dir = os.path.join(directory, 'valid')
            test_dir = os.path.join(directory, 'test')
            for folder in [train_dir, valid_dir, test_dir]:
                if os.path.exists(folder):
                    shutil.rmtree(folder)
                os.makedirs(os.path.join(folder, 'images'), exist_ok=True)
                os.makedirs(os.path.join(folder, 'labels'), exist_ok=True)

            # 파일을 train, valid, test로 분할하여 복사
            total_files = len(image_files)
            train_count = int(train_ratio * total_files)
            valid_count = int(valid_ratio * total_files)
            test_count = int(test_ratio * total_files)

            print(f"total{total_files} train{train_count} valid{valid_count} test{test_count}")

            for i in range(total_files):
                image_file = image_files[i]
                label_file = label_files[i]
                dest_folder = None

                if i < train_count:
                    dest_folder = 'train'
                elif i < train_count + valid_count:
                    dest_folder = 'valid'
                else:
                    dest_folder = 'test'

                image_dest = os.path.join(directory, dest_folder, 'images', image_file)
                label_dest = os.path.join(directory, dest_folder, 'labels', label_file)

                shutil.copy(os.path.join(directory, image_file), image_dest)
                shutil.copy(os.path.join(directory, label_file), label_dest)

            QMessageBox.information(self, "완료", "데이터 분할이 완료되었습니다.")
        except Exception as e:
            QMessageBox.warning(self, "에러", str(e))

    # train_slider 값이 변경될 때 호출될 슬롯
    def update_train_label(self):
        value = self.train_slider.value()
        self.train_ratio.setText(f"Train: {value}%")

    # valid_slider 값이 변경될 때 호출될 슬롯
    def update_valid_label(self):
        value = self.valid_slider.value()
        self.valid_ratio.setText(f"Valid: {value}%")

    # test_slider 값이 변경될 때 호출될 슬롯
    def update_test_label(self):
        value = self.test_slider.value()
        self.test_ratio.setText(f"Test: {value}%")

    def open_label_data(self):
        dialog = QDialog()
        dialog.resize(500, 400)
        layout = QVBoxLayout()
        label = QLabel("데이터를 라벨링할 물품의 이름을 하나만 입력하세요. 예) eraser")
        layout.addWidget(label)
        text_edit = QTextEdit()
        text_edit.setFixedHeight(30)
        layout.addWidget(text_edit)
        button_ok = QPushButton("확인")

        def on_button_ok_clicked():
            item_name = text_edit.toPlainText().strip()  # text_edit의 텍스트를 가져옴 (양쪽 공백 제거)
            if not item_name:
                QMessageBox.warning(self, "경고", "물품명을 입력하세요.")
                return
            else:
                self.image_directory = os.path.join("data", item_name)
                # good 디렉터리가 존재하고 비어 있지 않은지 확인
                if os.path.exists(self.image_directory):
                    jpg_files = [f for f in os.listdir(self.image_directory) if f.endswith('.jpg')]
                    if not jpg_files:  # 디렉터리 내에 jpg 파일이 없는 경우
                        QMessageBox.warning(self, "경고", "디렉터리에 이미지가 있어야 합니다.")
                        return
                else:
                    QMessageBox.warning(self, "경고", "디렉터리가 존재하지 않습니다.")
                    return

                # 이미지가 있는 경우에만 라벨링 가능 메시지 표시
                QMessageBox.information(self, "알림", "이미지 라벨링이 가능합니다.")
                dialog.close()
                exe_path = os.path.join("labelImg", 'labelImg.exe')
                if os.path.exists(exe_path) and exe_path.endswith(".exe"):
                    # labelImg.exe 파일이 존재하고 확장자가 .exe인 경우 실행
                    process = subprocess.Popen([exe_path])
                    process.wait()  # labelImg.exe가 실행되는 동안 대기

                    # labelImg.exe가 종료되면 crop_yolo.py 실행
                    if process.returncode == 0:  # labelImg.exe가 정상 종료되었을 때
                        yolo_crop = YC()
                        yolo_crop.setpath(self.image_directory, os.path.join(self.image_directory, 'good_crop'))
                        listofall = os.listdir(yolo_crop.input_path)
                        listofjpg = [file for file in listofall if file.endswith(".jpg") or file.endswith(".JPG")]
                        listoftag = [file for file in listofall if file.endswith(".txt") or file.endswith(".TXT")]
                        for i in range(len(listofjpg)):
                            yolo_crop.openfile(listoftag[i], listofjpg[i])

                    else:
                        QMessageBox.warning(self, "Error", "labelImg 실행 중 오류가 발생했습니다.")
                else:
                    QMessageBox.warning(self, "Error", "labelImg.exe 파일을 찾을 수 없거나 확장자가 올바르지 않습니다.")

        button_ok.clicked.connect(on_button_ok_clicked)
        layout.addWidget(button_ok)
        dialog.setLayout(layout)
        dialog.exec_()

    def open_add_data(self):
        dialog = QDialog(self)

        dialog.setWindowTitle("데이터 추가")
        dialog.resize(500, 400)
        item_label = QLabel("추가할 데이터의 이름을 영문으로 작성해 주세요. 예) eraser, milk")

        self.item_name = QTextEdit()
        item_layout = QVBoxLayout()
        item_layout.addWidget(item_label)
        item_layout.addWidget(self.item_name)

        # 파일 찾기 버튼 생성
        self.files = None
        file_label = QLabel("추가할 데이터 파일들을 선택해 주세요.")
        self.selected_files_label = QLabel()  # 선택된 파일 이름을 나타낼 라벨
        file_button = QPushButton("파일 찾기")
        file_button.clicked.connect(self.open_file_dialog)
        file_layout = QVBoxLayout()
        file_layout.addWidget(file_label)
        file_layout.addWidget(self.selected_files_label)
        file_layout.addWidget(file_button)

        # Dialog layout 생성
        layout = QVBoxLayout()
        layout.addLayout(item_layout)
        layout.addSpacing(20)  # 간격 추가
        layout.addLayout(file_layout)
        layout.addSpacing(40)  # 간격 추가

        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.add_data)
        button_box.button(QDialogButtonBox.Ok).setText("확인")

        layout.addWidget(button_box)
        dialog.setLayout(layout)

        dialog.exec_()

    def add_data(self):
        # 사용자가 입력한 데이터 이름 가져오기
        item_name_text = self.item_name.toPlainText().strip()

        if not item_name_text:
            QMessageBox.warning(self, "경고", "데이터 이름을 입력하세요.")
            return

        # 새 디렉터리 생성
        directory = os.path.join('data', item_name_text)
        os.makedirs(directory, exist_ok=True)

        if not self.files:
            QMessageBox.warning(self, "경고", "추가할 데이터를 선택하세요.")
            return
        else:
            for file in self.files:
                src_file = file  # 파일 경로
                dest_file = os.path.join(directory, os.path.basename(file))  # 대상 디렉토리에 파일 복사
                if os.path.exists(dest_file):
                    choice = QMessageBox.question(self, "파일 덮어쓰기",
                                                  f"파일 '{os.path.basename(dest_file)}'가 이미 존재합니다. 덮어쓰시겠습니까?",
                                                  QMessageBox.Yes | QMessageBox.No)
                    if choice == QMessageBox.Yes:
                        try:
                            os.remove(dest_file)
                            # 해당 파일의 확장자가 .jpg나 .JPG인 경우 동일한 이름의 txt 파일도 함께 삭제
                            base_name, ext = os.path.splitext(os.path.basename(dest_file))
                            if ext.lower() in ['.jpg', '.jpeg']:
                                txt_file = os.path.join(directory, base_name + '.txt')
                                if os.path.exists(txt_file):
                                    os.remove(txt_file)
                            shutil.copy(src_file, dest_file)
                        except Exception as e:
                            QMessageBox.warning(self, "오류", f"파일을 덮어쓰는 중 오류가 발생했습니다: {e}")
                    else:
                        new_filename, ext = os.path.splitext(os.path.basename(dest_file))
                        i = 1
                        while os.path.exists(os.path.join(directory, f"{new_filename}_{i}{ext}")):
                            i += 1
                        new_file = os.path.join(directory, f"{new_filename}_{i}{ext}")
                        try:
                            shutil.copy(src_file, new_file)
                        except Exception as e:
                            QMessageBox.warning(self, "오류", f"새 파일을 복사하는 중 오류가 발생했습니다: {e}")
                else:
                    try:
                        shutil.copy(src_file, dest_file)
                    except Exception as e:
                        QMessageBox.warning(self, "오류", f"파일을 복사하는 중 오류가 발생했습니다: {e}")

        QMessageBox.information(self, "완료", "데이터 추가가 완료되었습니다.")

    def open_file_dialog(self):
        options = QFileDialog.Options()
        self.files, _ = QFileDialog.getOpenFileNames(self, "파일 선택", "", "All Files (*);;", options=options)
        if self.files:
            self.selected_files_label.setWordWrap(True)
            self.selected_files_label.setText("선택된 파일: " + ", ".join(self.files))


