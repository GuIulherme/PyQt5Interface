from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QGridLayout, QPushButton, QWidget, QVBoxLayout, QFrame
from PyQt5.QtGui import QPixmap


class MovementSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.matriz = [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 3],
            [4, 0, 0, 0, 0, 0, 0, 5],
            [6, 0, 0, 0, 0, 0, 0, 7],
            [8, 0, 0, 0, 0, 0, 0, 9],
            [1, 0, 0, 0, 0, 0, 0, 2],
            [3, 4, 5, 6, 7, 8, 9, 1]
        ]

        self.cursor_position = [0, 0]  # [row, col]

        # Criar um QFrame para a matriz
        self.frame_matrix = QFrame(self)
        self.frame_matrix.setFixedSize(300, 300)  # Tamanho fixo para o frame
        self.gridLayout = QGridLayout(self.frame_matrix)

        self.labels = [[None for _ in range(8)] for _ in range(8)]
        label_width = 20  # Largura desejada para o label (em pixels)
        label_height = 20  # Altura desejada para o label (em pixels)

        self.image_label = QLabel(self.frame_matrix)
        self.image_label.setText("☒")
        font = QtGui.QFont()
        font.setPointSize(220)
        self.image_label.setFont(font)
        #self.image_label.setGeometry(QtCore.QRect(120, 90, 500, 191))
        self.gridLayout.addWidget(self.image_label, 0, 0, 8, 8)

        for i in range(8):
            for j in range(8):
                label = QLabel("*")
                font = QtGui.QFont()
                font.setPointSize(20)
                label.setFont(font)
                self.labels[i][j] = label
                label.setFixedWidth(20)
                label.setFixedHeight(20)
                self.gridLayout.addWidget(label, i, j)

        self.update_cursor()

        # Botões de controle
        self.btn_up = QPushButton("Up")
        self.btn_down = QPushButton("Down")
        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")

        self.btn_up.clicked.connect(self.move_cursor_up)
        self.btn_down.clicked.connect(self.move_cursor_down)
        self.btn_left.clicked.connect(self.move_cursor_left)
        self.btn_right.clicked.connect(self.move_cursor_right)

        vbox = QVBoxLayout()
        vbox.addWidget(self.frame_matrix)  # Adicionar o frame da matriz
        vbox.addWidget(self.btn_up)
        vbox.addWidget(self.btn_down)
        vbox.addWidget(self.btn_left)
        vbox.addWidget(self.btn_right)

        self.setLayout(vbox)

    def move_cursor_up(self):
        new_row = max(0, self.cursor_position[0] - 1)
        if self.matriz[new_row][self.cursor_position[1]] != 0:
            self.cursor_position[0] = new_row
        self.update_cursor()

    def move_cursor_down(self):
        new_row = min(7, self.cursor_position[0] + 1)
        if self.matriz[new_row][self.cursor_position[1]] != 0:
            self.cursor_position[0] = new_row
        self.update_cursor()

    def move_cursor_left(self):
        new_col = max(0, self.cursor_position[1] - 1)
        if self.matriz[self.cursor_position[0]][new_col] != 0:
            self.cursor_position[1] = new_col
        self.update_cursor()

    def move_cursor_right(self):
        new_col = min(7, self.cursor_position[1] + 1)
        if self.matriz[self.cursor_position[0]][new_col] != 0:
            self.cursor_position[1] = new_col
        self.update_cursor()

    def update_cursor(self):
        for i in range(8):
            for j in range(8):
                if self.matriz[i][j] != 0:
                    self.labels[i][j].setText("*" if [i, j] == self.cursor_position else " ")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MovementSystem()
    window.show()
    sys.exit(app.exec_())