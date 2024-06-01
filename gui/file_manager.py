import shutil
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QMessageBox, QFileDialog, QAction, \
    QLabel, QScrollArea, QVBoxLayout, QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QDir, QFileSystemWatcher

class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setStyleSheet("font-family: 'Noto Sans Kr'; font-size: 9pt;")
        self.tree_view = QTreeView()
        self.data_model = QFileSystemModel()
        # 데이터 디렉토리 경로 설정
        current_directory = QDir.currentPath()
        self.data_directory = os.path.join(current_directory, "data")
        if not os.path.exists(self.data_directory):
            os.mkdir(self.data_directory)

        # QFileSystemModel 설정
        self.data_model.setRootPath(self.data_directory)
        self.tree_view.setModel(self.data_model)
        self.tree_view.setRootIndex(self.data_model.index(self.data_directory))
        self.tree_view.setAnimated(False)
        self.tree_view.setIndentation(20)

        # 스크롤 영역 생성
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.tree_view)
        scroll_area.setWidgetResizable(True)
        self.tree_view.horizontalScrollBar().setStyleSheet(
                "QScrollBar:horizontal { border: none; background-color: #3F72AF; }"
        )
        self.tree_view.verticalScrollBar().setStyleSheet(
                "QScrollBar:vertical { border: none; background-color: #3F72AF; }"
        )
        # 메인 위젯 및 레이아웃 설정
        main_widget = QWidget()
        self.main_layout = QVBoxLayout(main_widget)
        self.label = QLabel("data 폴더 내부 디렉토리 및 파일 수")
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(scroll_area)
        self.setCentralWidget(main_widget)

        # 툴바 생성
        self.toolbar = self.addToolBar('파일 관리')

        # 삭제 버튼과 이벤트 연결
        delete_action = QAction('삭제', self)
        delete_action.triggered.connect(self.deleteFile)
        self.toolbar.addAction(delete_action)

        # 이동 버튼과 이벤트 연결
        move_action = QAction('이동', self)
        move_action.triggered.connect(self.moveFile)
        self.toolbar.addAction(move_action)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('File Manager')
        self.show()

        # 파일 시스템 감시자 설정
        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.addPath(self.data_directory)
        self.file_watcher.directoryChanged.connect(self.updateDirectoryInfo)
        self.file_watcher.fileChanged.connect(self.updateDirectoryInfo)

        # 모든 하위 디렉토리 및 파일 추가
        self.add_paths_to_watcher(self.data_directory)

        # 디렉토리 정보 업데이트
        self.updateDirectoryInfo()

    def add_paths_to_watcher(self, directory):
        """디렉토리 내 모든 서브 디렉토리 및 파일을 감시 목록에 추가"""
        for root, dirs, files in os.walk(directory):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                self.file_watcher.addPath(dir_path)
            for file_name in files:
                file_path = os.path.join(root, file_name)
                self.file_watcher.addPath(file_path)

    def updateDirectoryInfo(self):
        dir_info = ""
        for dir_name in os.listdir(self.data_directory):
            dir_path = os.path.join(self.data_directory, dir_name)
            if os.path.isdir(dir_path):
                img_count = len([f for f in os.listdir(dir_path) if f.endswith(('.jpg', '.png'))])
                txt_count = len([f for f in os.listdir(dir_path) if f.endswith('.txt') and f != "classes.txt"])
                dir_info += f"{dir_name} - 이미지 수: {img_count}, 라벨링 완료 수: {txt_count}\n"

        self.label.setText(f"data 폴더 내부 디렉토리 및 파일 수:\n{dir_info}")
        self.add_paths_to_watcher(self.data_directory)  # 새로운 파일 및 디렉토리를 감시 목록에 추가

    def deleteFile(self):
        indexes = self.tree_view.selectedIndexes()
        if not indexes:
            QMessageBox.warning(self, '경고', '삭제할 파일을 선택하세요.')
            return

        index = indexes[0]
        file_path = self.data_model.filePath(index)

        if os.path.exists(file_path):
            reply = QMessageBox.question(self, '삭제', f"정말 삭제하시겠습니까? :{file_path}?", QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
                QMessageBox.information(self, '삭제', f"{file_path}가 완전히 삭제되었습니다.")
                self.updateDirectoryInfo()  # 디렉토리 정보 업데이트

    def moveFile(self):
        indexes = self.tree_view.selectedIndexes()
        if not indexes:
            QMessageBox.warning(self, '경고', '이동할 파일을 선택하세요.')
            return

        index = indexes[0]
        file_path = self.data_model.filePath(index)

        new_location = QFileDialog.getExistingDirectory(self, "Select Directory", QDir(QDir.homePath()).dirName(), options=QFileDialog.ShowDirsOnly)

        if new_location:
            new_path = os.path.join(new_location, os.path.basename(file_path))
            if os.path.exists(new_path):
                QMessageBox.warning(self, '이동', f"이미 존재합니다. :{new_path}.")
            else:
                shutil.move(file_path, new_path)
                QMessageBox.information(self, '이동', f"{file_path}가 {new_path}로 이동하였습니다.")
                self.updateDirectoryInfo()  # 디렉토리 정보 업데이트

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileManager()
    sys.exit(app.exec_())
