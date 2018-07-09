# needs fpdf
from fpdf import FPDF
import sys
import os
from PIL import Image
def genpdf(fname,fdir='.'):
	pdf = FPDF('P','pt',(400,568))
	flist = ['scan.jpg']
	for f in flist:
		im = Image.open(f)
		print im.size
		print f
		pdf.add_page()
		pdf.set_font('Courier','B')
		pdf.set_font_size(14)
		pdf.set_text_color(0,255,0)
		pdf.text(10,10,'... pwned by truerandom ...')
		pdf.image(f,0,0)
	pdf.output(fname, "F")
try: fname = sys.argv[1]
except: fname = 'output.pdf'
genpdf(fname)
