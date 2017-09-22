import numpy as np
from stl import mesh
import cv2

def convert_image(gray_img, out_dir, invert=False):
    """
    takes image and converts it to STL based off of pixel value

    @param {numpy image array} gray_img - numpy array with gray image
    @param {string} out_dir - The file for the stl to be saved to
    @param {boolean} invert - invert the heights. dark and light switches heights

    @returns {None}
    """

    #creates vertices from image with the height of the cube being based off of the pixels height
    vertices_array = []
    faces_array = []
    for x,row in enumerate(gray_img):
        for y,pixel in enumerate(row):
            if invert:
                vertices = np.array([\
                    [x, y, 0],
                    [x+1, y, 0],
                    [x+1, y+1, 0],
                    [x, y+1, 0],                

                    [x, y, 255-pixel],
                    [x+1, y, 255-pixel],
                    [x+1, y+1, 255-pixel], 
                    [x, y+1, 255-pixel],
                ])

            else:
                vertices = np.array([\
                    [x, y, 0],
                    [x+1, y, 0],
                    [x+1, y+1, 0],
                    [x, y+1, 0],                

                    [x, y, pixel],
                    [x+1, y, pixel],
                    [x+1, y+1, pixel], 
                    [x, y+1, pixel],
                ])

            vertices_array.append(vertices)

    faces = np.array([[0,3,1],[1,3,2],[0,4,7],[0,7,3],[4,5,6],[4,6,7],[5,1,2],[5,2,6],[2,3,6],[3,7,6],[0,1,5],[0,5,4]])

    #creates meshes from vertices
    meshes = []
    for vertice in vertices_array:
        cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(faces):
            for j in range(3):
                cube.vectors[i][j] = vertice[f[j],:]
        
        meshes.append(cube)
    
    #combines all meshes together
    total_length_data = 0
    for i in range(len(meshes)):
        total_length_data += len(meshes[i].data)

    data = np.zeros(total_length_data, dtype = mesh.Mesh.dtype)
    data['vectors'] = np.array(meshes).reshape((-1, 9)).reshape((-1, 3, 3))
    mesh_final = mesh.Mesh(data.copy())

    #saves final mesh
    mesh_final.save(out_dir)

def get_gray_img(img_dir):
    """
    Gets an image and gray scales it

    @param {string} img_dir - The image directory

    @returns {numpy image array}
    """
    img = cv2.imread(img_dir)
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return gray_img

def blur_img(img, blur=(5, 5)):
    """
    blurs and image so that the final product looks smooth and doesn't have as many jagged lines

    @param {numpy image array} img - numpy array of an image
    @param {tuple} blur - (h, v) h is horizotal blur coefficient, v is vertical blur coefficient

    @returns {numpy image array}
    """
    img = cv2.blur(img,blur)
    return img

def run(img_dir, out_dir, blur=None, invert=False):
    """
    runs the whole project instead of you having to call individual functions

    @param {string} img_dir - The image directory
    @param {string} out_dir - The file for the stl to be saved to
    @param {tuple} blur - (h, v) h is horizotal blur coefficient, v is vertical blur coefficient. If you don't want a blur, leave empty
    @param {boolean} invert - invert the heights. dark and light switches heights

    ex. of call run("test.png", "test.stl", (5, 5))

    @returns {None}
    """

    img = get_gray_img(img_dir)

    if blur:
        img = blur_img(img, blur)
    
    convert_image(img, out_dir, invert)
