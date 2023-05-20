import numpy
import cv2
from tkinter.filedialog import askopenfilename

def GetImagePath():
    return askopenfilename(title='Select The Image', filetypes=(('png files', '*.png'), ('bmp files', '*.bmp'),('jpeg files', '*.jpeg'), ('jpg files', '*.jpg')))

def ReadImage(Path):
    return cv2.imread(Path, 0)

def SaveImage(Path, Image):
    cv2.imwrite(Path, Image)

def ShowImage(WindowTitle, Image):
    cv2.imshow(f'{WindowTitle}', Image)
    cv2.waitKey(0)

def Int32ToUint8(List):     
    return List.astype(numpy.uint8)

def CreateGaussianKernel(Size, Sigma):
    Kernel = numpy.fromfunction(lambda x, y: (1 / (2 * numpy.pi * Sigma ** 2)) * numpy.exp(-((x - Size // 2) ** 2 + (y - Size // 2) ** 2) / (2 * Sigma ** 2)), (Size, Size))
    return Kernel / numpy.sum(Kernel)

def ApplyGaussianFilter(OriginalImage):
    GaussianKernel = CreateGaussianKernel(5, 1)
    KernelRadius = GaussianKernel.shape[0] // 2
    FilteredImage = numpy.zeros_like(OriginalImage)
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

def ApplyUnsharpMaskingAndHighboostFilteringFilter(OriginalImage, K):
    FilteredImage = ApplyGaussianFilter(OriginalImage)
    FilteredImage = Int32ToUint8(FilteredImage)
    Mask = OriginalImage - FilteredImage
    SharpenedImage = OriginalImage + K * Mask
    return SharpenedImage

Path = GetImagePath()

OriginalImage = ReadImage(Path)

K=int(input('Enter Weight Of The Mask:'))

if  K>=0:
    SharpenedImage = ApplyUnsharpMaskingAndHighboostFilteringFilter(OriginalImage,K)
else:
    SharpenedImage = OriginalImage

SaveImage(r'Output Images\Unsharp Masking and Highboost Filtering Using Gaussian Filter.png',SharpenedImage)