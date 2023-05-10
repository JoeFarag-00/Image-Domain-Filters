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

def PadImageWithZeros(Image):
    r,c = Image.shape[0],Image.shape[1]
    PaddedImage=numpy.zeros((r + 2, c + 2), dtype=Image.dtype)
    PaddedImage[1:-1,1:-1]=Image
    return PaddedImage

def Int32ToUint8(List):     
    return List.astype(numpy.uint8)

def BlurImage(PaddedImage):
    BlurredImaged=PaddedImage.copy()
    for r in range(1,PaddedImage.shape[0]-1):
        for c in range(1,PaddedImage.shape[1]-1):
            LocalSum = 0
            for i in range(3):
                for j in range(3):
                    LocalSum += PaddedImage[r+i-1, c+j-1]
            LocalMean = LocalSum/9
            BlurredImaged[r,c]=LocalMean
    return BlurredImaged

Path = GetImagePath()

OriginalImage = ReadImage(Path)

PaddedImage = PadImageWithZeros(OriginalImage)

BlurredImage = BlurImage(PaddedImage)

BlurredImage = Int32ToUint8(BlurredImage)

Mask = BlurredImage-PaddedImage

SharpenedImage = Mask + PaddedImage

SaveImage('Project\Spatial Domain Filters\Smoothing\Averaging Filter\Output.png',SharpenedImage)