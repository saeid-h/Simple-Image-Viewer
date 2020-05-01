
# Simple Image Viewer
This python code provides a simple image viewer for the rgular image formats. This image viewer also supports non-standard floating point images which are widely used in computer vision including optical flow, disparity, and depth formats. 

# File Format Support
* png, jpg, ...:  &nbsp;&nbsp;   All regular images.
* flo: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Middleburry optical flow.
* dpt: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Middleburry depth.
* pfm: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Freiburg floating point disparity.

# Python Package

You can also download and install the **Simple Image Viewer** as a python package by:
```
python -m pip install simple-image-viewer
```
Then you can simply import it in a python code and use it as follows:
```python
from simple_image_viewer import *
SimpleImageViewer().mainloop()
```

## Donation
If this project help you reduce time to develop, you can give me a cup of coffee :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=VVZ72HZMRRM24&currency_code=USD&source=url)


Copyright (c) 2020 Saeid Hosseinipoor [Github](https://github.com/saeid-h) / [Web Page](https://saeid-h.github.io/) 