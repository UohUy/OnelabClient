# coding = utf-8

import sys, onelab, action
from qt import options, main
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog



if  __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    optionsWindow = QDialog()
    func = action.Action()
    c = onelab.client(__file__)

    work = action.Instantiate(main, options, func, mainWindow, optionsWindow)

    mainWindow.show()
    optionsWindow.exec()
    sys.exit(app.exec())

