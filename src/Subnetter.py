from PyQt4 import QtGui
from ui.UiSubnetter import Ui_Subnetter
from CustomInputDialog import CustomInputDialog
from SubnetDetail import SubnetDetail
import Vlsm


class Subnetter(QtGui.QMainWindow):
    def __init__(self):
        super(Subnetter , self).__init__()
        self.ui = Ui_Subnetter()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logo.jpg'))

        self.subnetter = None
        self.netNum = 0
        self.hosts = []
        self.ready = False

        self.ui.octate1.setText("172")
        self.ui.octate2.setText("16")
        self.ui.octate3.setText("0")
        self.ui.octate4.setText("0")
        self.ui.cidr.setText("22")
        self.ui.cname.setText("B")

        self.ui.subnetTable.setRowCount(1)
        self.ui.subnetTable.setColumnCount(3)
        self.ui.subnetTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.subnetTable.setHorizontalHeaderLabels(['Subnet Address' , 'Subnet Mask' , "Broadcast Address"])
        self.ui.subnetTable.horizontalHeader().setStyleSheet("::section{Background-color:Aquamarine;border-radius:14px;font-size:15px;font-weight:bold;color:black;}")
        self.ui.subnetTable.verticalHeader().setStyleSheet("::section{Background-color:Aquamarine;border-radius:14px;font-size:10px;font-weight:bold;color:black;}")
        self.ui.subnetTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.subnetTable.cellDoubleClicked.connect(self.showSubnetDetail)

        self.ui.octate1.textChanged.connect(self.prepareIp)
        self.ui.octate2.textChanged.connect(self.prepareIp)
        self.ui.octate3.textChanged.connect(self.prepareIp)
        self.ui.octate4.textChanged.connect(self.prepareIp)
        self.ui.cidr.textChanged.connect(self.prepareIp)

        self.ui.hostButton.clicked.connect(self.setHosts)
        self.ui.goBtn.clicked.connect(self.startSubnet)

        self.setWindowTitle("Subnetter")

        self.show()

    def startSubnet(self):
        if(self.ready):
            self.subnetter.subnet()
            subnets = self.subnetter.getSubs()
            for subnet in subnets:
                rowcount = self.ui.subnetTable.rowCount()
                item = QtGui.QTableWidgetItem(subnet.getSubIp() + "/" + str(subnet.getCidr()))
                item.setTextAlignment(5)
                self.ui.subnetTable.setItem(rowcount-1 , 0 , item)
                item = QtGui.QTableWidgetItem(subnet.getSubnetMask())
                item.setTextAlignment(5)
                self.ui.subnetTable.setItem(rowcount-1 , 1 , item)
                item = QtGui.QTableWidgetItem(subnet.getBroadcastIp() + "/" + str(subnet.getCidr()))
                item.setTextAlignment(5)
                self.ui.subnetTable.setItem(rowcount-1 , 2 , item)
                self.ui.subnetTable.insertRow(rowcount)
        else:
            self.setHosts()
        self.ready = False

    def prepareIp(self):
        map(self.checkInput , [self.ui.octate1 , self.ui.octate2 ,self.ui.octate3 ,self.ui.octate4 , self.ui.cidr])
        ip =  self.ui.octate1.toPlainText() + "." + self.ui.octate2.toPlainText() + "." +self.ui.octate3.toPlainText() + "." +self.ui.octate4.toPlainText()
        cidr = self.ui.cidr.toPlainText()
        hosts = tuple(self.hosts)
        self.subnetter = Vlsm.Vlsm(ip , cidr , hosts)
        self.ui.cname.setText(self.subnetter.getClass())
    def setHosts(self):
        host = 0
        self.hosts , ok =  CustomInputDialog().getHost()
        if(ok):
            self.hosts.sort(reverse=True)
            self.hosts = tuple(self.hosts)
            self.ready = True
            self.prepareIp()
    def checkInput(self , textEdit):
        if(len(textEdit.toPlainText()) > 3):
            textEdit.textCursor().deletePreviousChar()
        if(len(textEdit.toPlainText()) < 1):
            textEdit.setText("1")
        if(not(str(textEdit.toPlainText()).isdigit())):
            textEdit.textCursor().deletePreviousChar()
    def showSubnetDetail(self):
        col = self.ui.subnetTable.currentColumn()
        row = self.ui.subnetTable.currentRow()
        if(col == 0):
            ip = str(self.ui.subnetTable.item(row , col).text()).split("/")[0]
            self.window = SubnetDetail(self.subnetter.getSubnetObjectByIp(ip) , ip + " Details")
