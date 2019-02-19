import numpy as np
import matplotlib.pyplot as plt
import argparse
import cv2

alpha, gamma = 0.0, 0.0
beta, img = 0, 0

def ploting(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    plt.subplot(221), plt.imshow(img1), plt.title('Original')
    plt.subplot(222), plt.hist(img1.ravel(), 256, [0, 256]), plt.title('Histograma')
    plt.subplot(223), plt.imshow(img2), plt.title('Modificada')
    plt.subplot(224), plt.hist(img2.ravel(), 256, [0, 256]), plt.title('Histograma 2')

    plt.show()

def gain_bias():
    img_bias = cv2.add((img * alpha), beta)
    img_bias = np.uint8(img_bias)

    ploting(img, img_bias)

def gamma_correction():
    ok = 1/gamma
    img_1 = img/255.0
    img_1 = cv2.pow(img_1, ok)
    img_g = np.uint8(img_1 * 255)

    ploting(img, img_g)

def gain(d):
    global img

    img_x = img.copy()
    h, w, c = img_x.shape

    if d == 0:
        a = 1 - np.arange(0, 1, 1 / h)
    elif d == 1:
        a = 1 - np.arange(0, 1, 1 / w)

    dim_array = np.ones((1, img_x.ndim), int).ravel()
    dim_array[d] = -1
    img_x = np.uint8(img_x * a.reshape(dim_array))

    ploting(img, img_x)


def gain_x():
    gain(1)

def gain_y():
    gain(0)

def negative():
    img_neg = (255 - img)

    ploting(img, img_neg)

def operation(a):
    switcher = {
        "gain_bias": gain_bias,
        "gamma_correction": gamma_correction,
        "gain_x": gain_x,
        "gain_y": gain_y,
        "negative": negative
    }
    func = switcher.get(a, lambda: "Invalid Arguments")

    return func()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True,
                    help = "path to input image")
    ap.add_argument("-o", "--operation", required = True,
                    help = "could be: gain_bias, gamma_correction, gain_x, gain_y or negative")
    ap.add_argument("-a", "--alpha", type=float,
                    help = "alpha (decimal number)")
    ap.add_argument("-b", "--beta", type=int,
                    help = "beta (integer number)")
    ap.add_argument("-g", "--gamma", type=float,
                    help = "gamma (decimal number)")

    arg = ap.parse_args()
    args = vars(arg)

    if arg.operation == "gain_bias" and (arg.alpha is None or arg.beta is None):
        ap.error("--operation: gain_bias requires --alpha and --beta.")
    elif arg.operation == "gamma_correction" and arg.gamma is None:
        ap.error("--operation: gamma_correction requires --gamma.")

    global alpha, beta, gamma, img

    img = cv2.imread(args["image"])

    alpha = args["alpha"]
    beta = args["beta"]
    gamma = args["gamma"]
    operation(args["operation"])

if __name__ == "__main__":
   main()