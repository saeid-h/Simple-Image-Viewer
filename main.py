#!/usr/bin/env python

##############################################################################
#
# Copyright (c) 2020 Saeid Hosseinipoor <shossei1@stevens.edu>
# All rights reserved.
# Licensed under the New BSD License
#
##############################################################################
import src.simple_image_viewer as imv

if __name__ == "__main__":
	app = imv.SimpleImageViewer()
	app.mainloop()