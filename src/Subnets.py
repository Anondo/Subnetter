class Subnets(object):
    def __init__(self , subIp ,cidr, broadcastIp , class_name , hosts):
        self.subIp = subIp
        self.cidr = cidr
        self.broadcastIp = broadcastIp
        self.subnetmask = [0,0,0,0]
        self.addresses = []
        self.class_name = class_name
        self.hosts = hosts
        self.setAddresses()
        self.setMask()
    def setMask(self):
        index = 0
        power = 7
        for bit in range(1 , self.cidr+1):
            self.subnetmask[index]  += 2**power
            if(bit % 8 == 0):
                index += 1
                power = 7
            else:
                power-=1
        self.subnetmask = ".".join(map(str , self.subnetmask))
    def setAddresses(self):
        if(self.class_name == "A"):
            self.assignClassA()
        elif(self.class_name == "B"):
            self.assignClassB()
        elif(self.class_name == "C"):
            self.assignClassC()
    def assignClassA(self):
        ip = map(int , self.subIp.split("."))
        bip = map(int , self.broadcastIp.split("."))
        ip[3] +=  1
        while(ip != bip):
            if(ip[3] < 255):
                self.addresses.append(".".join(map(str , ip)))
                ip[3] += 1
            else:
                if(ip[2] < 255):
                    ip[2] += 1
                    ip[3] = 0
                    self.addresses.append(".".join(map(str , ip)))
                else:
                    ip[1] += 1
                    ip[2] = 0
                    ip[3] = 0
                    self.addresses.append(".".join(map(str , ip)))
    def assignClassB(self):
        ip = map(int , self.subIp.split("."))
        bip = map(int , self.broadcastIp.split("."))
        ip[3] +=  1
        while(ip != bip):
            if(ip[3] < 255):
                self.addresses.append(".".join(map(str , ip)))
                ip[3] += 1
            else:
                ip[2] += 1
                ip[3] = 0
                self.addresses.append(".".join(map(str , ip)))
    def assignClassC(self):
        ip = map(int , self.subIp.split("."))
        bip = map(int , self.broadcastIp.split("."))
        ip[3] +=  1
        while(ip != bip):
            if(ip[3] < 255):
                self.addresses.append(".".join(map(str , ip)))
                ip[3] += 1
    def getSubnetMask(self):
        return self.subnetmask
    def getSubIp(self):
        return self.subIp
    def getCidr(self):
        return self.cidr
    def getBroadcastIp(self):
        return self.broadcastIp
    def getAvailableIp(self):
        return self.addresses
    def getHosts(self):
        return self.hosts




    def getFullInfo(self):
        info = "Network Address = " + self.subIp+"/"+str(self.cidr) + "\n"
        #info += str(self.addresses) + "\n"
        info += self.subnetmask + "\n"
        info += "Broadcast Address = " + self.broadcastIp+"/"+str(self.cidr)
        return info
