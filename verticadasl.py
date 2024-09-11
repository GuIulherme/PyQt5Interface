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
        self.labelTorre = QtWidgets.QLabel(self.frame_Vvertical)
        font = QtGui.QFont()
        font.setPointSize(170)
        self.labelTorre.setFont(font)
        self.labelTorre.setObjectName("label")
        pixmap = QtGui.QPixmap("imgs/torre.png")
        self.labelTorre.setGeometry(QtCore.QRect(190, 0, 421, 311))

        pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)  # Redimensiona para 200x150, mantendo a proporção
        self.labelTorre.setPixmap(pixmap)

## GRID LAYOUT VERTICAL
        self.gridLayout2 = QGridLayout(self.frame_Vvertical)

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
        self.BtFrente.clicked.connect(self.move_cursor_Straight)

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
        self.BtEsquerda.clicked.connect(self.move_cursor_left)

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
        self.BtDireita.clicked.connect(self.move_cursor_right)

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
        self.BtSul.clicked.connect(self.move_cursor_South)

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


# VISTA AEREA
        self.frame_vAerea = QtWidgets.QFrame(self.centralwidget)
        self.frame_vAerea.setGeometry(QtCore.QRect(210, 900, 611, 321))
        self.frame_vAerea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vAerea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vAerea.setObjectName("frame_vAerea")




        #self.label_10.setGeometry(QtCore.QRect(120, 10, 500, 191))

        self.frame_matrizV = QtWidgets.QFrame(self.frame_vAerea)
        self.frame_matrizV.setGeometry(QtCore.QRect(220, 50, 250, 250))
        self.gridLayout = QGridLayout(self.frame_matrizV)

        self.label_10 = QtWidgets.QLabel(self.frame_matrizV)
        font = QtGui.QFont()
        font.setPointSize(180)
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 0, 0, 8, 8)

        

   ######   


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

        self.label_53.setText(_translate("MainWindow", "Vista aérea"))

        self.expanded_camera = False
        self.expanded_infra = False

 

# Inicializa o objeto de transmissão de vídeo
        self.video_stream = VideoStream()
        self.video_stream.frame_updated.connect(self.update_frame)

        self.video_stream2 = VideoStream()
        self.video_stream2.frame_updated.connect(self.update_frame2)


# Matriz aerea
        self.matrizAerea = [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 3],
            [4, 0, 0, 0, 0, 0, 0, 5],
            [6, 0, 0, 0, 0, 0, 0, 7],
            [8, 0, 0, 0, 0, 0, 0, 9],
            [1, 0, 0, 0, 0, 0, 0, 2],
            [3, 4, 5, 6, 7, 8, 9, 1],
        ]
        self.cursor_positionA = [0, 0]  # [row, col]

        self.labelAerea1 = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                labelAerea = QLabel(" " if self.matrizAerea[i][j] == 0 else "*")
                font = QtGui.QFont()
                font.setPointSize(20)
                labelAerea.setFont(font)
                self.labelAerea1[i][j] = labelAerea
                labelAerea.setFixedWidth(20)
                labelAerea.setFixedHeight(20)
                self.gridLayout.addWidget(labelAerea, i, j)

        self.update_cursorH()

    def move_cursor_Straight(self):
        new_row = max(0, self.cursor_positionA[0] - 1)
        if self.matrizAerea[new_row][self.cursor_positionA[1]] != 0:
            self.cursor_positionA[0] = new_row
        self.update_cursorH()

    def move_cursor_South(self):
        new_row = min(7, self.cursor_positionA[0] + 1)
        if self.matrizAerea[new_row][self.cursor_positionA[1]] != 0:
            self.cursor_positionA[0] = new_row
        self.update_cursorH()

    def move_cursor_left(self):
        new_col = max(0, self.cursor_positionA[1] - 1)
        if self.matrizAerea[self.cursor_positionA[0]][new_col] != 0:
            self.cursor_positionA[1] = new_col
        self.update_cursorH()

    def move_cursor_right(self):
        new_col = min(7, self.cursor_positionA[1] + 1)
        if self.matrizAerea[self.cursor_positionA[0]][new_col] != 0:
            self.cursor_positionA[1] = new_col
        self.update_cursorH()

    def update_cursorH(self):
        for i in range(8):
            for j in range(8):
                if self.matrizAerea[i][j] != 0:
                    self.labelAerea1[i][j].setText("*" if [i, j] == self.cursor_positionA else " ")
# Matriz vertical

        self.asterisks = [
            [1], [2], [3], [4], [5]
        ]
        self.cursor_positionV = 5

        for vertical_index in range(len(self.asterisks)):
            PosV = QLabel("@")
            font = QtGui.QFont()
            font.setPointSize(27)  # Define o tamanho da fonte como 20 pontos
            PosV.setFont(font)
            self.asterisks[vertical_index] = PosV  # Armazenar QLabel na lista    
            self.gridLayout2.addWidget(PosV, vertical_index, 1)
        self.update_cursorV()




# MOVIMENTAÇÃO VERTICAL SUBIR E DESCER      
    
    def move_cursor_up(self):
        self.cursor_positionV = max(0, self.cursor_positionV - 1)
        self.update_cursorV()

    def move_cursor_down(self):
        self.cursor_positionV = min(len(self.asterisks) - 1, self.cursor_positionV + 1)
        self.update_cursorV()

    
    def update_cursorV(self):
        for label in self.asterisks:
                label.setText(" ")  # Limpa o texto
                self.asterisks[self.cursor_positionV].setText("❇")  # Define o asterisco na posição do cursor
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
