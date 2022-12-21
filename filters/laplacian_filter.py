import numpy as np
from PIL import Image

class LaplacianFilter:
        
    def __init__(self, path):
        self.image = path

    #Function to calculate 2D convolution of two matrix
    def conv2d(self, image, kernel):
        m, n = kernel.shape
        if (m == n):
            y, x = image.shape
            y = y - m + 1
            x = x - m + 1 
            self.new_image = np.zeros((y,x))
            for i in range(y):
                for j in range(x):
                    self.new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel) 
        return self.new_image

    def apply_filter(self):
        self.img = np.array(Image.open(self.image).convert('L'))
        self.conv_kernel = np.array([[0,1,0],
                                [1,-4,1],
                                [0,1,0]])
        self.img = Image.fromarray(self.conv2d(self.img, self.conv_kernel))
        # Save image
        self.save = input("Do You Need To Save the New Image (Y/N): ")
        if self.save.lower() == 'y':
            if self.img.mode != 'RGB':
                self.img_name = input("Enter Image Name: ")
                self.new_img =self.img.convert('RGB')
                self.new_img.save(f'{self.img_name}.jpg')
        # Show the new image
        self.img.show()
