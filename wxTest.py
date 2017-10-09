#!/usr/bin/env Python
 #coding=utf-8

#filename : PictureBrowser.py
 #date     : 2012-10-11


import wx
import os
import sys
import string

#����H����û�еĻ��������ʼ���������޸ļ��صĳ�ʼ·��
class PBDirFrame(wx.Frame):
     def __init__(self, app):
        wx.Frame.__init__(self, None, -1, "ѡ���ļ���", size=(250,500))

        self.app = app

        #��������
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'Courier New')
        self.SetFont(font)
         
         #�ļ���listbox
        self.list = wx.ListBox(self, -1, (0,0), (200,600), '', wx.LB_SINGLE)
        self.list.Bind(wx.EVT_LISTBOX_DCLICK, self.OnDClick)
         
         #���ص�ǰ�ļ���
        #curdir = os.getcwd()#�������޸ĳ�ʼ·��������ǵ�ǰ����·��
        curdir = 'H:\\'
        os.chdir(curdir)
        self.LoadDir(curdir)
         
         #���¼�
        self.Bind(wx.EVT_CLOSE, self.OnClose)


         
         #��ʾ����
        self.Show()
     
     def OnClose(self, event):
        self.Destroy()
        self.app.Close()
     
     #listbox˫���¼�
     def OnDClick(self, event):
        if self.list.GetSelection()==0:#�ж��Ƿ�ѡ���˷�����һ���ļ���
             path = os.getcwd()
             pathinfo = os.path.split(path)
             dir = pathinfo[0]
        else:#�����Ҫ�������һ���ļ���
            dir = self.list.GetStringSelection()
         
        if os.path.isdir(dir):#�����ļ���
            self.LoadDir(dir)
        elif os.path.splitext(dir)[-1]=='.jpg':#��ʾͼƬ
            self.app.ShowImage(dir)

    #�����ļ��У�������붨���Լ���������ô�޸����������~
     def LoadDir(self, dir):
         #����Ŀ¼�򲻽��в���
        if not os.path.isdir(dir):
             return
         
        self.list.Clear()#���
        self.list.Append('...')#��ӷ�����һ���ļ��б�־

        dirs = []
        jpgs = []
        nnjpgs = []
        for _dir in os.listdir(dir):
            if os.path.isdir(dir+os.path.sep+_dir):
                dirs.append(_dir)
            else:
                info = os.path.splitext(_dir)
                if info[-1]=='.jpg':
                    if info[0].isdigit():
                        jpgs.append(string.atoi(info[0]))#ת��Ϊ����
                    else:
                        nnjpgs.append(_dir)
        jpgs.sort()
        for _jpgs in jpgs:
            self.list.Append(str(_jpgs)+'.jpg')
        for _nnjpgs in nnjpgs:
            self.list.Append(_nnjpgs)
        for _dirs in dirs:
            self.list.Append(_dirs)

        os.chdir(dir)#���ù���·��

    #�����һ��Ҫ��ʾ��ͼƬ
     def GetNextImage(self):
        index = self.list.GetSelection()
        i = index
        while i+1<self.list.GetCount():
            i += 1
            if os.path.splitext(self.list.GetString(i))[-1]=='.jpg':
                break
        if i<self.list.GetCount():
            index = i
        self.list.SetSelection(index)
        return self.list.GetStringSelection()

    #�����һ��ͼƬ
     def GetPreImage(self):
        index = self.list.GetSelection()
        i = index
        while i-1>0:
            i -= 1
            if os.path.splitext(self.list.GetString(i))[-1]=='.jpg':
                break
        if i>0:
            index = i
         
        self.list.SetSelection(index)
        return self.list.GetStringSelection()


class PBPicFrame(wx.Frame):

     max_width = 400
     max_height = 600

     def __init__(self, app):
        wx.Frame.__init__(self, None, -1, "��ʾͼƬ", size=(400,400))#, style=wx.SIMPLE_BORDER)

        #�Ƿ�Ҫ�ƶ�ͼƬ�ı�־
        self.bmoved = False
         
        self.app = app

        #staticbitmap
        self.bmp = wx.StaticBitmap(self, 0, wx.NullBitmap, (0,0), (400,400))


        self.Bind(wx.EVT_MOUSEWHEEL, self.OnChangeImage)
        self.bmp.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.bmp.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.bmp.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
         
        self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
        self.Hide()


     def ShowImage(self, path):
         if os.path.splitext(path)[-1]!='.jpg':
             return
         self.bmppath = path
         image = wx.Image(path, wx.BITMAP_TYPE_JPEG)
         bmp = image.ConvertToBitmap()
         size = self.GetSize(bmp)
         bmp = image.Scale(size[0], size[1]).ConvertToBitmap()
         self.bmp.SetSize(size)
         self.bmp.SetBitmap(bmp)
         self.Show()

     def GetSize(self, bmp):
         width = bmp.GetWidth()
         height = bmp.GetHeight()
         if width>self.max_width:
             height = height*self.max_width/width
             width = self.max_width
         if height>self.max_height:
             width = width*self.max_height/height
             height = self.max_height
         size = width, height
         return size
        

     def OnChangeImage(self, event):
         rotation = event.GetWheelRotation()
         if rotation<0:
             self.app.ShowNextImage()
         else:
             self.app.ShowPreImage()
     
     def OnLeftDown(self, event):
         self.pos = event.GetX(), event.GetY()
         self.bmoved = True

     def OnLeftUp(self, event):
         self.bmoved = False

     def OnMotion(self, event):
         if not self.bmoved:
             return
         pos = event.GetX(), event.GetY()
         dx = pos[0]-self.pos[0]
         dy = pos[1]-self.pos[1]
         pos = self.bmp.GetPosition()
         pos = pos[0]+dx, pos[1]+dy
         self.bmp.SetPosition(pos)

     def OnKeyDown(self, event):
         keycode = event.GetKeyCode()
         if keycode == 49:#����1�Ŵ�
            self.SizeUp()
         elif keycode == 50:#����2��С
            self.SizeDown()
         event.Skip()#���ò�ƺ���Ҫ��Ҫͬʱ����app�ϵĿ�ݼ�

     def SizeUp(self):
         self.max_width += 50
         self.max_height += 75
         self.ShowImage(self.bmppath)
     def SizeDown(self):
         self.max_width -= 50
         self.max_height -= 75
         self.ShowImage(self.bmppath)

class PBApp(wx.App):
     
     #redirect=False����Ϣ�����dos����
     def __init__(self, redirect=False):
        wx.App.__init__(self, redirect)
     
     def OnInit(self):
         
         #��ʾ�ļ����б����
        self.dirframe = PBDirFrame(self)
         
         #��ʾͼƬ����
        self.picframe = PBPicFrame(self)
         
         #���¼�
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        return True

     def ShowImage(self, path):
         #print 'showing app img', path
         self.picframe.ShowImage(path)
         self.picframe.SetFocus()
     
     def ShowNextImage(self):
         path = self.dirframe.GetNextImage()
         self.ShowImage(path)

     def ShowPreImage(self):
         path = self.dirframe.GetPreImage()
         self.ShowImage(path)

     def OnKeyDown(self, event):
         keycode = event.GetKeyCode()
         #print keycode
         if keycode == 27:# ESC��
            #�л�ͼƬ�������ʾ������
            if self.picframe.IsShown():
                 self.picframe.Hide()
            else:
                 self.picframe.Show()
     
     def Close(self):
         self.picframe.Close()
     
     
def main():
     app = PBApp()
     app.MainLoop()

if __name__=='__main__':
     main()
