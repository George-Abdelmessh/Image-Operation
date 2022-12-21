from itertools import product
from PIL import Image
import numpy as np
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros

class GaussianFilter:
    
    def __init__(self, path):
        self.image = path
        
    def gen_gaussian_kernel(self, k_size, sigma):
        center = k_size // 2
        x, y = mgrid[0 - center : k_size - center, 0 - center : k_size - center]
        g = 1 / (2 * pi * sigma) * exp(-(square(x) + square(y)) / (2 * square(sigma)))
        return g


    def gaussian_filter(self, image, k_size, sigma):
        height, width = image.shape[0], image.shape[1]
        # dst image height and width
        dst_height = height - k_size + 1
        dst_width = width - k_size + 1

        # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
        image_array = zeros((dst_height * dst_width, k_size * k_size))
        row = 0
        for i, j in product(range(dst_height), range(dst_width)):
            window = ravel(image[i : i + k_size, j : j + k_size])
            image_array[row, :] = window
            row += 1

        #  turn the kernel into shape(k*k, 1)
        gaussian_kernel = self.gen_gaussian_kernel(k_size, sigma)
        filter_array = ravel(gaussian_kernel)

        # reshape and get the dst image
        dst = dot(image_array, filter_array).reshape(dst_height, dst_width).astype(uint8)

        return dst


    def apply_filter(self):
        # read original image and turn image in gray scale value
        img = np.array(Image.open(self.image).convert('L'))
        try:
            mask = int(input("Enter Mask 'Recommend To Be Odd Number': "))
        except:
            print("Mask Must Be Intger!")
        try:
            sigma = float(input("Enter Sigma 'Must Be > 0 & < 1': "))
        except:
            print("Mask Must Be Float!")

        # get values with two different mask size
        gaussian = self.gaussian_filter(img, mask, sigma=sigma)
        
        # show result images
        self.img1 = Image.fromarray(gaussian)
        # Save image
        self.save = input("Do You Need To Save the New Image (Y/N): ")
        if self.save.lower() == 'y':
            if self.img1.mode != 'RGB':
                self.img_name = input("Enter Image Name: ")
                self.new_img =self.img1.convert('RGB')
                self.new_img.save(f'{self.img_name}.jpg')
        # Show the new image
        self.img1.show()

