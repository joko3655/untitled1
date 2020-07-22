#coding:utf-8
import wx
class Frame1(wx.Frame):
   def __init__(self,parent,title):
        wx.Frame.__init__(self, parent, title = title, pos = (100,200), size = (200,100))
        #容纳其他组件的容器
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, value = "Hello, World!", size = (200,100))
        self.Show(True)
if __name__ == '__main__':
    #创建一个应用程序对象，用于消息循环
    app = wx.App()
    #创建一个窗体
    frame = Frame1(None, "Example")
    app.MainLoop()
#Test Github
#Test 2 Github