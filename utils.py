import cv2 as cv
import keras.backend as K
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec


def predict(gray):
    h_in, w_in = 256, 256
    h_out, w_out = h_in // 4, w_in // 4
    epsilon = 1e-6
    T = 0.38

    img_rows, img_cols = gray.shape[:2]

    model_path = 'models/model.06-2.5489.hdf5'
    model = load_model(model_path)

    q_ab = np.load("data/pts_in_hull.npy")
    nb_q = q_ab.shape[0]

    L = gray
    gray = cv.resize(gray, (h_in, w_in), cv.INTER_CUBIC)

    x_test = np.empty((1, h_in, w_in, 1), dtype=np.float32)
    x_test[0, :, :, 0] = gray / 255.

    X_colorized = model.predict(x_test)
    X_colorized = X_colorized.reshape((h_out * w_out, nb_q))

    X_colorized = np.exp(np.log(X_colorized + epsilon) / T)
    X_colorized = X_colorized / np.sum(X_colorized, 1)[:, np.newaxis]

    q_a = q_ab[:, 0].reshape((1, 313))
    q_b = q_ab[:, 1].reshape((1, 313))

    X_a = np.sum(X_colorized * q_a, 1).reshape((h_out, w_out))
    X_b = np.sum(X_colorized * q_b, 1).reshape((h_out, w_out))

    X_a = cv.resize(X_a, (img_cols, img_rows), cv.INTER_CUBIC)
    X_b = cv.resize(X_b, (img_cols, img_rows), cv.INTER_CUBIC)

    X_a = X_a + 128
    X_b = X_b + 128

    out_lab = np.zeros((img_rows, img_cols, 3), dtype=np.int32)
    out_lab[:, :, 0] = L
    out_lab[:, :, 1] = X_a
    out_lab[:, :, 2] = X_b

    out_lab = out_lab.astype(np.uint8)
    out_bgr = cv.cvtColor(out_lab, cv.COLOR_LAB2BGR)

    out_bgr = out_bgr.astype(np.uint8)

    K.clear_session()

    return out_bgr


def _plot_image(ax, img, cmap=None, label=''):
    ax.imshow(img, cmap)
    ax.tick_params(axis='both',
                   which='both',
                   bottom='off',
                   top='off',
                   left='off',
                   right='off',
                   labelleft='off',
                   labelbottom='off')
    ax.set_xlabel(label)


def plot_bw_color_comparison(bw, color):
    gs = gridspec.GridSpec(6, 13)
    gs.update(hspace=0.1, wspace=0.001)
    fig = plt.figure(figsize=(7, 3))
    ax = fig.add_subplot(gs[:, 0:6])
    _plot_image(ax, bw, cmap='gray', label='original image')
    ax = fig.add_subplot(gs[:, 7:13])
    _plot_image(ax, color, label='colorized result')
    plt.show()
