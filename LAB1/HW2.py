import numpy as np
import matplotlib.pyplot as plt
import argparse
import cv2

img1, img2 = 0, 0
alpha = 0.0

def ploting(img, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img), plt.title(title)
    plt.show()

def normal_blend():
    global img1, img2, alpha

    alpha2 = 1 - alpha
    img1 = (img1 * alpha2)
    img2 = (img2 * alpha)

    img_blend = np.uint8(img1 + img2)

    title = 'Blend Normal'
    ploting(img_blend, title)

def blend(d, title):
    global img1, img2
    h, w, c = img1.shape

    if d == 0:
        b2 = np.arange(0, 1, 1 / h)
    elif d == 1:
        b2 = np.arange(0, 1, 1 / w)

    b1 = 1 - b2
    dim_1 = np.ones((1, img1.ndim), int).ravel()
    dim_2 = np.ones((1, img2.ndim), int).ravel()
    dim_1[d] = -1
    dim_2[d] = -1

    img1 = np.uint8(img1 * b1.reshape(dim_1))
    img2 = np.uint8(img2 * b2.reshape(dim_2))
    img_blend = np.uint8(img1 + img2)
    ploting(img_blend, title)

def x_blend():
    title = 'Blend en X'
    blend(1, title)

def y_blend():
    title = 'Blend en Y'
    blend(0, title)

def operation(a):
    switcher = {
        "normal_blend": normal_blend,
        "x_blend": x_blend,
        "y_blend": y_blend
    }
    func = switcher.get(a, lambda: "Invalid Argument")

    return func()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image1", required = True,
                    help = "path to input image 1")
    ap.add_argument("-j", "--image2", required = True,
                    help = "path to input image 2")
    ap.add_argument("-o", "--operation", required = True,
                    help = "could be: normal_blend, x_blend or y_blend")
    ap.add_argument("-a", "--alpha", type = float,
                    help = "alpha (decimal number)")

    arg = ap.parse_args()
    args = vars(arg)

    if arg.operation == "normal_blend" and arg.alpha is None:
        ap.error("--operation: gain_bias requires --alpha.")

    global alpha, img1, img2

    img1 = cv2.imread(args["image1"])
    img2 = cv2.imread(args["image2"])

    img1 = cv2.resize(img1, (600, 450))

    alpha = args["alpha"]
    operation(args["operation"])

if __name__ == "__main__":
   main()