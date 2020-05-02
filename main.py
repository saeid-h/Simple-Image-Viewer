#!/usr/bin/env python

##############################################################################
#
# Copyright (c) 2020 Saeid Hosseinipoor <https://saeid-h.github.io/>
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