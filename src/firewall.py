'''
Created on 2016年4月12日

@author: Yo
'''

class Pp:
    def __init__(self):
        self.rule=[]
    
    def AddPpRule(self,port,protocol="tcp"):
        newrule=[]
        newrule.append(port)
        newrule.append(protocol)
        self.rule.append(newrule)
        
    def RemovePpRule(self,port,protocol):
        for L in self.rule:
            if L[0]==port and L[1]== protocol:
                self.rule.remove(L)

    
    def EditPpRule(self,port,protocol,nport,nprotocol):
        Pp.RemovePpRule(self,port, protocol)
        Pp.AddPpRule(self,nport, nprotocol)

class Service:
    def __init__(self,name="",pp=Pp()):
        self.name=name
        self.pp=Pp()
        
    def SetServiceName(self,name=""):
        self.name=name
        
    def SetServicePp(self,pp):
        self.pp=pp
    
class Service_Ctl:
    def _init_(self):
        self.list=[]
    
    def AddService(self,service=Service()):
        self.list.append(service)
    
    def RemoveService(self,service=Service()):
        self.list.remove(service)

class Zone:
    def __init__(self,name="None",default="Allow"):
        self.default=default
        self.servicectl=Service_Ctl()
        self.name=name
        
class Zone_Ctl:
    def __init__(self):
        self.zonelist=[]
        self.default="public"
        
        
if __name__=="__main__":
    print("-------")
    pp=Pp()
    pp.AddPpRule(20)
    pp.AddPpRule(80,"udp")
    print(pp.rule)
    pp.RemovePpRule(80,"tcp")
    print(pp.rule)
    pp.AddPpRule(80,"udp")
    pp.EditPpRule(80,"udp",80,"tcp")
    print(pp.rule)
    print("-------")
    servicelist=Service_Ctl()
    service=Service()
    service.SetServiceName("httpd")
    service.SetServicePp(pp)
    print(service.name)
    print(service.pp.rule)
    #servicelist.AddService(service)
    #print(Service_Ctl.list)
    print("-------")
    
    