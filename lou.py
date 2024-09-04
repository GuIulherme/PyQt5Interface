import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout

class Rotas(QWidget):

    def __init__(self):

        super().__init__()
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.matrix_size = 5
        self.asterisks = []


        # Create the matrix of labels

        for i in range(self.matrix_size):
            row = []

            for j in range(self.matrix_size):
                label = QLabel("*")
                row.append(label)
                self.grid_layout.addWidget(label, i, j)

            self.asterisks.append(row)


        # ... rest of your code ...

        


        self.button_up = QPushButton("Cima")

        self.button_down = QPushButton("Baixo")


        self.button_right = QPushButton("Direita")

        self.button_left = QPushButton("Esquerda")


        self.grid_layout.addWidget(self.button_right, 5, 1)

        self.grid_layout.addWidget(self.button_left, 6, 1)


        self.grid_layout.addWidget(self.button_up, 5, 0)

        self.grid_layout.addWidget(self.button_down, 6, 0)


        self.cursor_position = (0, 0)


        self.button_right.clicked.connect(self.move_cursor_right)

        self.button_left.clicked.connect(self.move_cursor_left)


        self.button_up.clicked.connect(self.move_cursor_up)

        self.button_down.clicked.connect(self.move_cursor_down)


        self.update_cursor()

        print 
    def move_cursor_up(self):

        self.cursor_position = (max(0, self.cursor_position[0] - 1), self.cursor_position[1])

        self.update_cursor()


    def move_cursor_down(self):

        self.cursor_position = (min(self.matrix_size - 1, self.cursor_position[0] + 1), self.cursor_position[1])

        self.update_cursor()


    def move_cursor_left(self):

        # Only allow left movement if the cursor is at the right edge

        if self.cursor_position[1] == self.matrix_size - 1:

            self.cursor_position = (self.cursor_position[0], self.cursor_position[1])  # No movement

        else:

            self.cursor_position = (self.cursor_position[0], max(0, self.cursor_position[1] - 1))

        self.update_cursor()


    def move_cursor_right(self):

    # Only allow right movement if the cursor is at the leftmost edge (0th column) AND

    # either in the first or last row

        if self.cursor_position[1] == 0 and (self.cursor_position[0] == 0 or self.cursor_position[0] == self.matrix_size - 1):

          self.cursor_position = (self.cursor_position[0], self.cursor_position[1] + 1)

          self.update_cursor()


    def update_cursor(self):

        for i in range(self.matrix_size):

            for j in range(self.matrix_size):

                self.asterisks[i][j].setText("*" if (i, j) == self.cursor_position else " ")


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = Rotas()

    window.show()

    sys.exit(app.exec_())


