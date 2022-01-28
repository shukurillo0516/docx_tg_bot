from docx import Document
from docx.shared import Inches
from docx.shared import Pt
from docx.enum.section import WD_ORIENT

from docx.oxml import OxmlElement
from docx.oxml.ns import qn


document = Document()
section = document.sections[0]

# Customizing font
style = document.styles['Normal']
font = style.font
font.name = 'Arial'

# Customizing orientation
section.orientation = WD_ORIENT.LANDSCAPE
section.page_width = Inches(11.69)
section.page_height = Inches(8.27)

# Spliting page into two columns
sectPr = section._sectPr
cols = sectPr.xpath('./w:cols')[0]
cols.set(qn('w:num'),'2')

# Customizing margins of a page
section.right_margin, section.left_margin, section.top_margin, section.bottom_margin = 0, Inches(.5), Inches(.1), Inches(.1)


def add_paragraph(text, f_size=16):
	p = document.add_paragraph().add_run(text)
	p.font.size = Pt(f_size)


def fill_first_column():
	for i in range(24):
		add_paragraph('')


fill_first_column()
add_paragraph("text")
fill_first_column()
add_paragraph("text2", 12)





document.save("docs/messages.docx")