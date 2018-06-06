import  sys
from PyQt4 import QtGui
from src.Subnetter import Subnetter

app = QtGui.QApplication(sys.argv)
subnetter = Subnetter()
app.exec_()
