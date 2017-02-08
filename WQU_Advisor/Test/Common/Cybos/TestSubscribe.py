import sys
from PyQt5.QtWidgets import *
import win32com.client

class CpEvent:
    instance = None
    def OnReceived(self):
        print(CpEvent.instance.GetHeaderValue(18), ":", CpEvent.instance.GetHeaderValue(13))

app = QApplication(sys.argv)
inst = win32com.client.Dispatch("dscbo1.StockCur")
win32com.client.WithEvents(inst, CpEvent)
inst.SetInputValue(0, "A000660")
CpEvent.instance = inst
inst.Subscribe()
app.exec_()