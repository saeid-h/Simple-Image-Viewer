#!/usr/bin/env python
##############################################################################
#
# Copyright (c) 2020 Saeid Hosseinipoor <shossei1@stevens.edu>
# All rights reserved.
# Licensed under the New BSD License
#
##############################################################################
from __future__ import absolute_import, division, print_function

import PIL.Image

try:
	import clipboard
	CLIPBOARD_FLAG = False
except:
	CLIPBOARD_FLAG = False 

try:
	from helpers import *
except:
	from src.helpers import *

try:
	from Tkinter import *
	import tkFileDialog as filedialog
except ImportError:
	from tkinter import *
	from tkinter import filedialog
import PIL.ImageTk

class SimpleImageViewer(Frame):
	def chg_image(self, filename):
		self.original_image, self.display_image = open_image(self, filename)
		self.image_format = filename.split('.')[-1].lower()
		self.image_index = self.image_list.index(filename)
		sp = filename.split('/')
		path = '/'.join(sp[:2]+['...']+sp[-2:])
		self.master.title('Simple Image Viewer: '+path)
			
		self.display_image = PIL.Image.fromarray(self.display_image)
		self.img = PIL.ImageTk.PhotoImage(self.display_image)
		self.la.config(image=self.img, bg="#000000", width=self.img.width(), height=self.img.height())

	def open(self):
		filename = filedialog.askopenfilename(title = "Select file",filetypes = ALL_TYPES)
		
		if filename != "" and filename.split('.')[-1] in EXTENSIONS:
			dirName = '/'.join(filename.split('/')[:-1])+'/'
			self.image_list = getListOfFiles(dirName, masks=MASKS)
			self.chg_image(filename)
			self.image_list.sort()
		
	def save_as(self):
		if not hasattr(self, 'original_image'): 
			print ("Error: Select and open an image first.")
			return
		filename = filedialog.asksaveasfilename(filetypes = IMAGE_TYPES, defaultextension='.png') 
		if not filename: return
		print ('Saving '+filename)
		save_image (self, filename)
		
	def seek_prev(self):
		if self.image_index > 0:
			self.image_index -= 1
		else:
			self.image_index = len(self.image_list) - 1
		filename = self.image_list[self.image_index]
		if filename != "" and filename.split('.')[-1] in EXTENSIONS:
			self.chg_image(filename)
		print (self.image_index, filename)


	def seek_next(self):
		if self.image_index < len(self.image_list)-1:
			self.image_index += 1
		else:
			self.image_index = 0
		filename = self.image_list[self.image_index]
		if filename != "" and filename.split('.')[-1] in EXTENSIONS:
			self.chg_image(filename)
		print (self.image_index, filename)

	def ctrl_c(self):
		if not hasattr(self, 'display_image'): 
			print ("Error: Select and open an image first.")
			return
		# clipboard.set_image(self.im, format='png')
		clipboard.copy(self.im)


	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master.title('Simple Image Viewer')

		self.image_list = list()
		self.caption = StringVar()

		frame_top = Frame(self)
		Button(frame_top, text="Open File ...", command=self.open).pack(side=LEFT)
		Button(frame_top, text="Save as ...", command=self.save_as).pack(side=LEFT)
		if CLIPBOARD_FLAG:
			Button(frame_top, text="Copy to clipboard", command=self.ctrl_c).pack(side=RIGHT)

		frame_bot = Frame(self)
		Button(frame_bot, text="Prev", command=self.seek_prev).pack(side=LEFT)
		Button(frame_bot, text="Next", command=self.seek_next).pack(side=RIGHT)
				
		Label(frame_top, textvariable=self.caption).pack(side=LEFT)
		self.la = Label(self)

		frame_top.pack(side=TOP, fill=BOTH)
		frame_bot.pack(side=BOTTOM, fill=BOTH)
		self.la.pack()
		self.pack()

if __name__ == "__main__":
	app = SimpleImageViewer()
	app.mainloop()