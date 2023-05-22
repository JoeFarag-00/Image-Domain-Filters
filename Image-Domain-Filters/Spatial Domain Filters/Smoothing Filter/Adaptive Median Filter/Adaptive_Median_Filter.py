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
    cv2.waitKey(0)

def PadImageWithZeros(Image):
    r, c = Image.shape[0], Image.shape[1]
    PaddedImage = numpy.zeros((r + 2, c + 2), dtype=Image.dtype)
    PaddedImage[1:-1, 1:-1] = Image
    return PaddedImage

def Int32ToUint8(List):
    return List.astype(numpy.uint8)

def CalculateMedian(Kernel):
    FlattenedKernel = Kernel.flatten()
    SortedFlattenedKernel = sorted(FlattenedKernel)
    N=len(SortedFlattenedKernel)
    if N % 2 == 0:
         return (SortedFlattenedKernel[N//2 - 1] + SortedFlattenedKernel[N//2]) // 2
    else:
        return SortedFlattenedKernel[N//2]

def CalculateMax(Kernel):
    FlattenedKernel = Kernel.flatten()
    Max = numpy.max(Kernel)
    return Max

def CalculateMin(Kernel):
    FlattenedKernel = Kernel.flatten()
    Min = numpy.min(Kernel)
    return Min

def NumpyIgnoreError():
    numpy.seterr(over='ignore')

def ApplyAdaptiveMedianFilter(PaddedImage, SMax):
    FilteredImage = PaddedImage.copy()
    for i in range(1, PaddedImage.shape[0]-1):
        for j in range(1, PaddedImage.shape[1]-1):
            FilterSize = 3
            while FilterSize <= SMax:
                StartRow = max(0, i - FilterSize // 2)
                EndRow = min(PaddedImage.shape[0] , i + FilterSize // 2 + 1)
                StartColumn = max(0, j - FilterSize // 2)
                EndColumn = min(PaddedImage.shape[1] , j + FilterSize // 2 + 1)
                Kernel = PaddedImage[StartRow:EndRow, StartColumn:EndColumn]

                ZMin = CalculateMin(Kernel)
                ZMax = CalculateMax(Kernel)
                ZMed = CalculateMedian(Kernel)
                Zxy = PaddedImage[i, j]

                A1 = ZMed - ZMin
                A2 = ZMed - ZMax

                if A1 > 0 and A2 < 0:
                    B1 = Zxy - ZMin
                    B2 = Zxy - ZMax

                    if B1 > 0 and B2 < 0:
                        FilteredImage[i, j] = Zxy
                    else:
                        FilteredImage[i, j] = ZMed
                    break
                else:
                    FilterSize += 2

            if FilterSize > SMax:
                FilteredImage[i, j] = ZMed

    return FilteredImage

# NumpyIgnoreError()

# Path = GetImagePath()

# OriginalImage = ReadImage(Path)

# PaddedImage = PadImageWithZeros(OriginalImage)

# SMax = 7

# FilteredImage = ApplyAdaptiveMedianFilter(PaddedImage, SMax)

# FilteredImage = Int32ToUint8(FilteredImage)

# SaveImage('Output Images/Adaptive Median Filter.png', FilteredImage)