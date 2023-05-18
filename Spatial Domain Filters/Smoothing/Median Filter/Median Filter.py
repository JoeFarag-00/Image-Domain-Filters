from tkinter.filedialog import askopenfilename
import cv2
import numpy
import math

def GetImagePath():
    return askopenfilename(title = 'Select The Image',filetypes = (('png files', '*.png'), ('bmp files', '*.bmp'), ('jpeg files', '*.jpeg'),('jpg files','*.jpg')))

def ReadImage(Path):
    return cv2.imread(Path,0)

def SaveImage(Path,Image):
    cv2.imwrite(Path,Image)

def ShowImage(WindowTitle,Image):
    cv2.imshow(f'{WindowTitle}',Image)
    cv2.waitKey(0)

def PadImageWithZeros(Image):
    r,c = Image.shape[0],Image.shape[1]
    PaddedImage=numpy.zeros((r + 2, c + 2), dtype=Image.dtype)
    PaddedImage[1:-1,1:-1]=Image
    return PaddedImage

def Int32ToUint8(List):     
    return List.astype(numpy.uint8)

def CalculateMedian(Kernel):
    FlattenedKernel = Kernel.flatten()
    SortedFlattenedKernel = sorted(FlattenedKernel)
    N=len(SortedFlattenedKernel)
    if N % 2 == 0:
        return (SortedFlattenedKernel[N//2 - 1] + SortedFlattenedKernel[N//2]) / 2
    else:
         return SortedFlattenedKernel[N//2]

def BlurImage(PaddedImage):
    BlurredImaged = PaddedImage.copy()
    for r in range(1, PaddedImage.shape[0] - 1):
        for c in range(1, PaddedImage.shape[1] - 1):
            Kernel = PaddedImage[r - 1:r + 2, c - 1:c + 2]
            Median = CalculateMedian(Kernel)
            BlurredImaged[r, c] = Median
    return BlurredImaged

Path = GetImagePath()

OriginalImage = ReadImage(Path)

PaddedImage = PadImageWithZeros(OriginalImage)

BlurredImage = BlurImage(PaddedImage)

BlurredImage = Int32ToUint8(BlurredImage)

# check these steps or should i save the blurredimage

# Mask = BlurredImage-PaddedImage

# SharpenedImage = Mask + PaddedImage

# SaveImage('Project\Spatial Domain Filters\Smoothing\Median Filter\Output.png',SharpenedImage)
