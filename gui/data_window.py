from PyQt5.QtWidgets import (
    QMessageBox, QFileDialog, QProgressDialog, QApplication, QDialog, QVBoxLayout, 
    QPushButton, QLabel, QHBoxLayout, QSlider
)
from PyQt5.QtCore import Qt, QProcess
from PyQt5.QtGui import QPainter, QColor
import os
import shutil
import yaml
import gui.dataset_dialog as dataset_dialog
import gui.add_dialog as add_dialog
import gui.label_dialog as label_dialog
from gui.yolo_crop import YoloCrop as YC
import gui.loading

class TutorialDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.next_button = QPushButton("다음")
        self.page_label = None
        self.prev_button = None
        self.page_layout = None
        self.label = None
        self.labels = None
        self.layout = None
        self.currentPage = 1
        self.initUI()
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)

    def initUI(self):
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
        self.selected_files_label = None
        self.ratio_label = None
        self.test_ratio = None
        self.test_label = None
        self.verLay4 = None
        self.valid_ratio = None
        self.item_name = None
        self.add_button = None
        self.file_button = None
        self.valid_label = None
        self.verLay2 = None
        self.train_slider = None
        self.train_ratio = None
        self.train_label = None
        self.verLay3 = None
        self.horLay = None
        self.verLay5 = None
        self.directory_combo = None
        self.combo_label = None
        self.layout = None
        self.split_button = None
        self.files = None
        self.recommend_label = None
        self.create_dataset_dialog = None

    def open_create_dataset(self):
        self.create_dataset_dialog = QDialog()
        ui = dataset_dialog.Ui_dataset_dialog()
        ui.setupUi(self.create_dataset_dialog)
        self.create_dataset_dialog.setWindowTitle("데이터셋 생성")
        self.combo_label = ui.combobox_label
        self.directory_combo = ui.comboBox
        self.populate_directory_combo(self.directory_combo)

        # 훈련 슬라이더 설정 (60~80)
        self.train_slider = ui.train_slider
        self.train_slider.setRange(60, 80)
        self.train_slider.setTickInterval(1)
        self.train_slider.valueChanged.connect(self.update_ratios)

        self.train_ratio = ui.train_ratio
        self.valid_ratio = ui.valid_ratio
        self.test_ratio = ui.test_ratio

        # 추천값 레이블 추가
        self.recommend_label = QLabel("*추천값*", self.create_dataset_dialog)
        self.recommend_label.setAlignment(Qt.AlignCenter)
        self.recommend_label.setVisible(False)
        ui.verticalLayout.insertWidget(2, self.recommend_label)  # 데이터 분할 비율을 조정해 주세요 밑에 추가

        self.split_button = ui.split_button
        self.split_button.clicked.connect(self.split_data_yolo)

        QMessageBox.information(self, None, "YOLOv5를 위한 데이터셋을 생성합니다.")
        self.create_dataset_dialog.exec_()

    def update_ratios(self):
        value = self.train_slider.value()
        self.train_ratio.setText(f"{value}")
        valid_test_ratio = (100 - value) // 2
        self.valid_ratio.setText(f"{valid_test_ratio}")
        self.test_ratio.setText(f"{valid_test_ratio}")

        # 추천값 표시
        if value == 70:
            self.recommend_label.setVisible(True)
        else:
            self.recommend_label.setVisible(False)

        self.repaint()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.train_slider is None:
            return

        painter = QPainter(self)

        # 슬라이더 배경 그리기
        slider_rect = self.train_slider.geometry()
        painter.setPen(Qt.NoPen)

        # 훈련 비율 색상
        painter.setBrush(QColor(0, 255, 0))
        train_width = int(slider_rect.width() * (int(self.train_ratio.text()) / 100))
        painter.drawRect(slider_rect.x(), slider_rect.y() + slider_rect.height() + 5, train_width, 10)

        # 검증 비율 색상
        painter.setBrush(QColor(255, 255, 0))
        valid_width = int(slider_rect.width() * (int(self.valid_ratio.text()) / 100))
        painter.drawRect(slider_rect.x() + train_width, slider_rect.y() + slider_rect.height() + 5, valid_width, 10)

        # 시험 비율 색상
        painter.setBrush(QColor(255, 0, 0))
        test_width = slider_rect.width() - train_width - valid_width
        painter.drawRect(slider_rect.x() + train_width + valid_width, slider_rect.y() + slider_rect.height() + 5, test_width, 10)

    def split_data_yolo(self):
        directory_name = self.directory_combo.currentText()
        script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트 디렉토리 가져오기
        directory = os.path.abspath(os.path.join(script_dir, '../data', directory_name))

        image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.jpg', '.png'))]
        txt_label_files = [f[:-4] + '.txt' for f in image_files if f[:-4] + '.txt' in os.listdir(directory)]
        xml_label_files = [f[:-4] + '.xml' for f in image_files if f[:-4] + '.xml' in os.listdir(directory)]
        label_files = txt_label_files + xml_label_files

        if not image_files:
            QMessageBox.warning(self, "경고", "해당 디렉터리 내 이미지가 존재하지 않습니다.")
            return
        elif len(image_files) < 10:
            QMessageBox.warning(self, "경고", "이미지의 수가 10장 이상이어야 합니다.")
            return
        elif len(label_files) != len(image_files):
            QMessageBox.warning(self, "경고", "이미지와 레이블 파일의 수가 일치하지 않습니다.")
            return

        # Train, validation, test ratios
        train_ratio = self.train_slider.value() / 100
        valid_ratio = (100 - self.train_slider.value()) / 2 / 100
        test_ratio = valid_ratio

        total = train_ratio + valid_ratio + test_ratio
        if total != 1:
            QMessageBox.warning(self, "경고", "슬라이더 값의 합이 100이 되어야 합니다.")
            return

        try:
            # Create directories
            for folder in ['train', 'valid', 'test']:
                folder_path = os.path.join(directory, folder)
                shutil.rmtree(folder_path, ignore_errors=True)  # Clear existing directories
                os.makedirs(os.path.join(folder_path, 'images'), exist_ok=True)
                os.makedirs(os.path.join(folder_path, 'labels'), exist_ok=True)

            total_files = len(image_files)
            train_count = int(train_ratio * total_files)
            valid_count = int(valid_ratio * total_files)
            test_count = total_files - train_count - valid_count

            for i, img in enumerate(image_files):
                if i < train_count:
                    dest_folder = 'train'
                elif i < train_count + valid_count:
                    dest_folder = 'valid'
                else:
                    dest_folder = 'test'

                img_dest = os.path.abspath(os.path.join(directory, dest_folder, 'images', img))
                lbl_dest = os.path.abspath(os.path.join(directory, dest_folder, 'labels', os.path.splitext(img)[0] + ('.txt' if os.path.splitext(img)[0] + '.txt' in txt_label_files else '.xml')))

                shutil.copy(os.path.join(directory, img), img_dest)
                shutil.copy(os.path.join(directory, os.path.basename(lbl_dest)), lbl_dest)

            QMessageBox.information(self, "성공", "YOLOv5 데이터셋 생성이 완료되었습니다.")
            self.make_yaml_file(directory)

            QMessageBox.information(self, None, "EfficientAD를 위한 데이터셋을 생성합니다.")
            self.split_data_anomaly(directory_name, image_files, label_files)

        except Exception as e:
            QMessageBox.critical(self, "오류", f"YOLOv5 데이터셋 생성 중 오류가 발생했습니다.: {str(e)}")
            return
    def split_data_anomaly(self, item, imgs, tags):
        progressDialog = QProgressDialog("이미지를 처리 중입니다...", "취소", 0, len(tags), self)
        progressDialog.setWindowModality(Qt.WindowModal)  # 모달 설정
        try:
            progressDialog.setCancelButton(None)  # 취소 버튼 비활성화
            progressDialog.setMinimumDuration(0)
            progressDialog.setAutoClose(True)
            progressDialog.show()

            yolo_crop = YC()
            good_images = []
            bad_images = []
            script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트 디렉토리 가져오기
            # 태그 파일을 기반으로 이미지를 분류합니다.
            for tag_file in tags:
                with open(os.path.join(script_dir, '../data', item, tag_file), 'r') as f:
                    first_char = f.read(1)
                    if first_char == '0':  # 첫 번째 문자가 '0'이면 'bad'
                        bad_images.append(tag_file[:-4] + '.jpg')  # 해당 이미지 파일을 'bad'로 추가
                    else:  # 그 외의 경우는 'good'
                        good_images.append(tag_file[:-4] + '.jpg')  # 해당 이미지 파일을 'good'으로 추가

            # 훈련 및 테스트용 이미지 개수 계산
            num_train_good_images = int(len(good_images) * 0.8)
            num_test_good_images = len(good_images) - num_train_good_images

            total_images = len(good_images) + len(bad_images)  # 전체 이미지 수 계산

            # 이미지 경로 설정
            yolo_crop.setinputpath(os.path.join(script_dir, "../data", item))

            # 훈련용 'good' 이미지 처리
            yolo_crop.setoutputpath(os.path.join(script_dir, "../EfficientAD-main/mvtec_anomaly_detection", item, "train/good"))
            for i, img in enumerate(good_images[:num_train_good_images], 1):
                corresponding_txt_file = os.path.splitext(img)[0] + '.txt'
                if corresponding_txt_file in tags:
                    yolo_crop.openfile(corresponding_txt_file, img)
                progressDialog.setValue(int(i / total_images * 100))  # 진행률 업데이트

            # 테스트용 'good' 이미지 처리
            yolo_crop.setoutputpath(os.path.join(script_dir, "../EfficientAD-main/mvtec_anomaly_detection", item, "test/good"))
            for i, img in enumerate(good_images[num_train_good_images:], num_train_good_images + 1):
                corresponding_txt_file = os.path.splitext(img)[0] + '.txt'
                if corresponding_txt_file in tags:
                    yolo_crop.openfile(corresponding_txt_file, img)
                progressDialog.setValue(int(i / total_images * 100))  # 진행률 업데이트

            # 'bad' 이미지 처리
            yolo_crop.setoutputpath(os.path.join(script_dir, "../EfficientAD-main/mvtec_anomaly_detection", item, "test/bad"))
            for i, img in enumerate(bad_images, num_train_good_images + 1):
                corresponding_txt_file = os.path.splitext(img)[0] + '.txt'
                if corresponding_txt_file in tags:
                    yolo_crop.openfile(corresponding_txt_file, img)
                progressDialog.setValue(int(i / total_images * 100))  # 진행률 업데이트

            progressDialog.setValue(100)
            QMessageBox.information(None, "성공", "EfficientAD 데이터셋 생성이 완료되었습니다.")

        except Exception as e:
            QMessageBox.critical(None, "오류", f"EfficientAD 데이터셋 생성 중 오류가 발생했습니다.: {str(e)}")
        finally:
            progressDialog.close()

    def make_yaml_file(self, dir):
        yaml_file_path = os.path.join(dir, "data.yaml")

        # 절대 경로로 변환
        abs_train_path = os.path.abspath(os.path.join(dir, 'train'))
        abs_val_path = os.path.abspath(os.path.join(dir, 'valid'))
        abs_test_path = os.path.abspath(os.path.join(dir, 'test'))

        # 데이터 예시 (필요에 따라 수정 가능)
        data = {
            'train': abs_train_path,
            'val': abs_val_path,
            'test': abs_test_path,
            'nc': 2,
            'names': ['bad', 'good']
        }

        try:
            # YAML 파일 작성
            with open(yaml_file_path, 'w') as yaml_file:
                yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True)
            QMessageBox.information(self, "완료", f"YAML 파일이 성공적으로 작성되었습니다: {yaml_file_path}")
        except Exception as e:
            QMessageBox.warning(self, "오류", f"YAML 파일 작성 중 오류가 발생했습니다: {e}")


    def populate_directory_combo(self, combo):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트 디렉토리 가져오기
            directory = os.path.join(script_dir, "../data")
            directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
            combo.addItems(directories)
        except Exception as e:
            QMessageBox.warning(None, "경고", "data가 없습니다. 다시 확인해 주세요.")

    def open_label_data(self):
        dialog = QDialog(self)
        ui = label_dialog.Ui_label_dialog()
        ui.setupUi(dialog)
        dialog.setWindowTitle("데이터 라벨링")
        ver = ui.verticalLayout
        self.item_combo = ui.item_combo
        self.populate_directory_combo(self.item_combo)
        self.label_button = ui.label_button
        self.label_label = ui.label_label

        def on_button_ok_clicked():
            dialog.close()
            item_name = self.item_combo.currentText().strip()  # 텍스트 불필요한 공백 제거

            if not item_name:
                QMessageBox.warning(self, "경고", "물품명을 입력하세요.")
                return

            script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트 디렉토리 가져오기
            self.image_directory = os.path.join(script_dir, '../data', item_name)

            if not os.path.exists(self.image_directory):
                QMessageBox.warning(self, "경고", "디렉터리가 존재하지 않습니다.")
                return

            img_files = [f for f in os.listdir(self.image_directory) if
                         f.lower().endswith('.jpg') or f.lower().endswith('.png')]
            if not img_files:
                QMessageBox.warning(self, "경고", "디렉터리에 이미지가 있어야 합니다.")
                return

            # 이미지가 있는 경우에만 라벨링 가능 메시지 표시
            QMessageBox.information(self, "알림", "이미지 라벨링이 가능합니다.")

            # TutorialDialog 인스턴스 생성
            tutorial_dialog = TutorialDialog()

            # exe 파일 경로 설정
            exe_path = os.path.join(script_dir, "../labelImg", 'labelImg.exe')
            if os.path.exists(exe_path) and exe_path.lower().endswith(".exe"):
                # QProcess 인스턴스 생성
                self.process = QProcess(self)
                # 프로세스 종료 시그널 연결
                self.process.finished.connect(lambda: tutorial_dialog.close())
                # exe 파일 실행
                self.process.start(exe_path)
                # 튜토리얼 다이얼로그 실행
                tutorial_dialog.exec_()
            else:
                QMessageBox.warning(self, "오류", "labelImg.exe 파일을 찾을 수 없거나 확장자가 올바르지 않습니다.")
                return

        self.label_button.clicked.connect(on_button_ok_clicked)
        dialog.exec_()

    def open_add_data(self):
        dialog = QDialog(self)
        ui = add_dialog.Ui_add_dialog()
        ui.setupUi(dialog)
        dialog.setWindowTitle("데이터 추가")
        self.file_button = ui.file_button
        file_label = ui.file_label
        self.add_button = ui.add_button
        item_label = ui.item_label
        self.item_name = ui.item_name
        self.item_name.setPlaceholderText("예) eraser, milk, ...")
        verlay2 = ui.verlay2
        verlay1 = ui.verlay1
        grid = ui.gridLayout
        scroll_area = ui.scrollArea
        self.selected_files_label = ui.selected
        scroll_widget = ui.scrollAreaWidgetContents
        # 버튼 클릭 시 연결될 메서드 설정
        self.file_button.clicked.connect(self.open_file_dialog)
        self.add_button.clicked.connect(self.add_data)

        dialog.exec_()

    def add_data(self):
        # 사용자가 입력한 데이터 이름 가져오기
        item_name_text = self.item_name.toPlainText().strip()

        if not item_name_text:
            QMessageBox.warning(self, "경고", "데이터 이름을 입력하세요.")
            return

        # 새 디렉터리 생성
        script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트 디렉토리 가져오기
        directory = os.path.join(script_dir, '../data', item_name_text)
        os.makedirs(directory, exist_ok=True)

        # 폴더 내 파일 수 측정
        existing_files = [f for f in os.listdir(directory) if f.lower().endswith(".jpg") or f.lower().endswith(".png")]
        file_count = len(existing_files)

        if not self.files:
            QMessageBox.warning(self, "경고", "추가할 데이터를 선택하세요.")
            return
        else:
            for index, file in enumerate(self.files, start=file_count + 1):
                src_file = file  # 파일 경로
                base_filename = f"{index:03d}"
                ext = os.path.splitext(src_file)[1]
                dest_file = os.path.join(directory, base_filename + ext)  # 대상 디렉토리에 파일 복사

                if os.path.exists(dest_file):
                    choice = QMessageBox.question(self, "파일 덮어쓰기",
                                                  f"파일 '{os.path.basename(dest_file)}'가 이미 존재합니다. 덮어쓰시겠습니까?",
                                                  QMessageBox.Yes | QMessageBox.No)
                    if choice == QMessageBox.Yes:
                        try:
                            os.remove(dest_file)
                            # 해당 파일의 확장자가 .jpg나 .jpeg, .png인 경우 동일한 이름의 txt 파일도 함께 삭제
                            if ext.lower() in ['.jpg', '.jpeg', '.png']:
                                txt_file = os.path.join(directory, base_filename + '.txt')
                                if os.path.exists(txt_file):
                                    os.remove(txt_file)
                            shutil.copy(src_file, dest_file)
                        except Exception as e:
                            QMessageBox.warning(self, "오류", f"파일을 덮어쓰는 중 오류가 발생했습니다: {e}")
                    else:
                        suffix = 1
                        while os.path.exists(os.path.join(directory, f"{base_filename}_{suffix:03d}{ext}")):
                            suffix += 1
                        new_file = os.path.join(directory, f"{base_filename}_{suffix}{ext}")
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
            # 완료되면 다시 초기화
            self.files = None
            self.selected_files_label.clear()

    def open_file_dialog(self):
        options = QFileDialog.Options()
        self.files, _ = QFileDialog.getOpenFileNames(self, "파일 선택", "",
                                                     "JPEG Files (*.jpg);;PNG Files (*.png)",
                                                     options=options)
        if self.files:
            self.selected_files_label.setWordWrap(True)
            self.selected_files_label.setText("선택된 파일: " + ",\n".join(self.files))
