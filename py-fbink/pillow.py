#!/usr/bin/env python
"""
Another example on how to print image data via Pillow.

This example basically swaps FBInk's decoding for Pillow's,
but the intent is simply to show how it can be used,
ideally for image data *created* via Pillow ;).

(Because if your aim was actually simply to print an image file,
simply doing FBInk.fbink_print_image(fbfd, sys.argv[1], 0, 0, fbink_cfg) would be faster ;p).
"""

# To get a Py3k-like print function
from __future__ import print_function

import sys
# Load the wrapper module, it's linked against FBInk, so the dynamic loader will take care of pulling in the actual FBInk library
from _fbink import ffi, lib as FBInk

# Let's check which FBInk version we're using...
# NOTE: ffi.string() returns a bytes on Python 3, not a str, hence the extra decode
print("Loaded FBInk {}".format(ffi.string(FBInk.fbink_version()).decode("ascii")))

# Setup the config...
fbink_cfg = ffi.new("FBInkConfig *")
fbink_cfg.is_centered = True
fbink_cfg.is_halfway = True
fbink_cfg.is_verbose = True
fbink_cfg.is_flashing = True

# Abort if we weren't passed a filepath...
if len(sys.argv) < 2:
	raise SystemExit("Expected a path to an image file as the first argument!")

# NOTE: No error checking is done here!
fbfd = FBInk.fbink_open()
try:
	FBInk.fbink_init(fbfd, fbink_cfg)

	# Load the image specified on the command line...
	from PIL import Image
	im = Image.open(sys.argv[1])
	print("Image mode: {}".format(im.mode))
	print("Image size: {}x{}".format(im.width, im.height))

	# Now, make sure we'll pass raw data in a format FBInk/stb knows how to handle, doing as few conversions as possible.
	# If image is paletted, translate that to actual values, because stb won't know how to deal with paletted raw data...
	if im.mode == "P":
		print("Image is paletted, translating to actual values")
		# NOTE: No mode means "just honor the palette". Usually, that's RGB.
		#       We could also enforce Grayscale (L), but FBInk/stb will take care of that if needed.
		im = im.convert()

	# If image is not grayscale, RGB or RGBA (f.g., might be a CMYK JPEG) convert that to RGBA.
	if im.mode not in ["L", "RGB", "RGBA"]:
		print("Image data is packed in an unsupported mode, converting to RGBA")
		im = im.convert("RGBA")

	# And finally, get that image data as raw packed pixels.
	raw_data = im.tobytes("raw")
	raw_len = len(raw_data)
	print("Raw data buffer length: {}".format(raw_len))

	FBInk.fbink_print_raw_data(fbfd, raw_data, im.width, im.height, raw_len, 0, 0, fbink_cfg)
finally:
	FBInk.fbink_close(fbfd)

"""
NOTE: If you want to leave *all* the pixel format conversions to Pillow,
      you'll instead have to target the expected pixel format for the fb,
      which you can do with something like this.
      In practice, this is usually slower than letting FBInk/stb handle it, though.

      Unless, again, you're *creating* image data via Pillow, in which case,
      it's definitely better to create it in the appropriate pixel format from the get go ;).

	# Figure out which pixel-format is best suited to the current fb/settings
	fbink_state = ffi.new("FBInkState *")
	FBInk.fbink_get_state(fbink_cfg, fbink_state)

	# Assume RGB by default
	target_mode = "RGB"
	# Switch to grayscale if fb <= 8bpp
	if fbink_state.bpp <= 8:
		target_mode = "L"
	# Enable alpha unless we requested ignore_alpha
	if not fbink_cfg.ignore_alpha:
		target_mode += "A"
	print("Target mode: {}".format(target_mode))

"""
