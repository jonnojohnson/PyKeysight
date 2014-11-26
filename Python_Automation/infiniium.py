# -*- coding: utf-8 -*-
"""
Created on Sat Apr 06 15:58:10 2013

@author: marnj
"""
#from visa import instrument
#scope = instrument("TCPIP0::130.30.240.155::inst0::INSTR")
import visa
import types
        
class Command(visa.Instrument):
    def __init__(self, scpi_cmd, synopsis):
        self.scpi_cmd = scpi_cmd
        self.synopsis = synopsis

def cmd(self, scope, scpi_cmd, *args):
    self.scope = scope
    self.scpi_cmd = scpi_cmd
    self.scope.write(self.scpi_cmd+' '+' '.join(str(arg) for arg in args))

def query(self, scpi_cmd, *args):
    self.scpi_cmd = scpi_cmd
    return self.ask(self.scpi_cmd+'? '+' '.join(str(arg) for arg in args))

class CommonCommands():
    def __init__(self):
        self.cls = Command("*cls", "Synopsis")
        self.cls.cmd = types.MethodType(cmd, self.cls)
        self.ese = Command("*ese", "Synopsis")
        self.ese.cmd = types.MethodType(cmd, self.ese)
        self.esr = Command("*esr", "Synopsis")
        self.esr.query = types.MethodType(query, self.esr)
        self.idn = Command("*idn", "This is the idn docstring")
        self.idn.query = types.MethodType(query, self.idn)
        self.opc = Command("*opc", "Synopsis")
        self.opc.cmd = types.MethodType(cmd, self.opc)
        self.opt = Command("*opt", "Synopsis")
        self.opt.query = types.MethodType(query, self.opt)
        self.psc = Command("*psc", "Synopsis")
        self.psc.cmd = types.MethodType(cmd, self.psc)
        self.rcl = Command("*rcl", "Synopsis")
        self.rcl.cmd = types.MethodType(cmd, self.rcl)
        self.rst = Command("*rst", "Synopsis")
        self.rst.cmd = types.MethodType(cmd, self.rst)
        self.sav = Command("*sav", "Synopsis")
        self.sav.cmd = types.MethodType(cmd, self.sav)
        self.sre = Command("*sre", "Synopsis")
        self.sre.cmd = types.MethodType(cmd, self.sre)
        self.stb = Command("*stb", "Synopsis")
        self.stb.query = types.MethodType(query, self.stb)
        self.trg = Command("*trg", "Synopsis")
        self.trg.cmd = types.MethodType(cmd, self.trg)
        self.tst = Command("*tst", "Synopsis")
        self.tst.query = types.MethodType(query, self.tst)
        self.wai = Command("*wai", "Synopsis")
        self.wai.cmd = types.MethodType(cmd, self.wai)
        
class SubsystemCommands():
    def __init__(self):
        self.acquire = Command("acq", "Synopsis")
        self.acquire.average = Command("acq:aver", "Synopsis")
        self.acquire.average.cmd = types.MethodType(cmd, self.acquire.average)
        self.acquire.average.query = types.MethodType(query, self.acquire.average)
        self.acquire.average.count = Command("acq:aver:coun", "Synopsis")
        self.acquire.average.count.cmd = types.MethodType(cmd, self.acquire.average.count)
        self.acquire.average.count.query = types.MethodType(query, self.acquire.average.count)
        self.acquire.bandwidth = Command("acq:band", "Synopsis")
        self.acquire.bandwidth.cmd = types.MethodType(cmd, self.acquire.bandwidth)
        self.acquire.bandwidth.query = types.MethodType(query, self.acquire.bandwidth)
        self.ader = Command("ader", "Synopsis")
        self.ader.query = types.MethodType(query, self.ader)
        self.bus = Command("bus", "Synopsis")
        self.bus.b = Command("bus:b", "Synopsis")
        self.bus.b.type = Command("bus:b:type", "Synopsis")
        self.bus.b.type.cmd = types.MethodType(cmd, self.bus.b.type)
        self.bus.b.type.query = types.MethodType(query, self.bus.b.type)
     
class Infiniium(visa.Instrument):
    def __init__(self, resource_name):
        visa.Instrument.__init__(self, resource_name)
        self.common_commands = CommonCommands()
        self.subsystem_commands = SubsystemCommands()
        
