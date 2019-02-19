import cv2
import numpy as np
from matplotlib import pyplot as plt


def ploting(orig, thresh, erosion, dilation):
    plt.subplot(221), plt.imshow(orig), plt.title('Original')
    plt.subplot(222), plt.imshow(thresh, cmap="gray"), plt.title('OTSU')
    plt.subplot(223), plt.imshow(erosion, cmap="gray"), plt.title('Erosion')
    plt.subplot(224), plt.imshow(dilation, cmap="gray"), plt.title('Dilation')

    plt.show()


def dilate(dilation, struc):
    dilation = dilation.copy() / 255
    rows, cols = dilation.shape
    x, y = struc.shape

    box = np.pad(dilation, pad_width=2, mode='constant', constant_values=0)
    for r in range(rows):
        for c in range(cols):
            dilation[r, c] = np.max(box[r:r + x, c:c + y] * [struc])

    return dilation


def erode(erosion, struc):
    erosion = erosion.copy() / 255
    rows, cols = erosion.shape
    x, y = struc.shape
    '''
    box = np.ones((rows + x - 1, cols + y - 1), np.uint8)
    box[2:rows + 2, 2:cols + 2] = input
    '''
    box = np.pad(erosion, pad_width=2, mode='constant', constant_values=0)
    for r in range(rows):
        for c in range(cols):
            erosion[r, c] = (struc == (box[r:r + x, c:c + y] * [struc])).all()

    return erosion


def main():
    img = cv2.imread("MasterChief.jpg")
    orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    structure = np.array([[0, 1, 1, 1, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0]], np.uint8)

    erosion = erode(thresh, structure)
    dilation = dilate(thresh, structure)
    ploting(orig, thresh, erosion, dilation)


if __name__ == "__main__":
    main()
