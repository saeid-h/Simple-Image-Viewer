#!/usr/bin/env python

##############################################################################
#
# Copyright (c) 2020 Saeid Hosseinipoor <shossei1@stevens.edu>
# All rights reserved.
# Licensed under the MIT License
#
##############################################################################
try:
	from simple_image_viewer.simple_image_viewer import *
except:
	from simple_image_viewer import *

if __name__ == "__main__":
	SimpleImageViewer().mainloop()