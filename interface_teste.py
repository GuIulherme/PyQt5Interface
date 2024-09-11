#!/usr/bin/env python3

import sys
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import String, Empty
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

class CustomButton(QPushButton):
    def __init__(self, text, use_clicked=False, action=lambda: CustomButton.do_nothing):
        super().__init__(text)
        if use_clicked:
            self.clicked.connect(action)
        else:
            self.pressed.connect(action)
            self.released.connect(ros_adapter.stop)

    def do_nothing(self):
        pass

class ROSAdapter:
    def __init__(self):
        rospy.init_node('adapter_node')
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

class MainWindow(QMainWindow):
    def __init__(self, ros_adapter):
        super().__init__()
        self.setWindowTitle("Drone Control")
        self.setGeometry(100, 100, 800, 600)
        self.ros_adapter = ros_adapter

        main_layout = QVBoxLayout()

        camera_layout = self.create_camera_section("Camera drone")
        main_layout.addLayout(camera_layout)

        controls_layout = QHBoxLayout()
        controls_layout.addLayout(self.create_directional_control())
        controls_layout.addLayout(self.create_vertical_control())
        main_layout.addLayout(controls_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_image)
        self.timer.start(30)

        self.linear_vel = 0.5
        self.linear_z_vel = 0.5
        self.angular_vel = 1.0

    def create_camera_section(self, title):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(title))
        self.video_label = QLabel()
        self.video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.video_label.setScaledContents(True)
        layout.addWidget(self.video_label)
        layout.addWidget(CustomButton("Iniciar", True))
        layout.addWidget(CustomButton("Parar transmissão", True))
        return layout

    def create_directional_control(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Controle Direcional"))
        grid = QGridLayout()
        grid.addWidget(CustomButton("↖", action=lambda: self.ros_adapter.move(x=self.linear_vel, y=self.linear_vel)), 0, 0)
        grid.addWidget(CustomButton("↑", action=lambda: self.ros_adapter.move(x=self.linear_vel)), 0, 1)
        grid.addWidget(CustomButton("↗", action=lambda: self.ros_adapter.move(x=self.linear_vel, y=-self.linear_vel)), 0, 2)
        grid.addWidget(CustomButton("←", action=lambda: self.ros_adapter.move(y=self.linear_vel)), 1, 0)
        grid.addWidget(CustomButton("Start", True, action=lambda: self.ros_adapter.start_drone()), 1, 1)
        grid.addWidget(CustomButton("→", action=lambda: self.ros_adapter.move(y=-self.linear_vel)), 1, 2)
        grid.addWidget(CustomButton("↙", action=lambda: self.ros_adapter.move(x=-self.linear_vel, y=self.linear_vel)), 2, 0)
        grid.addWidget(CustomButton("↓", action=lambda: self.ros_adapter.move(x=-self.linear_vel)), 2, 1)
        grid.addWidget(CustomButton("↘", action=lambda: self.ros_adapter.move(x=-self.linear_vel, y=-self.linear_vel)), 2, 2)
        layout.addLayout(grid)
        return layout

    def create_vertical_control(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Controle Vertical e Rotação"))
        grid = QGridLayout()
        grid.addWidget(CustomButton("Subir", action=lambda: self.ros_adapter.move(z=self.linear_z_vel)), 0, 1)
        grid.addWidget(CustomButton("↺", action=lambda: self.ros_adapter.move(yaw=self.angular_vel)), 1, 0)
        grid.addWidget(CustomButton("O", True, action=lambda: self.ros_adapter.set_mark()), 1, 1)
        grid.addWidget(CustomButton("↻", action=lambda: self.ros_adapter.move(yaw=-self.angular_vel)), 1, 2)
        grid.addWidget(CustomButton("Descer", action=lambda: self.ros_adapter.move(z=-self.linear_z_vel)), 2, 1)
        layout.addLayout(grid)
        return layout

    def update_image(self):
        if self.ros_adapter.image is not None:
            height, width, channel = self.ros_adapter.image.shape
            bytes_per_line = 3 * width
            q_img = QImage(self.ros_adapter.image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.video_label.setPixmap(QPixmap.fromImage(q_img))

if __name__ == "__main__":
    rospy.init_node("adapter_node")
    rate = rospy.Rate(10)
    app = QApplication(sys.argv)
    ros_adapter = ROSAdapter()
    window = MainWindow(ros_adapter)
    window.show()
    sys.exit(app.exec_())