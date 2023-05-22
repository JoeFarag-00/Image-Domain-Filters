import cv2
import numpy as np
import matplotlib.pyplot as plt
class Interpolate:
  

    def nearest_neighbor_interpolation(self, scale_factor, image):
        self.image = image
        scaled_width = int(self.image.shape[1] * scale_factor)
        scaled_height = int(self.image.shape[0] * scale_factor)
        scaled_image = np.zeros((scaled_height, scaled_width), dtype=np.uint8)
        
        for i in range(scaled_height):
            for j in range(scaled_width):
                original_i = int(i / scale_factor)
                original_j = int(j / scale_factor)
                scaled_image[i, j] = self.image[original_i, original_j]
        
        return scaled_image
    def bilinear_interpolation(self, scale,image):
        self.image = image
        scaled_height = int(self.image.shape[0] * scale)
        scaled_width = int(self.image.shape[1] * scale)
        scaled_image = np.zeros((scaled_height, scaled_width), dtype=np.uint8)

        for i in range(scaled_height):
            for j in range(scaled_width):
                src_i = i / scale
                src_j = j / scale
                i1 = int(np.floor(src_i))
                i2 = int(np.ceil(src_i))
                j1 = int(np.floor(src_j))
                j2 = int(np.ceil(src_j))
                
                if i2 >= self.image.shape[0 ]:
                    i2 = self.image.shape[0] - 1
                if j2 >= self.image.shape[1]:
                    j2 = self.image.shape[1] - 1
                
                dx = src_i - i1
                dy = src_j - j1

                # Perform bilinear interpolation
                interpolated_value = (1 - dx) * (1 - dy) * self.image[i1, j1] \
                                     + dx * (1 - dy) * self.image[i2, j1] \
                                     + (1 - dx) * dy * self.image[i1, j2] \
                                     + dx * dy * self.image[i2, j2]

                scaled_image[i, j] = int(interpolated_value)

        return scaled_image
    def bicubic_interpolation(self, scale_factor,image):
        self.image = image
        height, width = self.image.shape

        new_height = int(height * scale_factor)
        new_width = int(width * scale_factor)

        scaled_image = np.zeros((new_height, new_width), dtype=np.uint8)

        for i in range(new_height):
            for j in range(new_width):
                x = (j + 0.5) / scale_factor - 0.5
                y = (i + 0.5) / scale_factor - 0.5

                x1 = int(np.floor(x))
                y1 = int(np.floor(y))

                dx = x - x1
                dy = y - y1

                interpolated_value = 0

                for m in range(-1, 3):
                    for n in range(-1, 3):
                        if (x1 + m >= 0 and x1 + m < width and y1 + n >= 0 and y1 + n < height):
                            weight_x = self.bicubic_weight(dx - m)
                            weight_y = self.bicubic_weight(dy - n)
                            interpolated_value += weight_x * weight_y * self.image[y1 + n, x1 + m]

                scaled_image[i, j] = interpolated_value.astype(np.uint8)

        return scaled_image
    def bicubic_weight(self, x):
        x = np.abs(x)
        if x <= 1:
            return 1 - 2 * x**2 + x**3
        elif x < 2:
            return 4 - 8 * x + 5 * x**2 - x**3
        else:
            return 0

# img=Interpolate("01.jpg")
# img.show_image()
# img.cal_tot()
# img.intensity_dist()
# img.show_intensity_dist()
# scaled_image = img.nearest_neighbor_interpolation(2.0)
# # scaled_image = img.bilinear_interpolation(2.0)
# # scaled_image = img.bicubic_interpolation(2.0)
# cv2.imshow('Scaled Image', scaled_image)
# cv2.waitKey(0)
