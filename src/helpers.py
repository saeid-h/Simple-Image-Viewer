
#!/usr/bin/env python
##############################################################################
#
# Copyright (c) 2020 Saeid Hosseinipoor <shossei1@stevens.edu>
# All rights reserved.
# Licensed under the New BSD License
#
##############################################################################

from __future__ import absolute_import, division, print_function

import os, glob
import scipy.misc

try:
	from sintel_io import *
	from flowlib import *
except:
	from src.sintel_io import *
	from src.flowlib import *

TK_SILENCE_DEPRECATION=1
MASKS = ('*.*', '*.jpg', '*.png', '*.flo', '*.dpt')
MASK_DESCRIPTION = ('all files', 'jpeg files', 'png files', 
					'flow files', 'depth files')
FILE_TYPES = zip(MASK_DESCRIPTION, MASKS)
EXTENSIONS = [mask.split('.')[-1] for mask in MASKS[1:]]
EXTENSIONS += ['jpeg']

def getListOfFiles(dirName, masks=['*.png'], sudirectories=False):
	listOfFile = os.listdir(dirName)
	allFiles = list()
	for mask in masks:
		allFiles += glob.glob(dirName+mask)
	for entry in listOfFile:
		fullPath = os.path.join(dirName, entry) + '/'
		if os.path.isdir(fullPath) and sudirectories:
			allFiles += getListOfFiles(fullPath, masks)
	
	return allFiles


def open_image (filename):
	extension = filename.split('.')[-1].lower()
	if extension in ['png', 'jpg', 'jpeg']:
		image = scipy.misc.imread(filename)
	elif extension == 'flo':
		flow = read_flow(filename)
		image = flow_to_image(flow)
	elif extension == 'dpt':
		image = 1. / depth_read(filename)
		image = image / np.max(image) * 255
	else:
		try:
			image = scipy.misc.imread(filename)
		except:
			image = np.ones([200,400]) * 255
			for i in range(100):
				image[i, 2*i] = 0
				image[99-i, 199-2*i] = 0
	
	return image
	

if __name__ == "__main__":
	pass