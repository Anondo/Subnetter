# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiWarning.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Warning(object):
    def setupUi(self, Warning):
        Warning.setObjectName(_fromUtf8("Warning"))
        Warning.resize(400, 211)
        Warning.setStyleSheet(_fromUtf8("background-image: url(\'background.png\');"))
        self.errorLabel = QtGui.QLabel(Warning)
        self.errorLabel.setGeometry(QtCore.QRect(60, 60, 271, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet(_fromUtf8("background-image: url();\n"
"color: Aquamarine;"))
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.okBtn = QtGui.QPushButton(Warning)
        self.okBtn.setGeometry(QtCore.QRect(290, 160, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        self.okBtn.setFont(font)
        self.okBtn.setStyleSheet(_fromUtf8("background-image: url();\n"
"background-color: Aquamarine;\n"
"color: Black;\n"
""))
        self.okBtn.setObjectName(_fromUtf8("okBtn"))

        self.retranslateUi(Warning)
        QtCore.QMetaObject.connectSlotsByName(Warning)

    def retranslateUi(self, Warning):
        Warning.setWindowTitle(_translate("Warning", "Warning!!!", None))
        self.errorLabel.setText(_translate("Warning", "TextLabel", None))
        self.okBtn.setText(_translate("Warning", "Got It", None))

