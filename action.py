# coding = utf-8

import webbrowser
from PyQt5.QtWidgets import QFileDialog

class Action():
    def file_open(self):
        self.file_open = QFileDialog.getOpenFileName()

    def file_save(self):
        self.file_new = QFileDialog.getSaveFileName()

    def help_online_document(self):
        self.help_online_document = webbrowser.open(url='http://onelab.info/wiki/ONELAB', new=0, autoraise=True)

class Instantiate(object):
    def __init__(self, main, options, func, mainWindow, optionsWindow):
        self.main = main.Ui_MainWindow()
        self.options = options.Ui_QDialogOptions()
        self.main.setupUi(mainWindow)
        self.main.retranslateUi(mainWindow)
        self.options.setupUi(optionsWindow)
        self.options.retranslateUi(optionsWindow)
        self.main.actionOnline_Document.triggered.connect(func.help_online_document)
        self.main.actionOpen.triggered.connect(func.file_open)
