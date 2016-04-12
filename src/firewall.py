'''
Created on 2016年4月12日

@author: Yo
'''
from asyncio.protocols import Protocol
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
        self.RemoveService(service)

class Zone:
    def __init__(self,name="None",default="Allow"):
        self.default=default
        self.servicectl=Service_Ctl()
        self.name=name
        
class Zone_Ctl:
    def __init__(self):
        self.zonelist=["block","dmz","drop","external","home","internal","public","trusted","work"]
        self.default="public"