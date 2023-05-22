import numpy as np
import cv2
from tkinter.filedialog import askopenfilename

def GetImagePath():
    return askopenfilename(title='Select The Image', filetypes=(('png files', '*.png'), ('bmp files', '*.bmp'),
                                                                 ('jpeg files', '*.jpeg'), ('jpg files', '*.jpg')))

def ReadImage(Path):
    return cv2.imread(Path, 0)

def SaveImage(Path, Image):
    cv2.imwrite(Path, Image)

def ShowImage(WindowTitle, Image):
    cv2.imshow(f'{WindowTitle}', Image)
    cv2.waitKey(0)

def CreateGaussianKernel(Size, Sigma):
    Kernel = np.fromfunction(lambda x, y: (1 / (2 * np.pi * Sigma ** 2)) * np.exp(-((x - Size // 2) ** 2 + (y - Size // 2) ** 2) / (2 * Sigma ** 2)), (Size, Size))
    return Kernel / np.sum(Kernel)

def ApplyGaussianFilter(OriginalImage):
    GaussianKernel = CreateGaussianKernel(5, 1)
    KernelRadius = GaussianKernel.shape[0] // 2
    FilteredImage = np.zeros_like(OriginalImage)
    PaddedImage = cv2.copyMakeBorder(OriginalImage, KernelRadius, KernelRadius, KernelRadius, KernelRadius,cv2.BORDER_CONSTANT, value=0)
    for r in range(OriginalImage.shape[0]):
        for c in range(OriginalImage.shape[1]):
            PixelSum = 0.0
            WeightSum = 0.0
            for i in range(GaussianKernel.shape[0]):
                for j in range(GaussianKernel.shape[0]):
                    NeighborRow = r + i
                    NeighborCol = c + j
                    PixelSum += PaddedImage[NeighborRow, NeighborCol] * GaussianKernel[i, j]
                    WeightSum += GaussianKernel[i, j]
            FilteredImage[r, c] = PixelSum / WeightSum
    return FilteredImage

# Path = GetImagePath()
# OriginalImage = ReadImage(Path)
# FilteredImage = ApplyGaussianFilter(OriginalImage)
# SaveImage('Output Images\Gaussian Filter.png', FilteredImage)