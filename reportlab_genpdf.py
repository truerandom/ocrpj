import sys
from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
packet = StringIO.StringIO()
# read your existing PDF
existing_pdf = PdfFileReader(file(sys.argv[1], "rb"))
output = PdfFileWriter()
# create a new PDF with Reportlab
print existing_pdf.getPage(0).mediaBox
can = canvas.Canvas(packet, pagesize=(existing_pdf.getPage(0).mediaBox[2],existing_pdf.getPage(0).mediaBox[3]))
can.drawString(0, 0, "Hello world")
can.save()
#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# add the "watermark" (which is the new pdf) on the existing page
#page = existing_pdf.getPage(0)
page = new_pdf.getPage(0)
page.mergePage(existing_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file(sys.argv[1]+'.pj', "wb")
output.write(outputStream)
outputStream.close()

