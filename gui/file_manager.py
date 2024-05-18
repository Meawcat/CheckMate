import shutil
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QMessageBox, QFileDialog, QAction, QToolBar
from PyQt5.QtCore import QDir

class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tree_view = QTreeView()
        self.data_model = QFileSystemModel()
        # 데이터 디렉토리 경로 설정
        data_directory = "../data"
        root_path = QDir.rootPath()
        data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), data_directory))
        self.data_model.setRootPath(root_path)
        self.tree_view.setModel(self.data_model)
        self.tree_view.setRootIndex(self.data_model.index(data_directory))
        self.tree_view.setAnimated(False)
        self.tree_view.setIndentation(20)

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
        self.setCentralWidget(self.tree_view)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('File Manager')
        self.show()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileManager()
    sys.exit(app.exec_())
