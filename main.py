import PySimpleGUI as psg
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow, QHBoxLayout, QTabWidget, \
    QPushButton
import sys

from game import Game
# TODO reste a finir le ui de la game tout les fonctionnalité sont la


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = Game()
        # set the title of main window
        self.setWindowTitle('Sidebar layout - www.luochang.ink')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # add all widgets
        self.btn_1 = QPushButton('Programmer', self)
        self.btn_2 = QPushButton('Tester', self)
        self.btn_3 = QPushButton('Outsource', self)
        self.btn_4 = QPushButton('Early access release', self)
        self.btn_5 = QPushButton('Next week', self)
        self.btn_6 = QPushButton('ScoreBoard', self)
        self.btn_7 = QPushButton('Detailed Budget', self)
        self.btn_8 = QPushButton('Quit', self)

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)
        self.btn_5.clicked.connect(self.button5)
        self.btn_6.clicked.connect(self.button6)
        self.btn_7.clicked.connect(self.button7)
        self.btn_8.clicked.connect(self.button8)

        # add tabs
        self.tab1 = self.ui1()

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addWidget(self.btn_5)
        left_layout.addWidget(self.btn_6)
        left_layout.addWidget(self.btn_7)
        left_layout.addWidget(self.btn_8)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # -----------------
    # buttons

    def button1(self):
        self.game.addProgrammer()

    def button2(self):
        self.game.addTester()

    def button3(self):
        self.game.sousTraiter()

    def button4(self):
        self.game.sortieAnticiper()

    def button5(self):
        self.game.nextWeek()

    def button6(self):
        # TODO créer principe de scoreboard
        pass

    def button7(self):
        self.game.getBudget()

    def button8(self):
        sys.exit()

    # -----------------
    # pages

    def ui1(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel(str(self.game.budget)))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
