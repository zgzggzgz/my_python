import wx,os,cStringIO

filelist=[]
filenames=os.listdir(os.getcwd())
for fn in filenames:
	filelist.append(fn)

class xinxinframe(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Pan Yixin',size=(1200,900))
		panel=wx.Panel(self,-1)
		#self.app=app
		
		str="xinxin"
		text=wx.StaticText(panel,-1,str,(540,800))
		font=wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
		text.SetFont(font)
		
		self.button=wx.Button(panel,-1,"start",pos=(540,700))
		self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
		self.button.SetDefault()

		self.button2=wx.Button(panel,-1,"stop",pos=(700,700))
		self.Bind(wx.EVT_BUTTON,self.OnClick2,self.button2)
		self.button2.SetDefault()
		
		listbox=wx.ListBox(panel,-1,(20,20),(200,800),filelist,wx.LB_SINGLE)
		#listbox.SetSelection(3)
		listbox.Bind(wx.EVT_LISTBOX_DCLICK,self.OnClick1)
		curdir=os.getcwd()
		os.chdir(curdir)
		#self.LoadDir(curdir)
		
		panel2=wx.Panel(panel,-1,style=wx.BORDER_DOUBLE,size=(800,600),pos=(300,50))		
		myImage=wx.StaticBitmap(panel2, -1,  pos=(30,50), size=(292,250))
		bmp=wx.Bitmap("1.png", wx.BITMAP_TYPE_PNG)
		myImage.SetBitmap(bmp)
		
	def OnClick(self,event):
		self.button.SetLabel("started")
	
	def OnClick1(self,event):
		pass
		
	def OnClick2(self,event):
		self.button.SetLabel("start")
		
if __name__=='__main__':
	app=wx.App()
	frame=xinxinframe()
	frame.Show()
	app.MainLoop()