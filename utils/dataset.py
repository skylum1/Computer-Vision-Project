
import os
import re
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from PIL import Image
def illum(image):
# read input
  hh, ww = image.shape[:2]
  print(hh, ww)
  max =hh ;#max(hh, ww)
  if max<ww:
    max=ww
  # # illumination normalize
  ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

  # # separate channels
  y, cr, cb = cv2.split(ycrcb)

  # # get background which paper says (gaussian blur using standard deviation 5 pixel for 300x300 size image)
  # # account for size of input vs 300
  sigma = int(5 * max / 300)
  print('sigma: ',sigma)
  gaussian = cv2.GaussianBlur(y, (0, 0), sigma, sigma)

  # # subtract background from Y channel
  y = (y - gaussian + 100)

  # # merge channels back
  ycrcb = cv2.merge([y, cr, cb])

  # #convert to BGR
  output = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

  # save results
  # cv2.imwrite('retina2_proc.jpg', output)

  # show results
  # cv2_imshow(image)
  temp=Image.fromarray(output).convert("L")
  return temp

'''
 Starting by a dataset name, this function return 
 classes => an array with all classes (subfolders inside dataset folder)
 filename => an array with all images filenames
 xFilepath => an array with all images name with path /dataset/classes_folder/filename.pgm
 y => an array with the relative label of filename||xFilepath
'''
def getDataset(dataset):
  directory = os.getcwd() + "/datasets/"+dataset+"/"
  classes = []
  filename = []
  xFilepath = []
  y = []
  for root, dirs, files in os.walk(directory):
    for dir in dirs:
      classes.append(dir)

#   classes.remove('.ipynb_checkpoints')
  for imgClass in classes:
    for file in os.listdir(directory + imgClass):
      if re.search("\.pgm$", file) and not re.search(".*Ambient[.]pgm$",file):
        y.append(imgClass) 
        xFilepath.append(imgClass + "/" + file)
        filename.append(file)
  return classes, filename, xFilepath, y







def getPersonalDataset():
	directory = os.getcwd() + "/datasets/personal/"

	x = []

	for root, dirs, files in os.walk(directory):
		for file in files:
			x.append("datasets/personal/" + file)

	return x
