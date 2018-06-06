from Subnets import Subnets

class Vlsm(object):
    def __init__(self , ip , cidr , hosts):
        self.ip = ip
        self.cidr = cidr
        self.hosts = hosts
        self.ip_octates = map(int , self.ip.split("."))
        self.broadcastIp = []
        self.subnets = []
        self.class_name = ""
        self.previous_host_num = 0
        self.working_octate = 3
        self.setClass()

    def subnet(self):
        map(self.vlsm , self.hosts)

    def setClass(self):
        foct = int(self.ip.split(".")[0])
        if(foct in range(128)):
            self.class_name = "A"
        elif(foct in range(128 , 192)):
            self.class_name = "B"
        else:
            self.class_name = "C"
    def getClass(self):
        return self.class_name

    def vlsm(self , host):
        hostbit = 0
        while(True):
            hostbit += 1
            if((2**hostbit)-2 >= host):
                break
        self.cidr = 32-hostbit
        self.change_octate(self.ip_octates , self.previous_host_num)
        self.ip = ".".join(map(str , self.ip_octates))
        self.previous_host_num = 2**hostbit
        self.setBroadcastIp()
        self.subnets.append(Subnets(self.ip , self.cidr , self.broadcastIp , self.getClass() , host))
    def change_octate(self , ip , host):
        ip[self.working_octate] += host
        if((ip[self.working_octate]) > 255):
            ip[self.working_octate] = 0
            self.working_octate -= 1
            new_host = (ip[self.working_octate]+host) / 255
            self.change_octate(ip , new_host)
        self.working_octate = 3
    def setBroadcastIp(self):
        self.broadcastIp = list(self.ip_octates)
        self.change_octate(self.broadcastIp , self.previous_host_num-1)
        if(self.broadcastIp[3] == 0):
            self.broadcastIpSetter()
        self.broadcastIp = ".".join(map(str , self.broadcastIp))
    def broadcastIpSetter(self):
        if(self.broadcastIp[self.working_octate] == 0):
            self.working_octate -= 1
            self.broadcastIpSetter()
            try:
                self.broadcastIp[self.working_octate] -= 1
                self.working_octate += 1
                self.broadcastIp[self.working_octate] = 255
            except IndexError:
                pass

    def getSubnetObjectByIp(self, ip):
        for subnet in self.subnets:
            if(subnet.getSubIp() == ip):
                return subnet
        return None
    def getSubs(self):
        return self.subnets


#ip = "128.16.0.0"
#cidr = 22
#hosts = (1051,850,501,212,112 , 2 ,2 ,2 ,2)
#subnetter = Vlsm(ip , cidr , hosts)
#subnetter.subnet()
