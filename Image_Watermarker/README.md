# Image Watermarker

This script adds watermarks to images.

## Features
    *Supports jpeg and png images (pdfs are not supported)
    *Can apply a watermark to multiple images in the same path
    *Watermark would be applied on the center of an image (watermark should have a transparent background)


## Getting Started
Upon startup, you will be prompted to provide the path of your folder containing your source images and your watermark
.  The full path is required if the files are not in the same directory as the Python script.
I have included a sample watermark in this directory
.  Note that this script does not resize your images so keep in mind the size of your watermark when applying it over multiple images.
  
## Prerequisites
Python 3.6 or later is required.

Required Python modules:

    *PIL
    *OS (included in standard library)
    *glob (included in standard library)
  
## Example
![Image](Screenshot.png)

![Image](Sample_Watermark.png)

![Image](Watermarked_Image.jpg)
