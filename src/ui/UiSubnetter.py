# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiSubnetter.ui'
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

class Ui_Subnetter(object):
    def setupUi(self, Subnetter):
        Subnetter.setObjectName(_fromUtf8("Subnetter"))
        Subnetter.resize(800, 600)
        Subnetter.setAutoFillBackground(False)
        Subnetter.setStyleSheet(_fromUtf8("\n"
"QMessageBox{\n"
"    background: url();\n"
"    background-color: red;\n"
"};\n"
"background: url(\'background.png\');"))
        self.centralwidget = QtGui.QWidget(Subnetter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.octate1 = QtGui.QTextEdit(self.centralwidget)
        self.octate1.setGeometry(QtCore.QRect(110, 50, 71, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.octate1.setFont(font)
        self.octate1.setStyleSheet(_fromUtf8("color: Aquamarine;\n"
"background-color: Black;"))
        self.octate1.setMidLineWidth(0)
        self.octate1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.octate1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.octate1.setObjectName(_fromUtf8("octate1"))
        self.ipLabel = QtGui.QLabel(self.centralwidget)
        self.ipLabel.setGeometry(QtCore.QRect(60, 50, 41, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Niagara Engraved"))
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.ipLabel.setFont(font)
        self.ipLabel.setStyleSheet(_fromUtf8("color: Aquamarine;"))
        self.ipLabel.setObjectName(_fromUtf8("ipLabel"))
        self.octate4 = QtGui.QTextEdit(self.centralwidget)
        self.octate4.setGeometry(QtCore.QRect(410, 50, 71, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.octate4.setFont(font)
        self.octate4.setStyleSheet(_fromUtf8("color: Aquamarine;\n"
"background-color: Black;"))
        self.octate4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.octate4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.octate4.setObjectName(_fromUtf8("octate4"))
        self.octate3 = QtGui.QTextEdit(self.centralwidget)
        self.octate3.setGeometry(QtCore.QRect(310, 50, 71, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.octate3.setFont(font)
        self.octate3.setStyleSheet(_fromUtf8("color: Aquamarine;\n"
"background-color: Black;"))
        self.octate3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.octate3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.octate3.setObjectName(_fromUtf8("octate3"))
        self.octate2 = QtGui.QTextEdit(self.centralwidget)
        self.octate2.setGeometry(QtCore.QRect(210, 50, 71, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.octate2.setFont(font)
        self.octate2.setStyleSheet(_fromUtf8("color: Aquamarine;\n"
"background-color: Black;"))
        self.octate2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.octate2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.octate2.setObjectName(_fromUtf8("octate2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 21, 81))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-image: url(\"\");\n"
"color: Aquamarine;\n"
"\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 21, 81))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background-image: url(\"\");\n"
"color: Aquamarine;\n"
"\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 30, 21, 81))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background-image: url(\"\");\n"
"color: Aquamarine;\n"
"\n"
""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 40, 51, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("background-image: url(\"\");\n"
"color: Aquamarine;\n"
"\n"
""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cidr = QtGui.QTextEdit(self.centralwidget)
        self.cidr.setGeometry(QtCore.QRect(540, 50, 71, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cidr.setFont(font)
        self.cidr.setStyleSheet(_fromUtf8("color: Aquamarine;\n"
"background-color: Black;"))
        self.cidr.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cidr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cidr.setObjectName(_fromUtf8("cidr"))
        self.cname = QtGui.QTextEdit(self.centralwidget)
        self.cname.setGeometry(QtCore.QRect(390, 150, 41, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.cname.setFont(font)
        self.cname.setStyleSheet(_fromUtf8("color: Aquamarine;\n"
"background-color: Black;"))
        self.cname.setMidLineWidth(0)
        self.cname.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cname.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cname.setReadOnly(True)
        self.cname.setObjectName(_fromUtf8("cname"))
        self.classLabel = QtGui.QLabel(self.centralwidget)
        self.classLabel.setGeometry(QtCore.QRect(260, 150, 111, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Niagara Engraved"))
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.classLabel.setFont(font)
        self.classLabel.setStyleSheet(_fromUtf8("color: Aquamarine;"))
        self.classLabel.setObjectName(_fromUtf8("classLabel"))
        self.hostButton = QtGui.QPushButton(self.centralwidget)
        self.hostButton.setGeometry(QtCore.QRect(660, 130, 150, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(18)
        self.hostButton.setFont(font)
        self.hostButton.setStyleSheet(_fromUtf8("background-image: url();\n"
"border-radius:50px;\n"
"border-width:1px;\n"
" border-radius:70px;\n"
" max-width:150px;\n"
" max-height:150px;\n"
" min-width:150px;\n"
" min-height:150px;\n"
"color: Aquamarine;\n"
""))
        self.hostButton.setObjectName(_fromUtf8("hostButton"))
        self.subnetTable = QtGui.QTableWidget(self.centralwidget)
        self.subnetTable.setGeometry(QtCore.QRect(30, 290, 751, 261))
        self.subnetTable.setMinimumSize(QtCore.QSize(751, 261))
        self.subnetTable.setMaximumSize(QtCore.QSize(751, 261))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subnetTable.setFont(font)
        self.subnetTable.setStyleSheet(_fromUtf8("background-image: url();\n"
"background-color: transparent;\n"
"color: Aquamarine;\n"
"border: 0px;"))
        self.subnetTable.setObjectName(_fromUtf8("subnetTable"))
        self.subnetTable.setColumnCount(0)
        self.subnetTable.setRowCount(0)
        self.goBtn = QtGui.QPushButton(self.centralwidget)
        self.goBtn.setGeometry(QtCore.QRect(640, 42, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.goBtn.setFont(font)
        self.goBtn.setStyleSheet(_fromUtf8("background-image: url();\n"
"border: 0px;\n"
"color: Aquamarine;"))
        self.goBtn.setObjectName(_fromUtf8("goBtn"))
        Subnetter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Subnetter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Subnetter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Subnetter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Subnetter.setStatusBar(self.statusbar)

        self.retranslateUi(Subnetter)
        QtCore.QMetaObject.connectSlotsByName(Subnetter)

    def retranslateUi(self, Subnetter):
        Subnetter.setWindowTitle(_translate("Subnetter", "MainWindow", None))
        self.octate1.setHtml(_translate("Subnetter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bauhaus 93\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">172</p></body></html>", None))
        self.ipLabel.setText(_translate("Subnetter", "IP:", None))
        self.octate4.setHtml(_translate("Subnetter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bauhaus 93\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.octate3.setHtml(_translate("Subnetter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bauhaus 93\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.octate2.setHtml(_translate("Subnetter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bauhaus 93\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16</p></body></html>", None))
        self.label.setText(_translate("Subnetter", ".", None))
        self.label_2.setText(_translate("Subnetter", ".", None))
        self.label_3.setText(_translate("Subnetter", ".", None))
        self.label_4.setText(_translate("Subnetter", "/", None))
        self.cidr.setHtml(_translate("Subnetter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bauhaus 93\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22</p></body></html>", None))
        self.cname.setHtml(_translate("Subnetter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bauhaus 93\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.classLabel.setText(_translate("Subnetter", "CLASS:", None))
        self.hostButton.setText(_translate("Subnetter", "Set Hosts", None))
        self.goBtn.setText(_translate("Subnetter", "GO!", None))

