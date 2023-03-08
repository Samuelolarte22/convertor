import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog
from moviepy.editor import *


class VideoToAudio(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle('Convertidor de Audio a Video')

        self.label = QLabel('Seleccionar archivo de video:', self)
        self.label.move(50, 50)

        self.button = QPushButton('Seleccionar', self)
        self.button.move(350, 50)
        self.button.clicked.connect(self.selectFile)

        self.convertButton = QPushButton('Convertir', self)
        self.convertButton.move(200, 150)
        self.convertButton.clicked.connect(self.convert)

        self.show()

    def selectFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo', '', 'Video Files (*.mp4 *.mov)')
        self.filePath = fileName
        self.label.setText(f'Se seleccionó: {self.filePath}')

    def convert(self):
        video = VideoFileClip(self.filePath)
        audio = video.audio
        audio.write_audiofile(os.path.splitext(self.filePath)[0] + ".mp3")
        video.reader.close()
        video.audio.reader.close_proc()
        self.label.setText('La conversión se completó.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoToAudio()
    sys.exit(app.exec_())