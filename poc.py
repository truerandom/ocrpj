import wx 
import os
from subprocess import check_output
from PIL import Image
from fpdf import FPDF
class MyForm(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="Filtros")
		self.panel = wx.Panel(self, wx.ID_ANY)
		self.setMenu()

	def setMenu(self):
		menuBar = wx.MenuBar()
		# menus
		fileMenu = wx.Menu()
		abrirMenuItem = fileMenu.Append(wx.NewId(), "Abrir","Open Image")
		self.Bind(wx.EVT_MENU, self.onAbrir, abrirMenuItem)
		exitMenuItem = fileMenu.Append(wx.NewId(), "Exit","Exit the application")
		self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
		# opciones de menu
		filtrosMenu = wx.Menu()
		# getTexto
		getTextMenuItem = filtrosMenu.Append(wx.NewId(), "Obtener texto","Open Image")
		self.Bind(wx.EVT_MENU, self.onGetText,getTextMenuItem)
		genPDFMenuItem = filtrosMenu.Append(wx.NewId(), "Generar PDF","Open Image")
		self.Bind(wx.EVT_MENU, self.onGenPDF,genPDFMenuItem)

		menuBar.Append(fileMenu, "&Archivos")
		menuBar.Append(filtrosMenu, "&Herramientas")
		self.SetMenuBar(menuBar)

	def onExit(self, event): self.Close()
	def onAbrir(self,event):
		wildcard = ""
		dialog = wx.FileDialog(None, "Choose a file", os.getcwd(),"", wildcard, wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.filename = dialog.GetPath()
			dialog.Destroy()
			fgs = wx.FlexGridSizer(cols=2, hgap=10, vgap=10)
			img1 = wx.Image(self.filename, wx.BITMAP_TYPE_ANY)
			sb1 = wx.StaticBitmap(self.panel, -1, wx.BitmapFromImage(img1))
			fgs.Add(sb1)
			self.panel.SetSizerAndFit(fgs)
			self.Fit()

	def onGetText(self,event):
		out = check_output(["tesseract",self.filename,"-l","spa","stdout"])
		pepe = TextEntryDialog(None,'Modificar texto', '')
		pepe.setText(out)
		val = pepe.ShowModal()
		pepe.Show()
		if val == wx.ID_OK:
			self.msg = pepe.getText()
			print self.msg
			pepe.Destroy()
		else:
			pepe.Destroy()

	def onGenPDF(self,event):
		im = Image.open(self.filename)
		h,w = im.size
		pdf = FPDF('P','pt',(h,w))
		pdf.add_page()
		pdf.set_font('Courier','B')
		pdf.set_font_size(10)
		pdf.set_text_color(0,255,0)
		effective_page_width = pdf.w-pdf.l_margin
		pdf.multi_cell(effective_page_width,6,self.msg.encode('latin-1','ignore'))
		pdf.image(self.filename,0,0)
		pdf.output("report.pdf", "F")
		print 'done check files'

class TextEntryDialog(wx.Dialog):
	def __init__(self, parent, title, caption):
		style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER 
		super(TextEntryDialog, self).__init__(parent, -1, title, style=style)
		text = wx.StaticText(self, -1, caption)
		input = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
		input.SetInitialSize((600, 300))
		buttons = self.CreateButtonSizer(wx.OK|wx.CANCEL)
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(text, 0, wx.ALL, 5)
		sizer.Add(input, 1, wx.EXPAND|wx.ALL, 5)
		sizer.Add(buttons, 0, wx.EXPAND|wx.ALL, 5)
		self.SetSizerAndFit(sizer)
		self.input = input

	def setText(self, value):
		self.input.SetValue(value)

	def getText(self):
		return self.input.GetValue()
if __name__ == "__main__":
	app = wx.App(False)
	frame = MyForm().Show()
	app.MainLoop()
