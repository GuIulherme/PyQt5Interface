from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
import time
import numpy as np
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QLabel, QTreeWidgetItem, QTreeWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPixmap

#CLASSE PARA FAZER A TRANSMISSÃO DO VIDEO
class VideoStream(QThread):
    frame_updated = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        super(VideoStream, self).__init__(parent)
        self.cap = cv2.VideoCapture(0)  # Substitua pelo caminho do seu vídeo local
        self.cap.set(cv2.CAP_PROP_FPS, 10)  # Set the desired frame rate (e.g., 10 FPS)
        self.streaming = False

    def run(self):
        self.streaming = True
        while self.streaming:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = imutils.resize(frame, width=1000, height=800)  # Redimensiona o frame para o tamanho desejado
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(img)
                self.frame_updated.emit(pixmap)

    def stop(self):
        self.streaming = False
        self.cap.release()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # self.timer.timeout.connect(self.increment_value)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1379, 872)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

#FRAME NA ESQUERDA QUE TEM A TABELA
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(0, 0, 451, 976))
        self.frame_1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_1.setObjectName("frame")

#### TABELA
        self.tree = QTreeWidget(self.frame_1)
        self.tree.setGeometry(QtCore.QRect(0, 0, 451, 976))  # Defina a geometria da árvore para ser a mesma do frame
        self.tree.setHeaderLabels(["Sentido", "Valor"])

## FRAME PRINCIPAL COM A TRANSMISSÃO DE VIDEO
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(450, 0, 1463, 976))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")

#BOTÃO PARA COMEÇAR A TRANSMISSÃO DE VIDEO
        self.pushButton_start = QtWidgets.QPushButton("Iniciar", self.frame_4)
        self.pushButton_start.setGeometry(QtCore.QRect(750, 5, 90, 25))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.clicked.connect(self.start_stream)

#LABEL AGUARDANDO TRANSMISSÃO
        self.video_label = QLabel(self.frame_4)
        self.video_label.setGeometry(QtCore.QRect(300, 70, 1300, 660))  # Defina as coordenadas e tamanho conforme necessário
        self.video_label.setText("Aguardando transmissão...")

# BOTÃO PARA TERMINAR A TRANSMISSÃO
        self.pushButton_end = QtWidgets.QPushButton("Parar transmissão", self.frame_4)
        self.pushButton_end.setGeometry(QtCore.QRect(730, 35, 140, 25))
        self.pushButton_end.setObjectName("pushButton_stop")
        self.pushButton_end.clicked.connect(self.end_stream)

# FRAME ONDE ESTA OS BOTÕES
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(450, 750, 1463, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")

        # botões/lado esquerdo
# BOTÃO QUE LEVA O DRONE PRA FRENTE 
        self.pushButton_frente = QtWidgets.QPushButton("↑", self.frame_2)
        self.pushButton_frente.setGeometry(QtCore.QRect(350, 20, 60, 55))
# FUNÇÕES DO BOTÃO FRENTE
        self.timer1 = QTimer(MainWindow)
        self.timer1.timeout.connect(self.incrementar_frente) 
        self.pushButton_frente.pressed.connect(self.start_increment_frente)
        self.pushButton_frente.released.connect(self.stop_increment_frente)

        self.pushButton_diagonalDireito_Frente = QtWidgets.QPushButton("↗", self.frame_2)
        self.pushButton_diagonalDireito_Frente.setGeometry(QtCore.QRect(460, 20, 60, 55))

        self.timer2 = QTimer(MainWindow)
        self.timer2.timeout.connect(self.incrementar_diagonalDireito_Frente)
        self.pushButton_diagonalDireito_Frente.pressed.connect(self.start_diagonalDireito_Frente)
        self.pushButton_diagonalDireito_Frente.released.connect(self.stop_diagonalDireito_Frente)
#####################3
        self.pushButton_diagonalEsquerdo_Frente = QtWidgets.QPushButton("↖", self.frame_2)
        self.pushButton_diagonalEsquerdo_Frente.setGeometry(QtCore.QRect(240, 20, 60, 55))

        self.timer3 = QTimer(MainWindow)
        self.timer3.timeout.connect(self.incrementar_diagonalEsquerdo_Frente)
        self.pushButton_diagonalEsquerdo_Frente.pressed.connect(self.start_diagonalEsquerdo_Frente)
        self.pushButton_diagonalEsquerdo_Frente.released.connect(self.stop_diagonalEsquerdo_Frente)

########333
        self.pushButton_Stop = QtWidgets.QPushButton("Stop", self.frame_2)
        self.pushButton_Stop.setGeometry(QtCore.QRect(350, 90, 60, 55))
        #função stop button
        self.pushButton_Stop.clicked.connect(self.stop_Button)
#################
        self.pushButton_esquerda = QtWidgets.QPushButton("←", self.frame_2)
        self.pushButton_esquerda.setGeometry(QtCore.QRect(270, 90, 60, 55))

        self.timer4 = QTimer(MainWindow)
        self.timer4.timeout.connect(self.incrementar_Esquerda)
        self.pushButton_esquerda.pressed.connect(self.start_Esquerda)
        self.pushButton_esquerda.released.connect(self.stop_Esquerda)      
################################
        self.pushButton_direita = QtWidgets.QPushButton("→", self.frame_2)
        self.pushButton_direita.setGeometry(QtCore.QRect(420, 90, 60, 55))
        
        self.timer5 = QTimer(MainWindow)
        self.timer5.timeout.connect(self.incrementar_Direita)
        self.pushButton_direita.pressed.connect(self.start_Direita)
        self.pushButton_direita.released.connect(self.stop_Direita)      

####################
        self.pushButton_tras = QtWidgets.QPushButton("↓", self.frame_2)
        self.pushButton_tras.setGeometry(QtCore.QRect(350, 160, 60, 55))

        self.timer6 = QTimer(MainWindow)
        self.timer6.timeout.connect(self.incrementar_Tras)
        self.pushButton_tras.pressed.connect(self.start_Tras)
        self.pushButton_tras.released.connect(self.stop_Tras)      


#################3
        self.pushButton_diagonalDireito_Tras = QtWidgets.QPushButton("↘", self.frame_2)
        self.pushButton_diagonalDireito_Tras.setGeometry(QtCore.QRect(460, 160, 60, 55))

        self.timer7 = QTimer(MainWindow)
        self.timer7.timeout.connect(self.incrementar_diagonalDireito_Tras)
        self.pushButton_diagonalDireito_Tras.pressed.connect(self.start_diagonalDireito_Tras)
        self.pushButton_diagonalDireito_Tras.released.connect(self.stop_diagonalDireito_Tras)         
#################
        self.pushButton_diagonalEsquerdo_Tras = QtWidgets.QPushButton("↙", self.frame_2)
        self.pushButton_diagonalEsquerdo_Tras.setGeometry(QtCore.QRect(240, 160, 60, 55))

        self.timer8 = QTimer(MainWindow)
        self.timer8.timeout.connect(self.incrementar_diagonalEsquerdo_Tras)
        self.pushButton_diagonalEsquerdo_Tras.pressed.connect(self.start_diagonalEsquerdo_Tras)
        self.pushButton_diagonalEsquerdo_Tras.released.connect(self.stop_diagonalEsquerdo_Tras)    


########### botoões/lado direito

        self.pushButton_cima = QtWidgets.QPushButton("↑", self.frame_2)
        self.pushButton_cima.setGeometry(QtCore.QRect(890, 20, 60, 55))

        self.timer9 = QTimer(MainWindow)
        self.timer9.timeout.connect(self.incrementar_Cima)
        self.pushButton_cima.pressed.connect(self.start_Cima)
        self.pushButton_cima.released.connect(self.stop_Cima)    

############## ovo

        self.pushButton_ovo = QtWidgets.QPushButton("O", self.frame_2)
        self.pushButton_ovo.setGeometry(QtCore.QRect(890, 90, 60, 55))

        self.pushButton_ovo.clicked.connect(self.botar_ovo)
############# antihorario

        self.pushButton_antihorario = QtWidgets.QPushButton("⟲", self.frame_2)
        self.pushButton_antihorario.setGeometry(QtCore.QRect(810, 90, 60, 55))

        self.timer11 = QTimer(MainWindow)
        self.timer11.timeout.connect(self.incrementar_Antihorario)
        self.pushButton_antihorario.pressed.connect(self.start_Antihorario)
        self.pushButton_antihorario.released.connect(self.stop_Antihorario)    

########## horario


        self.pushButton_horario = QtWidgets.QPushButton("⟳", self.frame_2)
        self.pushButton_horario.setGeometry(QtCore.QRect(970, 90, 60, 55))

        self.timer12 = QTimer(MainWindow)
        self.timer12.timeout.connect(self.incrementar_Horario)
        self.pushButton_horario.pressed.connect(self.start_Horario)
        self.pushButton_horario.released.connect(self.stop_Horario)   
########

        self.pushButton_baixo = QtWidgets.QPushButton("↓", self.frame_2)
        self.pushButton_baixo.setGeometry(QtCore.QRect(890, 160, 60, 55))

        self.timer13 = QTimer(MainWindow)
        self.timer13.timeout.connect(self.incrementar_Baixo)
        self.pushButton_baixo.pressed.connect(self.start_Baixo)
        self.pushButton_baixo.released.connect(self.stop_Baixo)    

        

        # Variáveis para armazenar a direção

        self.value = 0
        self.ovo = 0


        self.valores = []

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1379, 22))
        self.menubar.setObjectName("menubar")

        self.menudd = QtWidgets.QMenu(self.menubar)
        self.menudd.setObjectName("menudd")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menudd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# Inicializa o objeto de transmissão de vídeo
        self.video_stream = VideoStream()
        self.video_stream.frame_updated.connect(self.update_video)

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
        self.video_stream.wait()  # Aguarda o término do thread
        del self.video_stream  # Remove a instância do objeto
        self.video_stream = VideoStream()  # Cria uma nova instância do objeto
        self.video_stream.frame_updated.connect(self.update_video)

    def update_video(self, pixmap):
        self.video_label.setPixmap(pixmap)
############### fim das funções de stream de video

    #função dos botões 
    def incrementar_frente(self):
        self.value = 1 # Enquanto segurar o valor continuará 1 e sera imprimido na tela, essa logica segue para os demais botões
        print(self.value)

    def start_increment_frente(self):
        self.timer1.start(45)  # Faz a função de 45 milisegundos

    def stop_increment_frente(self):
        self.value = 0  # O value voltará a ser 0 ao parar de ser segurado
        self.timer1.stop()
        print(self.value)

#######
    def incrementar_diagonalDireito_Frente(self):
        self.value = 2
        print(self.value)

    def start_diagonalDireito_Frente(self):
        self.timer2.start(45)  # 

    def stop_diagonalDireito_Frente(self):
        self.value = 0
        self.timer2.stop()
        print(self.value)

 #############################################3
    def incrementar_diagonalEsquerdo_Frente(self):
        self.value = 3
        print(self.value)

    def start_diagonalEsquerdo_Frente(self):
        self.timer3.start(45)  # 

    def stop_diagonalEsquerdo_Frente(self):
        self.value = 0
        self.timer3.stop()
        print(self.value)

# PARADA TOTAL
    def stop_Button(self):
        self.value = 0
        print(self.value)

#Botão esquerda
    def incrementar_Esquerda(self):
        self.value = 4
        print(self.value)

    def start_Esquerda(self):
        self.timer4.start(45)  # 

    def stop_Esquerda(self):
        self.value = 0
        self.timer4.stop()
        print(self.value)

#Botão direito
    def incrementar_Direita(self):
        self.value = 5
        print(self.value)

    def start_Direita(self):
        self.timer5.start(45)  # 

    def stop_Direita(self):
        self.value = 0
        self.timer5.stop()
        print(self.value)

#Botão tras
    def incrementar_Tras (self):
        self.value = 6
        print(self.value)

    def start_Tras(self):
        self.timer6.start(45)  # 

    def stop_Tras(self):
        self.value = 0
        self.timer6.stop()
        print(self.value)

#Botão diagonalDireitoTras
    def incrementar_diagonalDireito_Tras (self):
        self.value = 7
        print(self.value)

    def start_diagonalDireito_Tras(self):
        self.timer7.start(45)  # 

    def stop_diagonalDireito_Tras(self):
        self.value = 0
        self.timer7.stop()
        print(self.value)

#Botão diagonalEsquerdoTras
    def incrementar_diagonalEsquerdo_Tras (self):
        self.value = 8
        print(self.value)

    def start_diagonalEsquerdo_Tras(self):
        self.timer8.start(45)  # 

    def stop_diagonalEsquerdo_Tras(self):
        self.value = 0
        self.timer8.stop()
        print(self.value)

#Botão Cima
    def incrementar_Cima(self):
        self.value = 9
        print(self.value)

    def start_Cima(self):
        self.timer9.start(45)  

    def stop_Cima(self):
        self.value = 0
        self.timer9.stop()
        print(self.value)

###### ovo botão
    def botar_ovo(self):
        self.ovo += 1
        print(self.ovo)


#### botão baixo

## FUNÇÃO VIRAR ANTIHORARIO
    def incrementar_Antihorario(self):
        self.value = 11
        print(self.value)

    def start_Antihorario(self):
        self.timer11.start(45)  # 

    def stop_Antihorario(self):
        self.value = 0
        self.timer11.stop()
        print(self.value)

## FUNÇÃO VIRAR HORARIO
    def incrementar_Horario(self):
        self.value = 12
        print(self.value)

    def start_Horario(self):
        self.timer12.start(45)  # 

    def stop_Horario(self):
        self.value = 0
        self.timer12.stop()
        print(self.value)

## FUNÇÃO BOTÃO BAIXO
    def incrementar_Baixo(self):
        self.value = 13
        print(self.value)

    def start_Baixo(self):
        self.timer13.start(45)  # 

    def stop_Baixo(self):
        self.value = 0
        self.timer13.stop()
        print(self.value)

## APAGAR


    #def imprimir_valores(self):
     #   self.tree.clear()
      #  sentidos = ["Direita", "Esquerda", "Frente", "Tras", "Cima", "Baixo", "Ovo", "Horario", "Anti-horario", "Teste"]
       # valores = [self.Direitavar, self.Esquerdavar, self.Frentevar, self.Trasvar, self.Cimavar, self.Baixovar, self.Ovovar, self.Horariovar, self.Antivar, self.value]
        #for sentido, valor in zip(sentidos, valores):
         #   item = QTreeWidgetItem([sentido, str(valor)])
          #  self.tree.addTopLevelItem(item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menudd.setTitle(_translate("MainWindow", "dd"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
