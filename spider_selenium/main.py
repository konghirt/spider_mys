import sys
from PyQt5.QtWidgets import QApplication
from views.MyWin import MainWin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    sys.exit(app.exec_())