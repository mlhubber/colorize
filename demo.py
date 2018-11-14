# Import required libraries.
print("Loading the required Python modules.\n")

import os
import cv2 as cv
import glob

from utils import predict, plot_bw_color_comparison, IMG_PATH


cwd = os.getcwd()
print("Demonstrate colorization using images found in\n",
      os.path.join(cwd, IMG_PATH), "\n")

print("Please close each image (Ctrl-w) to proceed through the demonstration.\n")

if __name__ == '__main__':
    image_folder = 'images'

    images = glob.glob(os.path.join(IMG_PATH, "*_bw.png"))
    images.sort()

    for image in images:
        print("Colorize " + os.path.basename(image))
        gray = cv.imread(image, 0)
        out = predict(gray)
        plot_bw_color_comparison(gray, cv.cvtColor(out, cv.COLOR_BGR2RGB))
