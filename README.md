# Simple Colorization

This pre-built model from Yang Liu provides a very simple example of
photo colorization using deep neural networks. For the demonstration a
sample of provided black and white photos are colorized and
displayed. You can colorize your own local photo, a photo's URL, or a
folder of photos using the *apply* command.

See the github repository for examples of its usage:
https://github.com/mlhubber/colorize

## Usage

* To install mlhub:

  ```console
  $ pip3 install mlhub
  ```

* To install and configure the pre-built model:

  ```console
  $ ml install   colorize
  $ ml configure colorize
  ```

Demonstration
-------------

```console
$ ml demo colorize
Loading the required Python modules ...

Loading the model ...
Demonstrate colorization using images found in
 /home/gjw/.mlhub/colorize/images 

Please close each image (Ctrl-w) to proceed through the demonstration.

Colorize image_01_bw.png
```
![](image_01.png)
```console
Colorize image_02_bw.png
```
![](image_02.png)
```console
Colorize image_03_bw.png
```
![](image_03.png)
```console
Colorize image_04_bw.png
```
![](image_04.png)
```console
Colorize image_05_bw.png
```
![](image_05.png)
```console
Colorize image_06_bw.png
```
![](image_06.png)
```console
Colorize image_07_bw.png
```
![](image_07.png)
```console
Colorize image_09_bw.png
```
![](image_09.png)
```console
Colorize image_10_bw.png
```
![](image_10.png)
```console

To colorize images given by a path or URL:

  $ ml apply colorize

```

## Commands

- To colorize an image from a local file:

    ```console
    $ ml apply colorize ~/.mlhub/colorize/images/image_07_bw.png
    ```

    Then the colorized image will be saved into a file like
    `image_07_bw_color.png`.

- To colorize images in a folder:

    ```console
    $ ml apply colorize ~/.mlhub/colorize/images
    ```

- To colorize an image from the web:

    ```console
    $ ml apply colorize https://flower-wallpaper.org/wp-content/uploads/2016/10/black-and-white-flowers-wallpaper2.jpg
    $ ml apply colorize https://flower-wallpaper.org/wp-content/uploads/2016/10/black-and-white-flower-wallpaper1-310x165.jpg
    ```

- To interatively colorize without repeatedly reloading the model:

    ```console
    $ ml apply colorize
	Loading the required Python modules ...

    Loading the model ...

    Path or URL of images to colorize (Quit by Ctrl-d):
    (You could try images in '~/.mlhub/colorize/images/')
    > https://flower-wallpaper.org/wp-content/uploads/2016/10/black-and-white-flowers-wallpaper2.jpg
	> https://flower-wallpaper.org/wp-content/uploads/2016/10/black-and-white-flowers-wallpaper5-1.jpg
	> https://www.designsmag.com/wp-content/uploads/2017/06/Black-White-Photography-DesignsMag-011.jpg
    ```

