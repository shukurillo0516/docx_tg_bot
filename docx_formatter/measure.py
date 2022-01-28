# Python 3 names -- see Note below
import tkinter 
from tkinter import font as tkFont

tkinter.Frame().destroy()  # Enough to initialize resources
arial36b = tkFont.Font(family='Arial', size=12)
text = "text   "


def measure_w(text) -> int: 
	return arial36b.measure(text)


# while measure_w(text) + measure_w('g') < 522:
# 	text += 'g'

print(measure_w(text), text)  # Prints: 400