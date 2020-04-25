
#!/usr/bin/env python
##############################################################################
#
# Copyright (c) 2020 Saeid Hosseinipoor <shossei1@stevens.edu>
# All rights reserved.
# Licensed under the New BSD License
#
##############################################################################

from __future__ import absolute_import, division, print_function

import os, glob, scipy.misc

try:
	from sintel_io import *
	from flowlib import *
	import pfmutil as pfm
except:
	from src.sintel_io import *
	from src.flowlib import *
	import src.pfmutil as pfm

os.environ['TK_SILENCE_DEPRECATION'] = '1'
MASKS = ('*.jpg', '*.png', '*.flo', '*.dpt', '*.pfm')
MASK_DESCRIPTION = ('jpeg files', 'png files', 'flow files', 'depth files', 'disparity files')
IMAGE_TYPES = zip(MASK_DESCRIPTION, MASKS)
ALL_TYPES = [('*.*', 'all files')] + IMAGE_TYPES
EXTENSIONS = [mask.split('.')[-1] for mask in MASKS]
EXTENSIONS += ['jpeg']

def getListOfFiles(dirName, masks=['*.png'], sudirectories=False):
	listOfFile = os.listdir(dirName)
	allFiles = list()
	for mask in masks:
		allFiles += glob.glob(dirName+mask)
	for entry in listOfFile:
		fullPath = os.path.join(dirName, entry) + '/'
		if os.path.isdir(fullPath) and sudirectories:
			allFiles += getListOfFiles(fullPath, masks, sudirectories)
	
	return allFiles

def open_image (obj, filename):
	extension = filename.split('.')[-1].lower()
	if extension in ['png', 'jpg', 'jpeg']:
		image = scipy.misc.imread(filename)
		disp_image = image
	elif extension == 'flo':
		image = read_flow(filename)
		disp_image = flow_to_image(image)
	elif extension == 'dpt':
		image = depth_read(filename)
		disp_image = 1. / image
		obj.dpt_max = np.amax(disp_image)
		disp_image = disp_image / np.amax(disp_image) * 255
	elif extension == 'pfm':
		image = pfm.load(filename)[0]
		disp_image = image
	else:
		try:
			image = scipy.misc.imread(filename)
			disp_image = image
		except:
			image = np.ones([200,400]) * 255
			for i in range(200):
				image[i, 2*i] = 0
				image[199-i, 398-2*i] = 0
			disp_image = image
	
	return image, disp_image
	
def save_image (obj, filename):
	extension = filename.split('.')[-1].lower()
	if extension in ['png', 'jpg', 'jpeg']:
		scipy.misc.imsave(filename, obj.display_image)
	elif extension == 'flo' and obj.image_format == 'flo':
		write_flow(image, obj.original_image)
	elif extension == 'dpt' and len(obj.original_image.shape) == 2:
		if obj.image_format == 'dpt':
			depth_write(filename, obj.original_image)
		else:
			depth_write(filename, 1. / obj.original_image)
	elif extension == 'pfm':
		if obj.image_format == 'dpt':
			pfm.save(filename, 1. / (obj.original_image / 255 * obj.dpt_max))
		else:
			pfm.save(filename, obj.original_image)
	else:
		try:
			scipy.misc.imsave(filename, obj.display_image)
		except:
			Print ("Error: Cannot save.")
	

if __name__ == "__main__":
	pass