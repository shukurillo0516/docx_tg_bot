# Python 3 names -- see Note below
import tkinter 
from tkinter import font as tkFont


from docx_formatter.rect_columns import FindEnd

PAGE_WIDTH = {
	16: 13900,
	15: 14600,
	14: 15100,
	13:	17100,
	12: 20500
}


def measure_w(text, f_size) -> int:
	tkinter.Frame().destroy()
	settings = tkFont.Font(family='Arial', size=f_size)
	return settings.measure(text)


def adjust_font(text, f_size=16) -> dict: 
	'''
		This function takes text and font size.
		Returns the most optimal font size to fit in the page.
		If even with smallest font size the text out of a page,
		then it passes to antother function (handle_content)
	'''
	tkinter.Frame().destroy() 
	if f_size == 12 and PAGE_WIDTH[12] < measure_w(text, f_size):
		cl = FindEnd()
		cl.find_end(text)

		text = cl.result
		resp = {
			"messages": text,
			"f_size": f_size
		}
		return resp
		# return handle_content(text)

	if PAGE_WIDTH[f_size] >= measure_w(text, f_size):
		resp = {
			"messages": [text],
			"f_size": f_size
		}
		return resp
	else:
		return adjust_font(text, f_size - 1)
	
