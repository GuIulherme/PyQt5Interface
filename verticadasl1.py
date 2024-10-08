#!/usr/bin/env python3
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import String, Empty
from PyQt5 import QtCore, QtGui, QtWidgets
from cv_bridge import CvBridge, CvBridgeError
from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import QTimer,pyqtSignal, QThread
from PyQt5.QtGui import QImage, QPixmap
import cv2
import sys

class ROSAdapter:
    def __init__(self):
   
        rospy.init_node('interface_drone')
        self.vel_pub = rospy.Publisher("/velocidade_manual", Twist, queue_size=10)
        self.mark_pub = rospy.Publisher('/marca', String, queue_size=10)
        self.takeoff_pub = rospy.Publisher('/bebop/takeoff', Empty, queue_size=10)
        self.start_pub = rospy.Publisher("/start", Empty, queue_size=10)
        self.image_sub = rospy.Subscriber("/bebop2/camera_base/image_raw", Image, self.image_callback)
        self.bridge = CvBridge()
        self.image = None

        self.has_takeoff = False

    def move(self, x=0, y=0, z=0, yaw=0):
        velocidade = Twist()
        velocidade.linear.x = x
        velocidade.linear.y = y
        velocidade.linear.z = z
        velocidade.angular.z = yaw
        self.vel_pub.publish(velocidade)

    def stop(self):
        self.vel_pub.publish(Twist())

    def set_mark(self):
        self.mark_pub.publish("marca")

    def start_drone(self):
        msg = Empty()
        if not self.has_takeoff:
            self.takeoff_pub.publish(msg)
            self.has_takeoff = True
        else:
            self.start_pub.publish(msg)

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image = cv_image
        except CvBridgeError as e:
            print(e)

class CustomButton(QtWidgets.QPushButton):
    def __init__(self, parent, text, aleft, atop, awidth, aheight,
                 use_clicked=False, action=lambda: CustomButton.do_nothing):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(aleft, atop, awidth, aheight))
        
        font = QtGui.QFont()
        font.setPointSize(15)  # Ajuste o tamanho da fonte conforme necessário
        self.setFont(font)
        self.setText(text)

        if use_clicked:
            self.clicked.connect(action)
        else:
            self.pressed.connect(action)
            self.released.connect(ros_adapter.stop)

    def do_nothing(self):
        pass

class Ui_MainWindow(object):

    def __init__(self, ros_adapter):
        super().__init__()

        self.ros_interface = ros_adapter

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

# LABEL AGUARDANDO TRANSMISSÃO
        self.video_label = QLabel(self.CameraNormal)
        self.video_label.setGeometry(QtCore.QRect(10, 50, 498, 480))  
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

# LABEL AGUARDANDO TRANSMISSÃO
        self.video_label2 = QLabel(self.CameraTermic)
        self.video_label2.setGeometry(QtCore.QRect(42, 50, 498, 480))
        self.video_label2.setText("Aguardando transmissão...")
        self.video_label2.setStyleSheet("background-color: lightgreen") 

# FRAME VERTICAL



        self.frame_Vvertical = QtWidgets.QFrame(self.centralwidget)
        self.frame_Vvertical.setGeometry(QtCore.QRect(650, 900, 431, 321))
        self.frame_Vvertical.setObjectName("frame_Vvertical")
        self.frame_Vvertical.setContentsMargins(170, 0, 0, 0)

# LABEL DO EMOJI DA TORRE
        self.labelTorre = QtWidgets.QLabel(self.frame_Vvertical)
        font = QtGui.QFont()
        font.setPointSize(170)
        self.labelTorre.setFont(font)
        pixmap = QtGui.QPixmap("imgs/torre.png")
        self.labelTorre.setGeometry(QtCore.QRect(190, 0, 421, 311))

        pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
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



        self.BtDescer = CustomButton(self.frame_controles, "Descer", 510, 350, 71, 71, False, 
        action=lambda: self.ros_interface.move(z=-self.linear_z_vel))
        self.BtDescer.clicked.connect(self.move_cursor_down)

        
        self.BtOvo = CustomButton(self.frame_controles, "O", 510, 270, 71, 71, True, 
        action=lambda: self.ros_interface.set_mark())


        self.BtStart = CustomButton(self.frame_controles, "Start", 160, 260, 71, 71,
        True, action=lambda: self.ros_interface.start_drone())



        self.BtHorario = CustomButton(self.frame_controles, "⟳", 590, 270, 71, 71, False, 
        action=lambda: self.ros_interface.move(yaw=-self.angular_vel))



        self.BtAntihorario = CustomButton(self.frame_controles, "⟲", 430, 270, 71, 71, False, 
        action=lambda: self.ros_interface.move(yaw=self.angular_vel))



        self.BtSubir = CustomButton(self.frame_controles, "Subir", 510, 190, 71, 71, False, 
        action=lambda: self.ros_interface.move(z=self.linear_z_vel))
        self.BtSubir.clicked.connect(self.move_cursor_up)


        self.BtNoroeste = CustomButton(self.frame_controles, "↖", 80, 180, 71, 71, False, 
        action=lambda: self.ros_interface.move(x=self.linear_vel, y=-self.linear_vel))


        self.BtFrente = CustomButton(self.frame_controles, "↑", 160, 180, 71, 71, False, 
        action=lambda: self.ros_interface.move(x=self.linear_vel))
        self.BtFrente.clicked.connect(self.move_cursor_Straight)


        self.BtNordeste = CustomButton(self.frame_controles, "↗", 240, 180, 71, 71, False, 
        action=lambda: self.ros_interface.move(x=self.linear_vel, y=-self.linear_vel))




        self.BtEsquerda = CustomButton(self.frame_controles, "←", 80, 260, 71, 71, False, 
        action=lambda: self.ros_interface.move(y=self.linear_vel))
        self.BtEsquerda.clicked.connect(self.move_cursor_left)




        self.BtNoroeste = CustomButton(self.frame_controles, "↖", 80, 180, 71, 71, False, 
        action=lambda: self.ros_interface.move(x=self.linear_vel, y=-self.linear_vel))


        self.BtDireita = CustomButton(self.frame_controles, "→", 240, 260, 71, 71, False, 
        action=lambda: self.ros_interface.move(y=-self.linear_vel))
        self.BtDireita.clicked.connect(self.move_cursor_right)


        self.BtSul = CustomButton(self.frame_controles, "↓", 160, 340, 71, 71, False, 
        action=lambda: self.ros_interface.move(x=-self.linear_vel))
        self.BtSul.clicked.connect(self.move_cursor_South)

        #self.BtSudoeste = self.create_button(self.frame_controles, "↙", 80, 340, 71, 71, 15)
       # self.BtSudoeste.pressed.connect(lambda: self.ros_interface.move(x = -0.5, y = 0.5))
        #self.BtSudoeste.released.connect(lambda: self.ros_interface.stop())
        self.BtSudoeste = CustomButton(self.frame_controles, "↙", 80, 340, 71, 71, False, 
        action=lambda: self.ros_interface.move(x=-self.linear_vel, y=self.linear_vel))


        self.BtSudoeste = CustomButton(self.frame_controles, "↘", 240, 340, 71, 71, False, 
        action=lambda: self.ros_interface.move(x=-self.linear_vel, y=-self.linear_vel))

        self.BtCameraBaixo = CustomButton(self.frame_controles, "↓", 870, 340, 71, 71)

        self.BtCameraDireita = CustomButton(self.frame_controles, "→", 950, 270, 71, 71)

        self.BtCameraEsquerda = CustomButton(self.frame_controles, "←", 790, 270, 71, 71)

        self.BtCameraFrente = CustomButton(self.frame_controles, "↑", 870, 190, 71, 71)


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

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_image)
        self.timer.start(30)

        self.linear_vel = 0.5
        self.linear_z_vel = 0.5
        self.angular_vel = 1.0

 




# Matriz aerea
        self.labelAerea1 = [[None for _ in range(8)] for _ in range(8)]

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
        self.cursor_positionV = 4

        self.asterisks = [1, 2, 3, 4, 5]
        self.labels = [None for _ in range(len(self.asterisks))]

        for i in range(8):
            for j in range(8):
                labelAerea = QtWidgets.QLabel(" " if self.matrizAerea[i][j] == 0 else "*")
                font = QtGui.QFont()
                font.setPointSize(20)
                labelAerea.setFont(font)
                self.labelAerea1[i][j] = labelAerea
                labelAerea.setFixedSize(30, 30)
                self.gridLayout.addWidget(labelAerea, i, j)

        # Inicialização dos rótulos verticais
        for vertical_index in range(len(self.asterisks)):
            PosV = QtWidgets.QLabel(" " if self.asterisks[vertical_index] != 0 else "*")
            font = QtGui.QFont()
            font.setPointSize(27)  # Define o tamanho da fonte como 20 pontos
            PosV.setFont(font)
            self.labels[vertical_index] = PosV
            self.gridLayout2.addWidget(PosV, vertical_index, 0)

        self.update_cursorH()
        self.update_cursorV()

    def update_cursorH(self):
        for i in range(8):
            for j in range(8):
                if self.matrizAerea[i][j] != 0:
                    self.labelAerea1[i][j].setText("*" if [i, j] == self.cursor_positionA else " ")

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

    def move_cursor_up(self):
        if self.cursor_positionV > 0:  # Verifica se não está na primeira posição
         self.cursor_positionV -= 1
        self.update_cursorV()

    def move_cursor_down(self):
        if self.cursor_positionV < len(self.asterisks) - 1:  # Verifica se não está na última posição
            self.cursor_positionV += 1
        self.update_cursorV()

    def update_cursorV(self):
        for vertical_index in range(len(self.asterisks)):
            if vertical_index == self.cursor_positionV:
                self.labels[vertical_index].setText("❇")  # Cursor na posição atual
            else:
                self.labels[vertical_index].setText(" ")  # Asterisco nas outras posições


####PROBLEMA NA LINHA 681 NÃO TEM ATRIBUTO IMAGE
    def update_image(self):
        if self.ros_interface.image is not None:
            height, width, channel = self.ros_interface.image.shape
            bytes_per_line = 3 * width
            q_img = QImage(self.ros_interface.image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.video_label.setPixmap(QPixmap.fromImage(q_img))
     # MOVIMENTAÇÃO VERTICAL SUBIR E DESCER      
       

    def expand_camera(self):
        self.CameraNormal.setGeometry(QtCore.QRect(0, 0, 1082, 551))
        self.CameraTermic.hide()

        self.video_label.setGeometry(QtCore.QRect(140, 50, 850, 480))  # Defina as coordenadas e tamanho conforme necessário
        self.pushButton.setGeometry(QtCore.QRect(1000, 210, 31, 25))
        self.pushButton.setText("←")
        self.label_63.setGeometry(QtCore.QRect(470, 0, 241, 51))
        
    def retrieve_camera(self):
         
         self.CameraNormal.setGeometry(QtCore.QRect(0, 0, 550, 551))
         self.CameraTermic.show()
         self.video_label.setGeometry(QtCore.QRect(10, 50, 498, 480))  # Defina as coordenadas e tamanho conforme necessário
             

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



        self.video_label2.setGeometry(QtCore.QRect(300, 50, 850, 480))  
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 31, 25))
        self.pushButton_2.setText("→")
        self.label_62.setGeometry(QtCore.QRect(470, 0, 241, 51))
        
    def retrieve_infra(self):
         self.CameraTermic.setGeometry(QtCore.QRect(550, 0, 541, 551))
         self.CameraNormal.show()
        
         self.video_label2.setGeometry(QtCore.QRect(42, 50, 490, 480))  # Defina as coordenadas e tamanho conforme necessário

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
    rospy.init_node("interface_drone")
    app = QtWidgets.QApplication(sys.argv)
    ros_adapter = ROSAdapter()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(ros_adapter)
    ui.setupUi(MainWindow)
    MainWindow.show()
    rate = rospy.Rate(10)
    sys.exit(app.exec_())