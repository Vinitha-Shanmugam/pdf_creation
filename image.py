from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

w, h = A4
c = canvas.Canvas("image.pdf", pagesize=A4)
# Place the logo in the upper left corner.
img = ImageReader(r"C:\Users\Vrdella\Pictures\Screenshots\Screenshot (187).png")
# Get the width and height of the image.
img_w, img_h = img.getSize()
# h - img_h is the height of the sheet minus the height
# of the image.
c.drawImage(img, 0, h - 300)
c.save()