# Import required libraries.
print("Loading the required Python modules.")

import os
import cv2 as cv
import glob

from utils import predict, plot_bw_color_comparison


if __name__ == '__main__':
    image_folder = 'images'

    images = glob.glob("images/*_bw.png")
    images.sort()

    cwd = os.getcwd()
    for image in images:
        print("Colorize " + os.path.join(cwd, image))
        gray = cv.imread(image, 0)
        out = predict(gray)
        plot_bw_color_comparison(gray, cv.cvtColor(out, cv.COLOR_BGR2RGB))
