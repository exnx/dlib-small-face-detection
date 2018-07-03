# dlib-small-face-detection

A modified dlib face detector that allows you to find faces much smaller.  It
upsizes the resolution for a given region of interest (passed to it), and searches
for a face there.  It then rectify the found bounding box coordinates to the orginal 
frame.  Passing a ROI is optional, but makes it run much faster.

Requirements:

dlib, imutils, Opencv, Python 3, cmake, xboost
