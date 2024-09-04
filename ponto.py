import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

class DeslocamentoMatriz(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Deslocamento na Matriz")

        # Inicializar a matriz e a posição do asterisco
        self.matriz = [
    [1, 2, 3, 4, 5, 6, 7, 8],

    [9, 0, 0, 0, 0, 0, 0, 1],

    [2, 0, 0, 0, 0, 0, 0, 3],

    [4, 0, 0, 0, 0, 0, 0, 5],

    [6, 0, 0, 0, 0, 0, 0, 7],

    [8, 0, 0, 0, 0, 0, 0, 9],

    [1, 0, 0, 0, 0, 0, 0, 2],

    [3, 4, 5, 6, 7, 8, 9, 1],
        ]
        self.posicao_x = 0
        self.posicao_y = 0

        # Criar um layout para organizar os labels
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        # Criar os labels para representar a matriz
        self.labels = []
        for i in range(8):
            linha = []
            for j in range(8):
                label = QLabel(str(self.matriz[i][j]))
                label.setAlignment(Qt.AlignCenter)
                linha.append(label)
                self.grid_layout.addWidget(label, i, j)
            self.labels.append(linha)

        # Criar os botões de controle
        self.botao_cima = QPushButton("Cima")
        self.botao_baixo = QPushButton("Baixo")
        self.botao_esquerda = QPushButton("Esquerda")
        self.botao_direita = QPushButton("Direita")

        # Conectar os botões às funções de movimentação
        self.botao_cima.clicked.connect(self.mover_cima)
        self.botao_baixo.clicked.connect(self.mover_baixo)
        self.botao_esquerda.clicked.connect(self.mover_esquerda)
        self.botao_direita.clicked.connect(self.mover_direita)

        # Adicionar os botões à interface
        # ... (Você pode usar um layout para organizar os botões)

        # Atualizar a interface inicialmente
        self.atualizar_interface()

    def atualizar_interface(self):
        for i in range(8):
            for j in range(8):
                if i == self.posicao_y and j == self.posicao_x:
                    self.labels[i][j].setText("*")
                else:
                    self.labels[i][j].setText(str(self.matriz[i][j]))

    def mover_cima(self):
        if self.posicao_y > 0 and self.matriz[self.posicao_y - 1][self.posicao_x] != 0:
            self.posicao_y -= 1
            self.atualizar_interface()
    # ... funções mover_baixo, mover_esquerda, mover_direita de forma similar

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeslocamentoMatriz()
    window.show()
    sys.exit(app.exec_())