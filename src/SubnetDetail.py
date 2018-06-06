from PyQt4 import QtGui
from ui.UiSubnetDetail import Ui_SubnetDetail

class SubnetDetail(QtGui.QDialog):
    def __init__(self  ,  subnet = None , title = ""):
        super(SubnetDetail , self).__init__()
        self.ui = Ui_SubnetDetail()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logo.jpg'))

        self.setWindowTitle(title)

        self.subnet = subnet

        self.ui.naEdit.setText(self.subnet.getSubIp() + "/" + str(self.subnet.getCidr()))
        self.ui.baEdit.setText(self.subnet.getBroadcastIp() + "/" + str(self.subnet.getCidr()))
        self.ui.smEdit.setText(self.subnet.getSubnetMask())
        self.ui.hEdit.setText(str(self.subnet.getHosts()))

        self.ui.ipTable.setRowCount(1)
        self.ui.ipTable.setColumnCount(1)
        self.ui.ipTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.ipTable.setHorizontalHeaderLabels(['Subnet Address'])
        self.ui.ipTable.horizontalHeader().setStyleSheet("::section{Background-color:Aquamarine;border-radius:14px;font-size:15px;font-weight:bold;color:black;}")
        self.ui.ipTable.verticalHeader().setStyleSheet("::section{Background-color:Aquamarine;border-radius:14px;font-size:10px;font-weight:bold;color:black;}")
        self.ui.ipTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.setTable()

        self.show()
    def setTable(self):
        for ip in self.subnet.getAvailableIp():
            rowcount = self.ui.ipTable.rowCount()
            item = QtGui.QTableWidgetItem(ip + "/" + str(self.subnet.getCidr()))
            item.setTextAlignment(5)
            self.ui.ipTable.setItem(rowcount-1 , 0 , item)
            self.ui.ipTable.insertRow(rowcount)
