import cv2
import numpy as np
import matplotlib.pyplot as plt
class Histo_Equa:

    def Histogram_Equalization(self,Path):
        self.Image_List = cv2.imread(Path, cv2.IMREAD_GRAYSCALE)
        self.Nk = np.zeros(256, dtype = int)
        for Row in range(self.Image_List.shape[0]):
            for Column in range(self.Image_List.shape[1]):
                self.Nk[self.Image_List[Row, Column]] += 1

        self.Total = 0
        self.CDF = []
        for i in self.Nk:
            self.Total += i
            self.CDF.append(self.Total)
        
        self.CDF_Normalized = [0] * 256
        self.CDF_Normalized[0] = self.CDF[0]
        for i in range(1, 256):
            self.CDF_Normalized[i] = (self.CDF[i] * 255) // self.Total

        self.Equalized_Image = [[0] * len(row) for row in self.Image_List]
        for i in range(len(self.Image_List)):
            for j in range(len(self.Image_List[i])):
                self.Equalized_Image[i][j] = self.CDF_Normalized[self.Image_List[i][j]]
                
        # self.Equalized_Image = np.uint8(self.Equalized_Image)
        # self.Equalized_Image = np.array(self.Image_List)
        # self.Show_Image(self.Equalized_Image, "Equalized Image")
        self.Equalized_Image = np.array(self.Equalized_Image)
        return self.Equalized_Image

    # def Show_Image(self, Image, Text):
    #     plt.title(Text)
    #     plt.imshow(Image, cmap='gray')
    #     plt.axis('off')
    #     plt.show()