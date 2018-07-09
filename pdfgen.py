#https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images/27327984#27327984
#exiftool -XMP-dc:Creator="ane Doe" -XMP-dc:Publisher="Research-publishing.netasdadadasdasasdadasda" techno.jpg.pdf
from PIL import Image
import os
import sys

filename = sys.argv[1]
im = Image.open(filename)
if im.mode == "RGBA": im = im.convert("RGB")
new_filename = "%s.pdf" % (sys.argv[1])
if not os.path.exists(new_filename):
	try:
		im.save(new_filename,"PDF",resolution=100.0,creator='asd')
	except Exception as e:
		print e
