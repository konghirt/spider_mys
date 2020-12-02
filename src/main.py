import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from views.MyWin import MainWin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec_())