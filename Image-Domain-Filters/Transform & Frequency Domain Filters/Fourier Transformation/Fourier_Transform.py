import cv2
import numpy as np
import matplotlib.pyplot as plt
class Fourier:
 
    def Shift(self,Path):
        self.Path = Path
        self.Image_List = cv2.imread(self.Path, cv2.IMREAD_GRAYSCALE)
        self.Fourier_List = np.zeros_like(self.Image_List, dtype = np.complex64)
        for Frequency_Row in range(self.Image_List.shape[0]):
            for Frequency_Column in range(self.Image_List.shape[1]):
                for Spatial_Row in range(self.Image_List.shape[0]):
                    for Spatial_Column in range(self.Image_List.shape[1]):
                        self.Fourier_List[Frequency_Row, Frequency_Column] += self.Image_List[Spatial_Row, Spatial_Column] * np.exp(-2j * np.pi * (Frequency_Row * Spatial_Row / self.Image_List.shape[0] + Frequency_Column * Spatial_Column / self.Image_List.shape[1]))
    
        shift_rows = (self.Fourier_List.shape[0] + 1) // 2
        shift_cols = (self.Fourier_List.shape[1] + 1) // 2
        self.Fourier_Shifted = np.empty_like(self.Fourier_List)
        self.Fourier_Shifted[:shift_rows, :shift_cols] = self.Fourier_List[-shift_rows:, -shift_cols:]
        self.Fourier_Shifted[:shift_rows, shift_cols:] = self.Fourier_List[-shift_rows:, :-shift_cols]
        self.Fourier_Shifted[shift_rows:, :shift_cols] = self.Fourier_List[:-shift_rows, -shift_cols:]
        self.Fourier_Shifted[shift_rows:, shift_cols:] = self.Fourier_List[:-shift_rows, :-shift_cols]
        
        self.Magnitude_Spectrum = np.log(1 + np.abs(self.Fourier_Shifted))
        return self.Magnitude_Spectrum
    
    
    def Inverse_Fourier(self,Path):
        self.Path = Path
        self.Image_List = cv2.imread(self.Path, cv2.IMREAD_GRAYSCALE)
        self.Fourier_List = np.zeros_like(self.Image_List, dtype = np.complex64)
        for Frequency_Row in range(self.Image_List.shape[0]):
            for Frequency_Column in range(self.Image_List.shape[1]):
                for Spatial_Row in range(self.Image_List.shape[0]):
                    for Spatial_Column in range(self.Image_List.shape[1]):
                        self.Fourier_List[Frequency_Row, Frequency_Column] += self.Image_List[Spatial_Row, Spatial_Column] * np.exp(-2j * np.pi * (Frequency_Row * Spatial_Row / self.Image_List.shape[0] + Frequency_Column * Spatial_Column / self.Image_List.shape[1]))
    
        shift_rows = (self.Fourier_List.shape[0] + 1) // 2
        shift_cols = (self.Fourier_List.shape[1] + 1) // 2
        self.Fourier_Shifted = np.empty_like(self.Fourier_List)
        self.Fourier_Shifted[:shift_rows, :shift_cols] = self.Fourier_List[-shift_rows:, -shift_cols:]
        self.Fourier_Shifted[:shift_rows, shift_cols:] = self.Fourier_List[-shift_rows:, :-shift_cols]
        self.Fourier_Shifted[shift_rows:, :shift_cols] = self.Fourier_List[:-shift_rows, -shift_cols:]
        self.Fourier_Shifted[shift_rows:, shift_cols:] = self.Fourier_List[:-shift_rows, :-shift_cols]
        
        self.Magnitude_Spectrum = np.log(1 + np.abs(self.Fourier_Shifted))
        self.Inverse_Fourier_Shifted = np.zeros_like(self.Fourier_Shifted, dtype = np.complex64)
        for Spatial_Row in range(self.Image_List.shape[0]):
            for Spatial_Column in range(self.Image_List.shape[1]):
                self.Inverse_Sum = 0
                for Frequency_Row in range(self.Image_List.shape[0]):
                    for Frequency_Column in range(self.Image_List.shape[1]):
                        self.Inverse_Sum += self.Fourier_Shifted[Frequency_Row, Frequency_Column] * np.exp(2j * np.pi * (Frequency_Row * Spatial_Row / self.Image_List.shape[0] + Frequency_Column * Spatial_Column / self.Image_List.shape[1]))
                self.Inverse_Fourier_Shifted[Spatial_Row, Spatial_Column] = self.Inverse_Sum

        self.Magnitude = np.abs(self.Inverse_Fourier_Shifted)
        self.Magnitude_Normalized = (self.Magnitude - self.Magnitude.min()) / (self.Magnitude.max() - self.Magnitude.min())
        self.Inverse_Fourier_Uint8 = (self.Magnitude_Normalized * 255)
        # print(type(self.Inverse_Fourier_Uint8))
        self.Inverse_Fourier_Uint8 = np.array(self.Inverse_Fourier_Uint8)
        return self.Inverse_Fourier_Uint8

    def Show_Image(self):
        fig, axes = plt.subplots(1, 3, figsize=(4 * 3, 4))

        # Plot each image in its respective subplot
        axes[0].imshow(self.Image_List, cmap='gray')
        axes[0].set_title('Original Image')
        axes[0].axis('off')

        axes[1].imshow(self.Magnitude_Spectrum, cmap='gray')
        axes[1].set_title('Fourier')
        axes[1].axis('off')

        axes[2].imshow(self.Inverse_Fourier_Uint8, cmap='gray')
        axes[2].set_title('Inverse Fourier')
        axes[2].axis('off')
        
        plt.show()

#     def Show_Image(self):
#         plt.figure(figsize=(4 * 3, 4))
#         plt.subplot(1, 3, 1)
#         plt.imshow(self.Image_List, cmap='gray')
#         plt.title('Original Image')
#         plt.axis('off')

#         plt.subplot(1, 3, 2)
#         plt.imshow(self.Magnitude_Spectrum, cmap='gray')
#         plt.title('Fourier')
#         plt.axis('off')

#         plt.subplot(1, 3, 3)
#         plt.imshow(self.Inverse_Fourier_Uint8, cmap='gray')
#         plt.title('Inverse Fourier')
#         plt.axis('off')

# Path = 'Image-Domain-Filters/Transform & Frequency Domain Filters/Fourier Transformation/07.jpg'
# Main = Fourier(Path)
# Main.Read_Image()
# Main.Start_Fourier()
# Main.Shift()
# Main.Inverse_Fourier()
# Main.Show_Image()