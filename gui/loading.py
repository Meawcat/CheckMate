from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget

class LoadingGif(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        import os
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)

    def initUI(self):
        self.setWindowTitle('로딩...')
        self.setFixedSize(300, 300)
        from PyQt5.QtCore import Qt
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        layout = QVBoxLayout()

        # 로딩 GIF 파일을 레이블에 설정합니다.
        self.label = QLabel(self)
        self.movie = QMovie("icons/loading2.gif")
        self.label.setMovie(self.movie)

        layout.addWidget(self.label)
        self.setLayout(layout)

    def start(self):
        self.movie.start()
        self.show()

    def stop(self):
        self.movie.stop()
        self.close()

