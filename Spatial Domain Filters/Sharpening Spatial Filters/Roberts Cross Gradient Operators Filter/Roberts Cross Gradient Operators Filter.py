from tkinter.filedialog import askopenfilename
import cv2
import numpy

def GetImagePath():
    return askopenfilename(title='Select The Image', filetypes=(('png files', '*.png'), ('bmp files', '*.bmp'), ('jpeg files', '*.jpeg'), ('jpg files', '*.jpg')))

def ReadImage(Path):
    return cv2.imread(Path, 0)

def SaveImage(Path, Image):
    cv2.imwrite(Path, Image)

def ShowImage(WindowTitle, Image):
    cv2.imshow(f'{WindowTitle}', Image)

def WaitKey():
    cv2.waitKey(0)

def ApplyRobertsCrossGradientOperatorsFilter(OriginalImage):
    Gx = numpy.array([[1,0],[0,-1]])
    Gy = numpy.array ([[0,1],[-1,0]])
    PaddedImage = cv2.copyMakeBorder(OriginalImage, 1, 1, 1, 1, cv2.BORDER_REFLECT)
    FilteredImage = numpy.zeros_like(OriginalImage)
    for r in range(OriginalImage.shape[0] - 1):
        for c in range(OriginalImage.shape[1] - 1):
            GxResponse = numpy.sum( PaddedImage[r:r+2, c:c+2] * Gx)
            GyResponse = numpy.sum( PaddedImage[r:r+2, c:c+2] * Gy)
            GradientMagnitude = numpy.sqrt( GxResponse**2 + GyResponse**2) 
            GradientMagnitude=numpy.clip(GradientMagnitude, 0, 255)
            FilteredImage[r, c] = GradientMagnitude
    return FilteredImage

Path = GetImagePath()

OriginalImage = ReadImage(Path)

FilteredImage = ApplyRobertsCrossGradientOperatorsFilter(OriginalImage)

SaveImage('Output Images/Roberts Cross Gradient Operators Filter.png', FilteredImage)