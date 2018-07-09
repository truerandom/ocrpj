# needs fpdf
from fpdf import FPDF
import sys
import os
from PIL import Image
def genpdf(ifile,fname,fdir='.'):
	im = Image.open('scan.jpg')
	h,w = im.size
	pdf = FPDF('P','pt',(h,w))
	pdf.add_page()
	pdf.set_font('Courier','B')
	pdf.set_font_size(14)
	pdf.set_text_color(0,255,0)
	pdf.text(10,10,'... pwned by truerandom ...')
	pdf.image(ifile,0,0)
	pdf.output(fname, "F")

try: fname = sys.argv[1]
except Exception as e:
	print 'Specify a filename'
	exit(1)
genpdf(fname,'outputpdf.pdf')
