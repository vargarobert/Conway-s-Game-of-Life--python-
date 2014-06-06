###########################################################################
## Copyright Robert-Gabor Varga
## http://robert-varga.com
##
## 210CT - Programming, Algorithms and Data Structures - Challenge 2
###########################################################################

import wx
from MainFrame import MainFrame



class GameOfLife(wx.App):
    def OnInit(self):
        self.m_frame = MainFrame(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

app = GameOfLife(0)
app.MainLoop()
