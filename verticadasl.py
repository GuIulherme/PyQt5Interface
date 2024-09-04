from PyQt5.QtGui import QImage
import cv2, imutils
import numpy as np
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGridLayout
from videostream import VideoStream

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 1861)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


# FRAME DA CAMERA COMUM
        self.CameraNormal = QtWidgets.QFrame(self.centralwidget)
        self.CameraNormal.setGeometry(QtCore.QRect(0, 0, 550, 551))
        self.CameraNormal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CameraNormal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CameraNormal.setObjectName("CameraNormal")



# BOTÃO PARA COMEÇAR A TRANSMISSÃO DE VIDEO
        self.pushButton_start = QtWidgets.QPushButton("Iniciar", self.CameraNormal)
        self.pushButton_start.setGeometry(QtCore.QRect(230, 50, 90, 25))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.clicked.connect(self.start_stream)
        

# BOTÃO PARA TERMINAR A TRANSMISSÃO
        self.pushButton_end = QtWidgets.QPushButton("Parar transmissão", self.CameraNormal)
        self.pushButton_end.setGeometry(QtCore.QRect(200, 77, 140, 30))
        self.pushButton_end.setObjectName("pushButton_end")
        self.pushButton_end.clicked.connect(self.end_stream)


# LABEL AGUARDANDO TRANSMISSÃO
        self.video_label = QLabel(self.CameraNormal)
        self.video_label.setGeometry(QtCore.QRect(10, 120, 498, 425))  # Defina as coordenadas e tamanho conforme necessário
        self.video_label.setText("Aguardando transmissão...")
        self.video_label.setStyleSheet("background-color: lightgreen") 


# BOTÃO PARA EXPANDIR A CAMERA
        self.pushButton = QtWidgets.QPushButton("→",self.CameraNormal)
        self.pushButton.setGeometry(QtCore.QRect(510, 210, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


# PARA EXPANDIR A CAMERA
        self.pushButton.clicked.connect(self.expand_camera)
        self.pushButton.clicked.connect(self.retrieve_camera)
        self.pushButton.clicked.connect(self.handle_camera_button)

# 
        self.label_63 = QtWidgets.QLabel(self.CameraNormal)
        self.label_63.setGeometry(QtCore.QRect(180, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")

        self.frame_Bateria = QtWidgets.QFrame(self.centralwidget)
        self.frame_Bateria.setGeometry(QtCore.QRect(0, 900, 211, 321))
        font = QtGui.QFont()
        font.setPointSize(120)

        self.frame_Bateria.setFont(font)
        self.frame_Bateria.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Bateria.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Bateria.setObjectName("frame_Bateria")

        self.label_39 = QtWidgets.QLabel(self.frame_Bateria)
        self.label_39.setGeometry(QtCore.QRect(60, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")

        self.label_Bateria = QtWidgets.QLabel(self.frame_Bateria)
        self.label_Bateria.setGeometry(QtCore.QRect(40, 130, 121, 71))
        self.label_Bateria.setText("")
        self.label_Bateria.setPixmap(QtGui.QPixmap("imgs/gui_battery_full_icon_157695(1).png"))
        self.label_Bateria.setObjectName("label_Bateria")

        self.label_42 = QtWidgets.QLabel(self.frame_Bateria)
        self.label_42.setGeometry(QtCore.QRect(70, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")

#   FRAME PARA A CAMERA TERMICA

        self.CameraTermic = QtWidgets.QFrame(self.centralwidget)
        self.CameraTermic.setGeometry(QtCore.QRect(550, 0, 541, 551))
        self.CameraTermic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CameraTermic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CameraTermic.setObjectName("CameraTermic")

#  Botão para expandir e retrair a camera
        self.pushButton_2 = QtWidgets.QPushButton(self.CameraTermic)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
#Funções do botão expandir
        self.pushButton_2.clicked.connect(self.expand_infra)
        self.pushButton_2.clicked.connect(self.retrieve_infra)
        self.pushButton_2.clicked.connect(self.handle_infra_button)

        self.label_62 = QtWidgets.QLabel(self.CameraTermic)
        self.label_62.setGeometry(QtCore.QRect(184 , 0, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")

# BOTÃO PARA COMEÇAR A TRANSMISSÃO DE VIDEO
        self.pushButton_start2 = QtWidgets.QPushButton("Iniciar", self.CameraTermic)
        self.pushButton_start2.setGeometry(QtCore.QRect(230, 50, 90, 25))
        self.pushButton_start2.setObjectName("pushButton_start")
        self.pushButton_start2.clicked.connect(self.start_stream)
        

# BOTÃO PARA TERMINAR A TRANSMISSÃO
        self.pushButton_end2 = QtWidgets.QPushButton("Parar transmissão", self.CameraTermic)
        self.pushButton_end2.setGeometry(QtCore.QRect(200, 77, 140, 30))
        self.pushButton_end2.setObjectName("pushButton_end")
        self.pushButton_end2.clicked.connect(self.end_stream2)


# LABEL AGUARDANDO TRANSMISSÃO
        self.video_label2 = QLabel(self.CameraTermic)
        self.video_label2.setGeometry(QtCore.QRect(42, 120, 490, 425))  # Defina as coordenadas e tamanho conforme necessário
        self.video_label2.setText("Aguardando transmissão...")
        self.video_label2.setStyleSheet("background-color: lightgreen") 

# FRAME VERTICAL



        self.frame_Vvertical = QtWidgets.QFrame(self.centralwidget)
        self.frame_Vvertical.setGeometry(QtCore.QRect(650, 900, 431, 321))
        self.frame_Vvertical.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Vvertical.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Vvertical.setObjectName("frame_Vvertical")
        self.frame_Vvertical.setContentsMargins(170, 0, 0, 0)

# LABEL DO EMOJI DA TORRE
        self.label = QtWidgets.QLabel(self.frame_Vvertical)
        font = QtGui.QFont()
        font.setPointSize(170)
        self.label.setFont(font)
        self.label.setObjectName("label")
        pixmap = QtGui.QPixmap("imgs/torre.png")
        self.label.setGeometry(QtCore.QRect(190, 0, 421, 311))

        pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)  # Redimensiona para 200x150, mantendo a proporção
        self.label.setPixmap(pixmap)

## GRID LAYOUT VERTICAL
        self.gridLayout = QGridLayout(self.frame_Vvertical)

# LABEL 2
        self.label_2 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_2.setGeometry(QtCore.QRect(120, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)

        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_3.setGeometry(QtCore.QRect(120, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_4.setGeometry(QtCore.QRect(120, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_5.setGeometry(QtCore.QRect(120, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_6.setGeometry(QtCore.QRect(120, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_7.setGeometry(QtCore.QRect(120, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_8.setGeometry(QtCore.QRect(120, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_9.setGeometry(QtCore.QRect(120, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_55 = QtWidgets.QLabel(self.frame_Vvertical)
        self.label_55.setGeometry(QtCore.QRect(230, 0, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.frame_controles = QtWidgets.QFrame(self.centralwidget)
        self.frame_controles.setGeometry(QtCore.QRect(0, 1220, 1081, 611))
        self.frame_controles.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_controles.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_controles.setObjectName("frame_controles")

        self.BtDescer = QtWidgets.QPushButton(self.frame_controles)
        self.BtDescer.setGeometry(QtCore.QRect(510, 350, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtDescer.setFont(font)
        self.BtDescer.setText("Descer")
        self.BtDescer.setObjectName("BtDescer")
        self.BtDescer.clicked.connect(self.move_cursor_down)

        #self.timer13 = QTimer(MainWindow)
        #self.timer13.timeout.connect(self.incrementar_Baixo)
      #  self.BtDescer.pressed.connect(self.start_Baixo)
       # self.BtDescer.released.connect(self.stop_Baixo)


        self.BtOvo = QtWidgets.QPushButton(self.frame_controles)
        self.BtOvo.setGeometry(QtCore.QRect(510, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)

        self.BtOvo.setFont(font)
        self.BtOvo.setText("O")
        self.BtOvo.setObjectName("BtOvo")
       # self.BtOvo.clicked.connect(self.botar_ovo)



        self.BtHorario = QtWidgets.QPushButton(self.frame_controles)
        self.BtHorario.setGeometry(QtCore.QRect(590, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtHorario.setFont(font)
        self.BtHorario.setText("⟳")
        self.BtHorario.setObjectName("BtHorario")
        
        #self.timer12 = QTimer(MainWindow)
         #self.timer12.timeout.connect(self.incrementar_Horario)
         #self.BtHorario.pressed.connect(self.start_Horario)
       #  self.BtHorario.released.connect(self.stop_Horario)   



        self.BtAntihorario = QtWidgets.QPushButton(self.frame_controles)
        self.BtAntihorario.setGeometry(QtCore.QRect(430, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtAntihorario.setFont(font)
        self.BtAntihorario.setText("⟲")
        self.BtAntihorario.setObjectName("BtAntihorario")

        #self.timer11 = QTimer(MainWindow)
         #self.timer11.timeout.connect(self.incrementar_Antihorario)
         #self.BtAntihorario.pressed.connect(self.start_Antihorario)
         #self.BtAntihorario.released.connect(self.stop_Antihorario)  


        self.BtSubir = QtWidgets.QPushButton(self.frame_controles)
        self.BtSubir.setGeometry(QtCore.QRect(510, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtSubir.setFont(font)
        self.BtSubir.setText("Subir")
        self.BtSubir.setObjectName("BtSubir")
        self.BtSubir.clicked.connect(self.move_cursor_up)


        #self.timer9 = QTimer(MainWindow)
         #self.timer9.timeout.connect(self.incrementar_Cima)
         #self.BtSubir.pressed.connect(self.start_Cima)
         #self.BtSubir.released.connect(self.stop_Cima)    



        self.BtNoroeste = QtWidgets.QPushButton(self.frame_controles)
        self.BtNoroeste.setGeometry(QtCore.QRect(80, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtNoroeste.setFont(font)
        self.BtNoroeste.setText("↖")
        self.BtNoroeste.setObjectName("BtNoroeste")

       # self.timer3 = QTimer(MainWindow)
        # self.timer3.timeout.connect(self.incrementar_diagonalEsquerdo_Frente)
        # self.BtNoroeste.pressed.connect(self.start_diagonalEsquerdo_Frente)
        # self.BtNoroeste.released.connect(self.stop_diagonalEsquerdo_Frente)



        self.BtFrente = QtWidgets.QPushButton(self.frame_controles)
        self.BtFrente.setGeometry(QtCore.QRect(160, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtFrente.setFont(font)
        self.BtFrente.setText("↑")
        self.BtFrente.setObjectName("BtFrente")

        #self.timer1 = QTimer(MainWindow)
         #self.timer1.timeout.connect(self.incrementar_frente) 
        # self.BtFrente.pressed.connect(self.start_increment_frente)
         # self.BtFrente.released.connect(self.stop_increment_frente)



        self.BtNordeste = QtWidgets.QPushButton(self.frame_controles)
        self.BtNordeste.setGeometry(QtCore.QRect(240, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtNordeste.setFont(font)
        self.BtNordeste.setText("↗")
        self.BtNordeste.setObjectName("BtNordeste")

      #  self.timer2 = QTimer(MainWindow)
        # self.timer2.timeout.connect(self.incrementar_diagonalDireito_Frente)
        # self.BtNordeste.pressed.connect(self.start_diagonalDireito_Frente)
         # self.BtNordeste.released.connect(self.stop_diagonalDireito_Frente)


        self.BtEsquerda = QtWidgets.QPushButton(self.frame_controles)
        self.BtEsquerda.setGeometry(QtCore.QRect(80, 260, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtEsquerda.setFont(font)
        self.BtEsquerda.setText("←")
        self.BtEsquerda.setObjectName("BtEsquerda")

       # self.timer4 = QTimer(MainWindow)
        # self.timer4.timeout.connect(self.incrementar_Esquerda)
        # self.BtEsquerda.pressed.connect(self.start_Esquerda)
         # self.BtEsquerda.released.connect(self.stop_Esquerda) 


        self.BtStop = QtWidgets.QPushButton(self.frame_controles)
        self.BtStop.setGeometry(QtCore.QRect(160, 260, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtStop.setFont(font)
        self.BtStop.setText("Stop")
        self.BtStop.setObjectName("BtStop")

     #    self.BtStop.clicked.connect(self.stop_Button)

        self.BtDireita = QtWidgets.QPushButton(self.frame_controles)
        self.BtDireita.setGeometry(QtCore.QRect(240, 260, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtDireita.setFont(font)
        self.BtDireita.setText("→")
        self.BtDireita.setObjectName("BtDireita")

     #   self.timer5 = QTimer(MainWindow)
        # self.timer5.timeout.connect(self.incrementar_Direita)
         #self.BtDireita.pressed.connect(self.start_Direita)
         #self.BtDireita.released.connect(self.stop_Direita)      

        self.BtSul = QtWidgets.QPushButton(self.frame_controles)
        self.BtSul.setGeometry(QtCore.QRect(160, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtSul.setFont(font)
        self.BtSul.setText("↓")
        self.BtSul.setObjectName("BtSul")

       # self.timer13 = QTimer(MainWindow)
         #self.timer13.timeout.connect(self.incrementar_Baixo)
        # self.BtSul.pressed.connect(self.start_Baixo)
         #self.BtSul.released.connect(self.stop_Baixo)  

        self.BtSudoeste = QtWidgets.QPushButton(self.frame_controles)
        self.BtSudoeste.setGeometry(QtCore.QRect(80, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtSudoeste.setFont(font)
        self.BtSudoeste.setText("↙")
        self.BtSudoeste.setObjectName("BtSudoeste")

        #self.timer8 = QTimer(MainWindow)
         #self.timer8.timeout.connect(self.incrementar_diagonalEsquerdo_Tras)
         #self.BtSudoeste.pressed.connect(self.start_diagonalEsquerdo_Tras)
        # self.BtSudoeste.released.connect(self.stop_diagonalEsquerdo_Tras) 


        self.BtSudeste = QtWidgets.QPushButton(self.frame_controles)
        self.BtSudeste.setGeometry(QtCore.QRect(240, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtSudeste.setFont(font)
        self.BtSudeste.setText("↘")
        self.BtSudeste.setObjectName("BtSudeste")

       # self.timer7 = QTimer(MainWindow)
        # self.timer7.timeout.connect(self.incrementar_diagonalDireito_Tras)
        # self.BtSudeste.pressed.connect(self.start_diagonalDireito_Tras)
         #self.BtSudeste.released.connect(self.stop_diagonalDireito_Tras) 


        self.BtCameraBaixo = QtWidgets.QPushButton(self.frame_controles)
        self.BtCameraBaixo.setGeometry(QtCore.QRect(870, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtCameraBaixo.setFont(font)
        self.BtCameraBaixo.setText("↓")
        self.BtCameraBaixo.setObjectName("BtCameraBaixo")
        self.BtCameraDireita = QtWidgets.QPushButton(self.frame_controles)
        self.BtCameraDireita.setGeometry(QtCore.QRect(950, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtCameraDireita.setFont(font)
        self.BtCameraDireita.setText("→")
        self.BtCameraDireita.setObjectName("BtCameraDireita")
        self.BtCameraEsquerda = QtWidgets.QPushButton(self.frame_controles)
        self.BtCameraEsquerda.setGeometry(QtCore.QRect(790, 270, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtCameraEsquerda.setFont(font)
        self.BtCameraEsquerda.setText("←")
        self.BtCameraEsquerda.setObjectName("BtCameraEsquerda")
        self.BtCameraFrente = QtWidgets.QPushButton(self.frame_controles)
        self.BtCameraFrente.setGeometry(QtCore.QRect(870, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BtCameraFrente.setFont(font)
        self.BtCameraFrente.setText("↑")
        self.BtCameraFrente.setObjectName("BtCameraFrente")
        self.label_40 = QtWidgets.QLabel(self.frame_controles)
        self.label_40.setGeometry(QtCore.QRect(860, 70, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_52 = QtWidgets.QLabel(self.frame_controles)
        self.label_52.setGeometry(QtCore.QRect(100, 70, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.label_54 = QtWidgets.QLabel(self.frame_controles)
        self.label_54.setGeometry(QtCore.QRect(460, 70, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.BtCameraEsquerda.raise_()
        self.BtDescer.raise_()
        self.BtOvo.raise_()
        self.BtHorario.raise_()
        self.BtAntihorario.raise_()
        self.BtSubir.raise_()
        self.BtNoroeste.raise_()
        self.BtFrente.raise_()
        self.BtNordeste.raise_()
        self.BtEsquerda.raise_()
        self.BtStop.raise_()
        self.BtDireita.raise_()
        self.BtSul.raise_()
        self.BtSudoeste.raise_()
        self.BtSudeste.raise_()
        self.BtCameraBaixo.raise_()
        self.BtCameraDireita.raise_()
        self.BtCameraFrente.raise_()
        self.label_40.raise_()
        self.label_52.raise_()
        self.label_54.raise_()
        self.frame_sensorV = QtWidgets.QFrame(self.centralwidget)
        self.frame_sensorV.setGeometry(QtCore.QRect(550, 550, 211, 351))
        self.frame_sensorV.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sensorV.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sensorV.setObjectName("frame_sensorV")
        self.label_43 = QtWidgets.QLabel(self.frame_sensorV)
        self.label_43.setGeometry(QtCore.QRect(40, 90, 131, 161))
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("imgs/WhatsApp_Image_2024-06-03_at_15.21.19-removebg-preview.png"))
        self.label_43.setObjectName("label_43")
        self.DangerVbaixo = QtWidgets.QLabel(self.frame_sensorV)
        self.DangerVbaixo.setGeometry(QtCore.QRect(70, 210, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.DangerVbaixo.setFont(font)
        self.DangerVbaixo.setObjectName("DangerVbaixo")
        self.DangerVcima = QtWidgets.QLabel(self.frame_sensorV)
        self.DangerVcima.setGeometry(QtCore.QRect(70, 80, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.DangerVcima.setFont(font)
        self.DangerVcima.setObjectName("DangerVcima")
        self.label_56 = QtWidgets.QLabel(self.frame_sensorV)
        self.label_56.setGeometry(QtCore.QRect(30, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.frame_sensorH = QtWidgets.QFrame(self.centralwidget)
        self.frame_sensorH.setGeometry(QtCore.QRect(760, 550, 321, 351))
        self.frame_sensorH.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sensorH.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sensorH.setObjectName("frame_sensorH")
        self.label_44 = QtWidgets.QLabel(self.frame_sensorH)
        self.label_44.setGeometry(QtCore.QRect(80, 110, 141, 161))
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap("imgs/drone_flying_camera_surveillance_aviation_icon_134041(1).png"))
        self.label_44.setObjectName("label_44")
        self.DangerHbaixo = QtWidgets.QLabel(self.frame_sensorH)
        self.DangerHbaixo.setGeometry(QtCore.QRect(110, 260, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.DangerHbaixo.setFont(font)
        self.DangerHbaixo.setObjectName("DangerHbaixo")
        self.DangerHwest = QtWidgets.QLabel(self.frame_sensorH)
        self.DangerHwest.setGeometry(QtCore.QRect(20, 150, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.DangerHwest.setFont(font)
        self.DangerHwest.setObjectName("DangerHwest")
        self.DangerHcima = QtWidgets.QLabel(self.frame_sensorH)
        self.DangerHcima.setGeometry(QtCore.QRect(110, 60, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.DangerHcima.setFont(font)
        self.DangerHcima.setObjectName("DangerHcima")
        self.DangerHeast = QtWidgets.QLabel(self.frame_sensorH)
        self.DangerHeast.setGeometry(QtCore.QRect(220, 150, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.DangerHeast.setFont(font)
        self.DangerHeast.setObjectName("DangerHeast")
        self.label_57 = QtWidgets.QLabel(self.frame_sensorH)
        self.label_57.setGeometry(QtCore.QRect(50, 0, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.frame_mapa = QtWidgets.QFrame(self.centralwidget)
        self.frame_mapa.setGeometry(QtCore.QRect(-1, 549, 551, 351))
        self.frame_mapa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mapa.setObjectName("frame_mapa")
        self.mapaIMG = QtWidgets.QLabel(self.frame_mapa)
        self.mapaIMG.setGeometry(QtCore.QRect(0, 10, 541, 331))
        self.mapaIMG.setText("")
        self.mapaIMG.setPixmap(QtGui.QPixmap("imgs/Screenshot from 2024-06-03 15-31-13.png"))
        self.mapaIMG.setObjectName("mapaIMG")


# VISAO AEREA
        self.frame_vAerea = QtWidgets.QFrame(self.centralwidget)
        self.frame_vAerea.setGeometry(QtCore.QRect(210, 900, 611, 321))
        self.frame_vAerea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vAerea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vAerea.setObjectName("frame_vAerea")


        self.label_10 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_10.setGeometry(QtCore.QRect(120, 90, 211, 191))
        font = QtGui.QFont()
        font.setPointSize(180)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_11.setGeometry(QtCore.QRect(110, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_12.setGeometry(QtCore.QRect(110, 120, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_13.setGeometry(QtCore.QRect(110, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_14.setGeometry(QtCore.QRect(140, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_15.setGeometry(QtCore.QRect(110, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_16.setGeometry(QtCore.QRect(110, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_17.setGeometry(QtCore.QRect(110, 210, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_18.setGeometry(QtCore.QRect(110, 180, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_19.setGeometry(QtCore.QRect(110, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_20.setGeometry(QtCore.QRect(170, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_21.setGeometry(QtCore.QRect(200, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_22.setGeometry(QtCore.QRect(230, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_23.setGeometry(QtCore.QRect(290, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_24.setGeometry(QtCore.QRect(260, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_25.setGeometry(QtCore.QRect(320, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_26.setGeometry(QtCore.QRect(320, 210, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_27.setGeometry(QtCore.QRect(320, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_28.setGeometry(QtCore.QRect(320, 180, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_29.setGeometry(QtCore.QRect(320, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_30.setGeometry(QtCore.QRect(320, 120, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_31.setGeometry(QtCore.QRect(320, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_32.setGeometry(QtCore.QRect(320, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_33.setGeometry(QtCore.QRect(290, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_34.setGeometry(QtCore.QRect(140, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_35.setGeometry(QtCore.QRect(170, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_36.setGeometry(QtCore.QRect(200, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_37.setGeometry(QtCore.QRect(230, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_38.setGeometry(QtCore.QRect(260, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")


        self.label_53 = QtWidgets.QLabel(self.frame_vAerea)
        self.label_53.setGeometry(QtCore.QRect(270, 0, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_63.setText(_translate("MainWindow", "Camera comum"))
        self.label_39.setText(_translate("MainWindow", "BATERIA"))
        self.label_42.setText(_translate("MainWindow", "100%"))
        self.pushButton_2.setText(_translate("MainWindow", "←"))
        self.label_62.setText(_translate("MainWindow", "Câmera Térmica"))







        self.label_55.setText(_translate("MainWindow", "Vista vertical"))
        self.label_40.setText(_translate("MainWindow", "Camera"))
        self.label_52.setText(_translate("MainWindow", "Controle direcional"))
        self.label_54.setText(_translate("MainWindow", " Controle Vertical"))
        self.DangerVbaixo.setText(_translate("MainWindow", "⚠️"))
        self.DangerVcima.setText(_translate("MainWindow", "⚠️"))
        self.label_56.setText(_translate("MainWindow", "Sensor vertical"))
        self.DangerHbaixo.setText(_translate("MainWindow", "⚠️"))
        self.DangerHwest.setText(_translate("MainWindow", "⚠️"))
        self.DangerHcima.setText(_translate("MainWindow", "⚠️"))
        self.DangerHeast.setText(_translate("MainWindow", "⚠️"))
        self.label_57.setText(_translate("MainWindow", "Sensor horizontal"))
        self.label_10.setText(_translate("MainWindow", "☒"))
        self.label_11.setText(_translate("MainWindow", "❇"))
        self.label_12.setText(_translate("MainWindow", "❇"))
        self.label_13.setText(_translate("MainWindow", "❇"))
        self.label_14.setText(_translate("MainWindow", "❇"))
        self.label_15.setText(_translate("MainWindow", "❇"))
        self.label_16.setText(_translate("MainWindow", "❇"))
        self.label_17.setText(_translate("MainWindow", "❇"))
        self.label_18.setText(_translate("MainWindow", "❇"))
        self.label_19.setText(_translate("MainWindow", "❇"))
        self.label_20.setText(_translate("MainWindow", "❇"))
        self.label_21.setText(_translate("MainWindow", "❇"))
        self.label_22.setText(_translate("MainWindow", "❇"))
        self.label_23.setText(_translate("MainWindow", "❇"))
        self.label_24.setText(_translate("MainWindow", "❇"))
        self.label_25.setText(_translate("MainWindow", "❇"))
        self.label_26.setText(_translate("MainWindow", "❇"))
        self.label_27.setText(_translate("MainWindow", "❇"))
        self.label_28.setText(_translate("MainWindow", "❇"))
        self.label_29.setText(_translate("MainWindow", "❇"))
        self.label_30.setText(_translate("MainWindow", "❇"))
        self.label_31.setText(_translate("MainWindow", "❇"))
        self.label_32.setText(_translate("MainWindow", "❇"))
        self.label_33.setText(_translate("MainWindow", "❇"))
        self.label_34.setText(_translate("MainWindow", "❇"))
        self.label_35.setText(_translate("MainWindow", "❇"))
        self.label_36.setText(_translate("MainWindow", "❇"))
        self.label_37.setText(_translate("MainWindow", "❇"))
        self.label_38.setText(_translate("MainWindow", "❇"))
        self.label_53.setText(_translate("MainWindow", "Vista aérea"))

        self.expanded_camera = False
        self.expanded_infra = False
        self.cursor_position = 5

 

# Inicializa o objeto de transmissão de vídeo
        self.video_stream = VideoStream()
        self.video_stream.frame_updated.connect(self.update_frame)

        self.video_stream2 = VideoStream()
        self.video_stream2.frame_updated.connect(self.update_frame2)

# Matriz vertical
        self.asterisks = []
        
        for i in range(5):
            PosV = QLabel("❇")
            font = QtGui.QFont()
            font.setPointSize(20)  # Define o tamanho da fonte como 20 pontos
            PosV.setFont(font)
            self.asterisks.append(PosV)
            self.gridLayout.addWidget(PosV, i, 1)
        self.update_cursor()

# MOVIMENTAÇÃO VERTICAL SUBIR E DESCER      
    
    def move_cursor_up(self):
        self.cursor_position = max(0, self.cursor_position - 1)
        self.update_cursor()

    def move_cursor_down(self):
        self.cursor_position = min(len(self.asterisks) - 1, self.cursor_position + 1)
        self.update_cursor()

    def update_cursor(self):
        for i, label in enumerate(self.asterisks):
            label.setText("*" if i == self.cursor_position else " ")

#    def VistaVerti(self):


    def start_stream(self):
        self.pushButton_start.setEnabled(False)
        self.pushButton_end.setEnabled(True)
        self.video_label.setText("Recebendo vídeo...")
        self.video_stream.start()


    def end_stream(self):
        self.pushButton_start.setEnabled(True)
        self.pushButton_end.setEnabled(False)
        self.video_label.setText("Aguardando transmissão...")
        self.video_stream.stop()
        self.video_stream.wait()
        del self.video_stream
        self.video_stream = VideoStream()
        self.video_stream.frame_updated.connect(self.update_frame)


    def update_frame(self, pixmap):
       self.video_label.setPixmap(pixmap)

    def starQt_stream2(self):
        self.pushButton_start2.setEnabled(False)
        self.pushButton_end2.setEnabled(True)
        self.video_label2.setText("Recebendo vídeo...")
        self.video_stream2.start()


    def end_stream2(self):
        self.pushButton_start2.setEnabled(True)
        self.pushButton_end2.setEnabled(False)
        self.video_label2.setText("Aguardando transmissão...")
        self.video_stream2.stop()
        self.video_stream2.wait()
        del self.video_stream2
        self.video_stream2 = VideoStream()
        self.video_stream2.frame_updated.connect(self.update_frame2)


    def update_frame2(self, pixmap):
       self.video_label2.setPixmap(pixmap)
################################
# Botões pra extender a camera normal

    def expand_camera(self):
        self.CameraNormal.setGeometry(QtCore.QRect(0, 0, 1082, 551))
        self.CameraTermic.hide()
       
        self.pushButton_start.setGeometry(QtCore.QRect(500, 50, 90, 25))
        self.pushButton_end.setGeometry(QtCore.QRect(470, 77, 140, 30))

        self.video_label.setGeometry(QtCore.QRect(300, 120, 498, 425))  # Defina as coordenadas e tamanho conforme necessário
        self.pushButton.setGeometry(QtCore.QRect(1000, 210, 31, 25))
        self.pushButton.setText("←")
        self.label_63.setGeometry(QtCore.QRect(470, 0, 241, 51))
        
    def retrieve_camera(self):
         
         self.CameraNormal.setGeometry(QtCore.QRect(0, 0, 550, 551))
         self.CameraTermic.show()
         self.video_label.setGeometry(QtCore.QRect(10, 120, 498, 425))  # Defina as coordenadas e tamanho conforme necessário
             
         self.pushButton_end.setGeometry(QtCore.QRect(200, 77, 140, 30))
         self.pushButton_start.setGeometry(QtCore.QRect(230, 50, 90, 25))
         self.pushButton.setGeometry(QtCore.QRect(510, 210, 31, 25))
         self.pushButton.setText("→")
         self.label_63.setGeometry(QtCore.QRect(180, 0, 171, 51))

    
    def handle_camera_button(self):
        if not self.expanded_camera:
            self.expand_camera()
            self.expanded_camera = True
        else:
            self.retrieve_camera()
            self.expanded_camera = False


#### Botão pra expandir camera infravermelho

    def expand_infra(self):
        self.CameraTermic.setGeometry(QtCore.QRect(0, 0, 1082, 551))
        self.CameraNormal.hide()

        self.pushButton_start2.setGeometry(QtCore.QRect(500, 50, 90, 25))
        self.pushButton_end2.setGeometry(QtCore.QRect(470, 77, 140, 30))

        self.video_label2.setGeometry(QtCore.QRect(300, 120, 498, 425))  
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 31, 25))
        self.pushButton_2.setText("→")
        self.label_62.setGeometry(QtCore.QRect(470, 0, 241, 51))
        
    def retrieve_infra(self):
         self.CameraTermic.setGeometry(QtCore.QRect(550, 0, 541, 551))
         self.CameraNormal.show()
        
         self.pushButton_start2.setGeometry(QtCore.QRect(230, 50, 90, 25))
         self.pushButton_end2.setGeometry(QtCore.QRect(200, 77, 140, 30))
         self.video_label2.setGeometry(QtCore.QRect(42, 120, 490, 425))  # Defina as coordenadas e tamanho conforme necessário

         self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 31, 25))
         self.pushButton_2.setText("←")
         self.label_62.setGeometry(QtCore.QRect(170, 0, 241, 51))

    def handle_infra_button(self):
        if not self.expanded_infra:
            self.expand_infra()
            self.expanded_infra = True
        else:
            self.retrieve_infra()
            self.expanded_infra = False



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
