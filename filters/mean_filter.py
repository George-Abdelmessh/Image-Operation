from PIL import Image
import numpy as np


class MeanFilter:

    def __init__(self, path):
        self.image = path

    def apply_filter(self):
        # Read the image
        self.img = np.array(Image.open(self.image).convert('L'))
        # Obtain number of rows and columns of the image
        self.m, self.n = self.img.shape
        # Develop Averaging filter(3, 3) mask
        self.mask = np.ones([3, 3], dtype=int)
        self.mask = self.mask / 9
        # Convolve the 3X3 mask over the image
        self.img_new = np.zeros([self.m, self.n])

        for i in range(1, self.m-1):
            for j in range(1, self.n-1):
                temp = self.img[i-1, j-1] * self.mask[0, 0] + self.img[i-1, j] * \
                    self.mask[0, 1] + self.img[i-1, j + 1] * self.mask[0, 2] + \
                        self.img[i, j-1] * self.mask[1, 0] + self.img[i, j] * \
                            self.mask[1, 1] + self.img[i, j + 1] * self.mask[1, 2] + \
                                self.img[i + 1, j-1] *  self.mask[2, 0] + self.img[i + 1, j] * \
                                    self.mask[2, 1] + self.img[i + 1, j + 1] * self.mask[2, 2]
                self.img_new[i, j] = temp

        # Convert matrix to image
        self.img_new1 = self.img_new.astype(np.uint8)
        self.img = Image.fromarray(self.img_new1)
        # Save image
        self.save = input("Do You Need To Save the New Image (Y/N): ")
        if self.save.lower() == 'y':
            if self.img.mode != 'RGB':
                self.img_name = input("Enter Image Name: ")
                self.new_img =self.img.convert('RGB')
                self.new_img.save(f'{self.img_name}.jpg')
        # Show the new image
        self.img.show()
