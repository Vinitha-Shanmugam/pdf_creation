# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
#
#
# def generate_pdf():
#     # Create a PDF document
#     pdf_file_path = "example.pdf"
#     pdf = SimpleDocTemplate(pdf_file_path, pagesize=letter)
#
#     # Set up the table data
#     table_data = [
#         ["Name", "Age", "Country"],
#         ["John Doe", "30", "USA"],
#         ["Jane Smith", "25", "Canada"],
#         ["Bob Johnson", "40", "UK"]
#     ]
#
#     # Set up the table style
#     style = TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Bottom padding for header row
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background color for data rows
#     ])
#
#     # Create the table and apply the style
#     table = Table(table_data)
#     table.setStyle(style)
#
#     # Build the PDF document
#     elements = [table]
#     pdf.build(elements)
#
#
# generate_pdf()
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_pdf():
    # Create a PDF document
    pdf_file_path = "example.pdf"
    pdf = SimpleDocTemplate(pdf_file_path, pagesize=letter)

    # Set up the table data
    table_data = [
    ["S.No", "Item Name", "MRP", "Quantity", "Pcs", "Base Rate", "Disc 1", "Disc 2",
     "Taxable Amt", "CSGT Amt", "CGST Tax%", "S/UTGST Amt", "S/UTGST Tax%", "Net Amount"],
    [1, "Sample Item 1", 25.99, 5, "20.00", 2.00, 1.00, 90.00, 4.50, 5.00, 4.50, 5.00, 99.00],
    [2, "Sample Item 2", 25.00, 5, "20.00", 2.00, 1.00, 90.00, 4.50, 5.00, 4.50, 5.00, 99.00],
    # Add more rows as needed
]


    # Set up the table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header row background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Bottom padding for header row
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background color for data rows
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),  # Background color for even rows
    ])

    # Create the table and apply the style
    table = Table(table_data)
    table.setStyle(style)

    # Build the PDF document
    elements = [table]
    pdf.build(elements)

generate_pdf()
