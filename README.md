# Simple Colorization

This pre-built model from Yang Liu provides a very simple example of
photo colorization using deep neural networks. For the demonstration a
sample of provided black and white photos are colorized and
displayed. You can colorize your own local photo, a photo's URL, or a
folder of photos using the *score* command.

See the github repository for examples of its usage:
https://github.com/mlhubber/colorize

## Usage

* To install and run the pre-built model:

  ```console
  $ pip3 install mlhub
  $ ml install   colorize
  $ ml configure colorize
  $ ml demo      colorize
  ```

## Dependencies

- [NumPy](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
- [Tensorflow](https://www.tensorflow.org/versions/r0.8/get_started/os_setup.html)
- [Keras](https://keras.io/#installation)
- [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/)

## Examples

* To colorize:

  - An image from a local file:

    ```console
    $ ml score colorize ~/.mlhub/colorize/images/image_07_bw.png
    ```

    Then the colorized image will be saved into a file like
    `image_07_bw_color.png`.

  - Images in a folder:

    ```console
    $ ml score colorize ~/.mlhub/colorize/images
    ```

  - An image from the web:

    ```console
    $ ml score colorize https://flower-wallpaper.org/wp-content/uploads/2016/10/black-and-white-flowers-wallpaper2.jpg
    ```

  - Interatively without repeatedly reloading the model:

    ```console
    $ ml score colorize
    ```
