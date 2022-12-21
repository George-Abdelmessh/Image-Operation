from PIL import Image
import numpy as np


class MedianFilter:

    def __init__(self, path):
        self.image = path

    def apply_filter(self):
        # Read the image
        self.img = np.array(Image.open(self.image).convert('L'))
        # Obtain the number of rows and columns of the image
        self.m, self.n = self.img.shape
        # Traverse the image. For every 3X3 area,
        # find the median of the pixels and
        # replace the center pixel by the median
        self.img_new1 = np.zeros([self.m, self.n])

        for i in range(1, self.m-1):
            for j in range(1, self.n-1):
                self.temp = [self.img[i-1, j-1],
                    self.img[i-1, j],
                    self.img[i-1, j + 1],
                    self.img[i, j-1],
                    self.img[i, j],
                    self.img[i, j + 1],
                    self.img[i + 1, j-1],
                    self.img[i + 1, j],
                    self.img[i + 1, j + 1]]
                
                self.temp = sorted(self.temp)
                self.img_new1[i, j]= self.temp[4]

        # Convert matrix to image
        self.img_new1 = self.img_new1.astype(np.uint8)
        self.img = Image.fromarray(self.img_new1)
        # Save image
        self.save = input("Do You Need To Save the New Image (Y/N): ")
        if self.save.lower() == 'y':
            if self.img.mode != 'RGB':
                self.img_name = input("Enter Image Name: ")
                self.new_img =self.img.convert('RGB')
                self.new_img.save(f'{self.img_name}.jpg')
        # Show Image
        self.img.show()
