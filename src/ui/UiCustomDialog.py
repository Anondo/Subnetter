# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiCustomDialog.ui'
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

class Ui_hostDialog(object):
    def setupUi(self, hostDialog):
        hostDialog.setObjectName(_fromUtf8("hostDialog"))
        hostDialog.resize(347, 226)
        hostDialog.setMinimumSize(QtCore.QSize(347, 226))
        hostDialog.setMaximumSize(QtCore.QSize(347, 226))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        hostDialog.setFont(font)
        hostDialog.setStyleSheet(_fromUtf8("background-image: url(\'background.png\');\n"
"color: Aquamarine;"))
        self.infoLabel = QtGui.QLabel(hostDialog)
        self.infoLabel.setGeometry(QtCore.QRect(30, -60, 347, 226))
        self.infoLabel.setMinimumSize(QtCore.QSize(347, 226))
        self.infoLabel.setMaximumSize(QtCore.QSize(347, 226))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(12)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.netEdit = QtGui.QTextEdit(hostDialog)
        self.netEdit.setGeometry(QtCore.QRect(40, 70, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.netEdit.setFont(font)
        self.netEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.netEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.netEdit.setObjectName(_fromUtf8("netEdit"))
        self.setBtn = QtGui.QPushButton(hostDialog)
        self.setBtn.setGeometry(QtCore.QRect(60, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        self.setBtn.setFont(font)
        self.setBtn.setStyleSheet(_fromUtf8("background-image: url();\n"
"background-color: Aquamarine;\n"
"color: Black;"))
        self.setBtn.setObjectName(_fromUtf8("setBtn"))
        self.clrBtn = QtGui.QPushButton(hostDialog)
        self.clrBtn.setGeometry(QtCore.QRect(170, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        self.clrBtn.setFont(font)
        self.clrBtn.setStyleSheet(_fromUtf8("background-image: url();\n"
"background-color: Aquamarine;\n"
"color: Black;"))
        self.clrBtn.setObjectName(_fromUtf8("clrBtn"))

        self.retranslateUi(hostDialog)
        QtCore.QMetaObject.connectSlotsByName(hostDialog)

    def retranslateUi(self, hostDialog):
        hostDialog.setWindowTitle(_translate("hostDialog", "Hosts Required", None))
        self.infoLabel.setText(_translate("hostDialog", "Enter Hosts Required(separated by space):", None))
        self.setBtn.setText(_translate("hostDialog", "Set", None))
        self.clrBtn.setText(_translate("hostDialog", "Clear", None))
