from PyQt5.QtGui import QImage
import cv2, imutils
import numpy as np
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGridLayout

class VideoStream(QThread):
   frame_updated = pyqtSignal(QPixmap)


   def __init__(self, parent=None):
       super(VideoStream, self).__init__(parent)
       self.cap = cv2.VideoCapture(0)
       self.cap.set(cv2.CAP_PROP_FPS, 10)
       self.streaming = False


   def run(self):
       self.streaming = True
       while self.streaming:
           ret, frame = self.cap.read()
           if ret:
               frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
               frame = imutils.resize(frame, width=428, height=425)
               img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
               pixmap = QPixmap.fromImage(img)
               self.frame_updated.emit(pixmap)


   def stop(self):
       self.streaming = False
       self.cap.release()
