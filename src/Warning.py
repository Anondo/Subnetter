from PyQt4 import QtGui
from ui.UiWarning import Ui_Warning

class Warning(QtGui.QDialog):
    def __init__(self , error_msg = ""):
        super(Warning , self).__init__()
        self.ui = Ui_Warning()
        self.ui.setupUi(self)
        self.error_msg = error_msg

        self.ui.errorLabel.setText(self.error_msg)

        self.ui.okBtn.clicked.connect(self.windowClose)

        self.show()

    def windowClose(self):
        self.close()
