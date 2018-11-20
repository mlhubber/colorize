# Import the necessary packages.
print("Loading the required Python modules ...\n")

import os
import cv2 as cv
import glob
import sys
import readline
import re
import toolz
import urllib
import numpy as np
import socket

from utils import get_predict_api, plot_bw_color_comparison
from mlhub import utils as mlutils

print("Loading the model ...")
predict, _ = get_predict_api()

def _tab_complete_path(text, state):
    if '~' in text:
        text = os.path.expanduser('~')

    if os.path.isdir(text):
        text += '/'

    return [x for x in glob.glob(text + '*')][state]


def _is_url(url):
    """Check if url is a valid URL."""

    urlregex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(urlregex, url) is not None:
        return True
    else:
        return False


def _read_cv_image_from(url):
    """Read an image from url or file as grayscale opencv image."""

    return toolz.pipe(
        url,
        urllib.request.urlopen if _is_url(url) else lambda x: open(x, 'rb'),
        lambda x: x.read(),
        bytearray,
        lambda x: np.asarray(x, dtype="uint8"),
        lambda x: cv.imdecode(x, cv.IMREAD_GRAYSCALE))


def _colorize_one_img(url):
    """colorize a single image in url.

    Args:
        url (str): a url to an image, or a path to an image.
    """

    try:
        gray = _read_cv_image_from(url)
    except (urllib.error.URLError, socket.gaierror, FileNotFoundError, OSError):
        print("URL or file invalid:\n  {}".format(url))
        return

    print("Colorize " + url)
    color = predict(gray)
    gray_name = os.path.basename(url).split('.')
    color_name = '.'.join(['.'.join(gray_name[:-1]) + "_color", gray_name[-1]])
    cv.imwrite(os.path.join(CMD_CWD, color_name), color)
    plot_bw_color_comparison(gray, cv.cvtColor(color, cv.COLOR_BGR2RGB))
    print("    into " + color_name)


def _colorize(url):
    """Colorize the images in url.

    Args:
        url (str): a url to an image, or a path to an image, or a dir for images.
    """

    if _is_url(url):
        _colorize_one_img(url)
    else:
        # Change to the dir of command which invokes this script
        if CMD_CWD != '':
            oldwd = os.getcwd()
            os.chdir(CMD_CWD)

        url = os.path.abspath(os.path.expanduser(url))

        if CMD_CWD != '':
            os.chdir(oldwd)

        if os.path.isdir(url):
            for img in os.listdir(url):
                img_file = os.path.join(url, '', img)
                _colorize_one_img(img_file)
        else:
            _colorize_one_img(url)


# The working dir of the command which invokes this script.

CMD_CWD = mlutils.get_cmd_cwd()


# Setup input path completion

readline.set_completer_delims('\t')
readline.parse_and_bind("tab: complete")
readline.set_completer(_tab_complete_path)


# Scoring

if len(sys.argv) < 2:
    try:
        url = input("\nPath or URL of images to colorize (Quit by Ctrl-d):\n(You could try images in '~/.mlhub/colorize/images/')\n> ")
    except EOFError:
        print()
        sys.exit(0)

    while url != '':
        _colorize(url)

        try:
            url = input('\nPath or URL of images to colorize (Quit by Ctrl-d):\n> ')
        except EOFError:
            print()
            sys.exit(0)
else:
    for url in sys.argv[1:]:
        _colorize(url)
