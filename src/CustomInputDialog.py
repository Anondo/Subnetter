from PyQt4 import QtGui
from ui.UiCustomDialog import Ui_hostDialog

class CustomInputDialog(QtGui.QDialog):
    def __init__(self ,  parent = None):
        super(CustomInputDialog , self).__init__(parent)
        self.ui = Ui_hostDialog()
        self.ui.setupUi(self)
        self.setClicked = False
        self.setWindowIcon(QtGui.QIcon('logo.jpg'))

        self.hosts = None

        self.ui.netEdit.textChanged.connect(self.checkInput)

        self.ui.clrBtn.clicked.connect(self.clearScreen)
        self.ui.setBtn.clicked.connect(self.setHost)
    def getHost(parent=None):
        dialog = CustomInputDialog(parent)
        dialog.exec_()
        return dialog.hosts , dialog.setClicked
    def setHost(self):
        self.hosts = str(self.ui.netEdit.toPlainText()).split(" ")
        if(self.hosts):
            self.hosts = map(int , self.hosts)
            self.setClicked = True
            self.close()
    def clearScreen(self):
        self.ui.netEdit.setText("")
    def checkInput(self):
        txt = str(self.ui.netEdit.toPlainText())
        if(txt[len(txt)-1] ==  " " and txt[len(txt)-2] ==  " "):
            self.ui.netEdit.textCursor().deletePreviousChar()
        txt = "".join(txt.split(" "))
        if(not(txt.isdigit())):
            self.ui.netEdit.textCursor().deletePreviousChar()
