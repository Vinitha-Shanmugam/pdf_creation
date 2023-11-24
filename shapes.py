# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4, letter, landscape
# from reportlab.pdfgen import canvas
#
# # w, h = A4
# pdf = canvas.Canvas("shapes.pdf", pagesize=A4)
# width, height = A4
# pdf.setPageSize((width, height))
#
# #    pdf = canvas.Canvas(buffer)
# # pdf.translate(inch, inch)
# # red colour of lin
# width, h = A4
# pdf.setPageSize((width, height))
# xlist = [10, 60, 110, 160, 210]
# ylist = [h - 20, h - 40, h - 60, h - 80, h - 100]
# pdf.grid(xlist, ylist)
# pdf.drawString(30,h-35,"hello")
# # pdf.drawString(250, height - 120, "Customer Invoice")
# # # Draw a horizontal line at the top of the page
# # pdf.line(30, height - 130, 30 + 530, height - 130)
# #
# # # Set the fill color to blue
# # pdf.setFillColorRGB(0, 0, 1)
# #
# # # Draw the text in blue color
# # pdf.setFont("Helvetica", 9)
# # pdf.drawString(30, height - 165, "Vrihodha Organics Private Limited")
# # pdf.setFillColorRGB(0, 0, 0)
# # pdf.drawString(30, height - 180, "Ground Floor, 145, Arokiya Nagar, Nanjikottai Road")
# # pdf.drawString(30, height - 190, "Vilar, Thanjavur,Tamilnadu-613006")
# # pdf.drawString(30, height - 200, "Phone Number: 98438 42243")
# # pdf.drawString(30, height - 210, "GST Number: 33AAICV5446JIZI")
# # pdf.drawString(30, height - 220, "FSSAI Number: 12422020000430")
# # pdf.drawString(370, height - 165, 'To')
# # pdf.setFillColorRGB(0, 0, 1)
# # pdf.drawString(30, height - 260, "Your Orders")
# # pdf.setFillColorRGB(0, 0, 0)
# # pdf.setFont("Helvetica-Bold", 6)
# # pdf.drawString(30, height - 275, "S.No")
# # pdf.setFont("Helvetica", 6)
# # pdf.drawString(65, height - 275, "Item Name")
# # pdf.drawString(150, height - 275, "MRP")
# # pdf.drawString(190, height - 275, "Quantity")
# # pdf.drawString(190, height - 285, "pcs")
# # pdf.drawString(230, height - 275, "Base Rate")
# # pdf.drawString(285, height - 275, "Disc 1")
# # pdf.drawString(320, height - 275, "Disc 2")
# # pdf.drawString(350, height - 275, "Taxable amt")
# # pdf.drawString(400, height - 275, "CGST Amt")
# # pdf.drawString(400, height - 285, "CGST Tax%")
# # pdf.drawString(450, height - 275, "S/UTGST Amt")
# # pdf.drawString(450, height - 285, "S/UTGST Amt")
# # pdf.drawString(500, height - 275, "Net Amount")
# # pdf.setStrokeColorRGB(128, 0, 128)
# # pdf.line(30, height - 290, 30 + 530, height - 290)
# # table_data = [
# #         ["Name", "Age", "Country"],
# #         ["John Doe", "30", "USA"],
# #         ["Jane Smith", "25", "Canada"],
# #         ["Bob Johnson", "40", "UK"]
# #     ]
# #
# #
# # style = [
# #         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
# #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
# #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
# #         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Bottom padding for header row
# #         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background color for data rows
# #     ]
# #
# #     # Draw the table
# # pdf.table(table_data, style=style)
# pdf.showPage()
# pdf.save()
# # c.drawString(30, h - 50, "Line")
# # x = 120
# # y = h - 45
# # c.line(x, y, x + 100, y)
# # c.drawString(30, h - 100, "Rectangle")
# # c.rect(x, h - 120, 100, 50)
# # c.drawString(30, h - 170, "Circle")
# # c.circle(170, h - 165, 20)
# # c.drawString(30, h - 240, "Ellipse")
# # c.ellipse(x, y - 170, x + 100, y - 220)
# # c.setFillColorRGB(0, 0, 255)
# # c.drawString(50, h - 50, "Hello world!")
# # c.rect(500, h - 150, 50, 50, fill=True)
# # c.setStrokeColorRGB(1, 0, 0)
# # c.setFont("Helvetica", 10)
# # c.setFont("Courier-Bold", 24)
# # c.drawString(650, h - 650, "Hello world!")
# # c.setFont("Times-Roman", 20)
# # c.drawString(130, h - 50, "Hello world!")
# # text = c.beginText(50, h - 50)
# # text.setFont("Times-Roman", 12)
# # text.textLine("Hello world!")
# # text.textLine("From ReportLab and Python!")
# # text.textLines("Hello world!\nFrom ReportLab and Python!")
# # c.drawText(text)
# # c.drawImage(r"C:\Users\Vrdella\Pictures\Screenshots\Screenshot (187).png", 500, h - 200)
# # c.drawImage(r"C:\Users\Vrdella\Pictures\Screenshots\Screenshot (187).png", 500, h - 200, width=50, height=50)
# # xlist = [10, 60, 110, 160]
# # ylist = [h - 10, h - 60, h - 110, h - 160]
# # c.grid(xlist, ylist)




import itertools
from random import randint
from statistics import mean

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


def export_to_pdf(data):
    c = canvas.Canvas("grid-students.pdf", pagesize=A4)
    w, h = A4
    max_rows_per_page = 45
    # Margin.
    x_offset = 50
    y_offset = 50
    # Space between rows.
    padding = 15

    xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()

    c.save()


data = [("NAME", "GR. 1", "GR. 2", "GR. 3", "AVG", "STATUS")]

for i in range(1, 101):
    exams = [randint(0, 10) for _ in range(3)]
    avg = round(mean(exams), 2)
    state = "Approved" if avg >= 4 else "Disapproved"
    data.append((f"Student {i}", *exams, avg, state))

export_to_pdf(data)