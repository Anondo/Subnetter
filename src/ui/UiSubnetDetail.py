# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiSubnetDetail.ui'
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

class Ui_SubnetDetail(object):
    def setupUi(self, SubnetDetail):
        SubnetDetail.setObjectName(_fromUtf8("SubnetDetail"))
        SubnetDetail.resize(476, 534)
        SubnetDetail.setStyleSheet(_fromUtf8("background-image: url(\'background.png\');"))
        self.naLabel = QtGui.QLabel(SubnetDetail)
        self.naLabel.setGeometry(QtCore.QRect(20, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.naLabel.setFont(font)
        self.naLabel.setStyleSheet(_fromUtf8("background-image: url();\n"
"color: Aquamarine;"))
        self.naLabel.setObjectName(_fromUtf8("naLabel"))
        self.baLabel = QtGui.QLabel(SubnetDetail)
        self.baLabel.setGeometry(QtCore.QRect(20, 60, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.baLabel.setFont(font)
        self.baLabel.setStyleSheet(_fromUtf8("background-image: url();\n"
"color: Aquamarine;"))
        self.baLabel.setObjectName(_fromUtf8("baLabel"))
        self.smLabel = QtGui.QLabel(SubnetDetail)
        self.smLabel.setGeometry(QtCore.QRect(20, 100, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.smLabel.setFont(font)
        self.smLabel.setStyleSheet(_fromUtf8("background-image: url();\n"
"color: Aquamarine;"))
        self.smLabel.setObjectName(_fromUtf8("smLabel"))
        self.hLabe = QtGui.QLabel(SubnetDetail)
        self.hLabe.setGeometry(QtCore.QRect(20, 140, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.hLabe.setFont(font)
        self.hLabe.setStyleSheet(_fromUtf8("background-image: url();\n"
"color: Aquamarine;"))
        self.hLabe.setObjectName(_fromUtf8("hLabe"))
        self.naEdit = QtGui.QTextEdit(SubnetDetail)
        self.naEdit.setGeometry(QtCore.QRect(250, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.naEdit.setFont(font)
        self.naEdit.setStyleSheet(_fromUtf8("color: Aquamarine;"))
        self.naEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.naEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.naEdit.setReadOnly(True)
        self.naEdit.setObjectName(_fromUtf8("naEdit"))
        self.baEdit = QtGui.QTextEdit(SubnetDetail)
        self.baEdit.setGeometry(QtCore.QRect(250, 60, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.baEdit.setFont(font)
        self.baEdit.setStyleSheet(_fromUtf8("color: Aquamarine;"))
        self.baEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.baEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.baEdit.setReadOnly(True)
        self.baEdit.setObjectName(_fromUtf8("baEdit"))
        self.smEdit = QtGui.QTextEdit(SubnetDetail)
        self.smEdit.setGeometry(QtCore.QRect(250, 100, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.smEdit.setFont(font)
        self.smEdit.setStyleSheet(_fromUtf8("color: Aquamarine;"))
        self.smEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.smEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.smEdit.setReadOnly(True)
        self.smEdit.setObjectName(_fromUtf8("smEdit"))
        self.hEdit = QtGui.QTextEdit(SubnetDetail)
        self.hEdit.setGeometry(QtCore.QRect(250, 140, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.hEdit.setFont(font)
        self.hEdit.setStyleSheet(_fromUtf8("color: Aquamarine;"))
        self.hEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hEdit.setReadOnly(True)
        self.hEdit.setObjectName(_fromUtf8("hEdit"))
        self.avIpLabel = QtGui.QLabel(SubnetDetail)
        self.avIpLabel.setGeometry(QtCore.QRect(20, 190, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(20)
        self.avIpLabel.setFont(font)
        self.avIpLabel.setStyleSheet(_fromUtf8("background-image: url();\n"
"color: Aquamarine;"))
        self.avIpLabel.setObjectName(_fromUtf8("avIpLabel"))
        self.ipTable = QtGui.QTableWidget(SubnetDetail)
        self.ipTable.setGeometry(QtCore.QRect(15, 230, 451, 301))
        self.ipTable.setMinimumSize(QtCore.QSize(451, 301))
        self.ipTable.setMaximumSize(QtCore.QSize(451, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.ipTable.setFont(font)
        self.ipTable.setStyleSheet(_fromUtf8("background-image: url();\n"
"background-color: transparent;\n"
"color: Aquamarine;"))
        self.ipTable.setObjectName(_fromUtf8("ipTable"))
        self.ipTable.setColumnCount(0)
        self.ipTable.setRowCount(0)

        self.retranslateUi(SubnetDetail)
        QtCore.QMetaObject.connectSlotsByName(SubnetDetail)

    def retranslateUi(self, SubnetDetail):
        SubnetDetail.setWindowTitle(_translate("SubnetDetail", "Dialog", None))
        self.naLabel.setText(_translate("SubnetDetail", "Network Address:", None))
        self.baLabel.setText(_translate("SubnetDetail", "Broadcast Address:", None))
        self.smLabel.setText(_translate("SubnetDetail", "Subnet Mask:", None))
        self.hLabe.setText(_translate("SubnetDetail", "Hosts:", None))
        self.naEdit.setHtml(_translate("SubnetDetail", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bauhaus 93\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>", None))
        self.avIpLabel.setText(_translate("SubnetDetail", "Available Ip:", None))

