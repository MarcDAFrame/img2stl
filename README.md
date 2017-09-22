# img2stl v0.0

## Synopsis
This code converts 2D images to gray scale and then given the gray values creates a height map. This can create some neat effects and could be used for 3D printing a portrait or abstract designs.

Just a neat side project that was in my head for a few weeks.

## Examples

| Raw Image  | Stair.stl |        Stair.stl (with blur)       |
| ------------- | ------------- | ------------- |
| <img src="https://github.com/MarcDAFrame/img2stl/blob/master/git%20imgs/gradient.jpg" width="200" height="150">  | <img src="https://github.com/MarcDAFrame/img2stl/blob/master/git%20imgs/stairs.PNG" width="200" height="150">  |     <img src="https://github.com/MarcDAFrame/img2stl/blob/master/git%20imgs/blurred%20stairs.PNG" width="200" height="150">          |
| this is the image  | basic settings |      with a blur of (50, 50)         |
  
| Raw Image  | Elvis.stl |        Elvis.stl (with invert)       |
| ------------- | ------------- | ------------- |
| <img src="https://github.com/MarcDAFrame/img2stl/blob/master/git%20imgs/elvis.jpg" width="200" height="150">  | <img src="https://github.com/MarcDAFrame/img2stl/blob/master/git%20imgs/elvis.PNG" width="200" height="150">  |     <img src="https://github.com/MarcDAFrame/img2stl/blob/master/git%20imgs/elvis%20inverted.PNG" width="200" height="150">          |
| this is the image  | basic settings |      with inverted = True        |


## Methods:
  - **run(img_dir, out_dir, blur=None, invert=False)**
  
      runs the whole project instead of you having to call individual functions

      @param {string} img_dir - The image directory
      
      @param {string} out_dir - The file for the stl to be saved to
      
      @param {tuple} blur - (h, v) h is horizotal blur coefficient, v is vertical blur coefficient. If you don't want a blur, leave empty
      
      @param {boolean} invert - invert the heights. dark and light switches heights

      ex. of call run("test.png", "test.stl", (5, 5))

      @returns {None}
  - **convert_image(gray_img, out_dir, invert=False)**
  
      takes image and converts it to STL based off of pixel value

      @param {numpy image array} gray_img - numpy array with gray image
      
      @param {string} out_dir - The file for the stl to be saved to
      
      @param {boolean} invert - invert the heights. dark and light switches heights

      @returns {None}
  - **get_gray_img(img_dir)**
  
      gets an image and gray scales it

      @param {string} img_dir - The image directory

      @returns {numpy image array}
  - **blur_img(img, blur=(5, 5))**
  
      blurs and image so that the final product looks smooth and doesn't have as many jagged lines

      @param {numpy image array} img - numpy array of an image
      
      @param {tuple} blur - (h, v) h is horizotal blur coefficient, v is vertical blur coefficient

      @returns {numpy image array}

## TODO:
  - add threshold so you can remove pure white values / noise
