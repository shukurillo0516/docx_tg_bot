# Python 3 names -- see Note below
import tkinter 
from tkinter import font as tkFont

 # Enough to initialize resources

PAGE_WIDTH = {
	16: 13900,
	15: 14600,
	14: 15100,
	13:	17100,
	12: 20500
}


def measure_w(text, f_size) -> int:
	settings = tkFont.Font(family='Arial', size=f_size)
	return settings.measure(text)


def adjust_font(text, f_size=16) -> list: 
	''' This function takes text and font size.
		Returns the most optimal font size to fit in the page.
		If even with smallest font size the text out of a page,
		then it returns the smallest font size and text'''
	tkinter.Frame().destroy() 
	if f_size == 12:
		return [text, f_size]

	if PAGE_WIDTH[f_size] >= measure_w(text, f_size):
		return [text, f_size]
	else:
		return adjust_font(text, f_size - 1)
	

# print(adjust_font(text, 16))
# print(measure_w(text, 13))

