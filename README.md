# Simple Colorization

Bare minimal code to run colorization demo.

## Dependencies

- [NumPy](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
- [Tensorflow](https://www.tensorflow.org/versions/r0.8/get_started/os_setup.html)
- [Keras](https://keras.io/#installation)
- [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/)

## Usage

* To install and run the pre-built model::

  $ pip install mlhub
  $ ml install colorize
  $ ml configure colorize
  $ ml demo colorize

* To colorize:

  - An image from a local file:

    ```console
      $ ml score colorize ~/.mlhub/colorize/images/image_07_bw.png
    ```

  - Images in a folder:

    ```console
      $ ml score colorize ~/.mlhub/colorize/images
    ```

  - An image from the web:

    ```console
      $ ml score colorize https://github.com/foamliu/Simple-Colorization/raw/master/images/sample.png
    ```

  - Interatively without repeatedly reloading the model:

    ```console
      $ ml score colorize
    ```

