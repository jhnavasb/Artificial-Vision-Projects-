import numpy as np
import imutils
import cv2
from matplotlib import pyplot as plt
import re
import argparse

answers = {0: 1, 1: 2, 2: 0, 3: 3, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}
results = np.zeros((10,), dtype=int)
correct = np.zeros((10,), dtype=int)
cross_n, coord = [], []

def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left

    rect = np.zeros((4, 2), dtype="float32")

    so = sorted(pts, key=lambda x: x[1])

    if so[0][0] < so[1][0]:
        rect[0] = so[0]
        rect[1] = so[1]
    else:
        rect[0] = so[1]
        rect[1] = so[0]

    if so[2][0] < so[3][0]:
        rect[2] = so[3]
        rect[3] = so[2]
    else:
        rect[2] = so[2]
        rect[3] = so[3]

    return rect


def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped


def grade(questionCnts, thresh, n):
    global answers, results, correct

    boundingBoxes = [cv2.boundingRect(c) for c in questionCnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(questionCnts, boundingBoxes),
                                        key=lambda b: b[1][1], reverse=False))  # ab 1
    #correct = 0

    for (q, i) in enumerate(np.arange(0, len(cnts), 4)):
        boundingBoxes = [cv2.boundingRect(c) for c in questionCnts[i:i + 4]]
        (cnts, boundingBoxes) = zip(*sorted(zip(questionCnts[i:i + 4], boundingBoxes),
                                            key=lambda b: b[1][0], reverse=False))

        bubbled, idiot = 4, -1

        for (j, c) in enumerate(cnts):
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)

            mask = cv2.bitwise_and(thresh, thresh, mask=mask)
            total = cv2.countNonZero(mask)

            #cv2.imshow('try', mask)
            #cv2.waitKey(0)
            #print(total)
            if total > 500:
                bubbled = j
                idiot += 1
            #if bubbled is None or total > bubbled[0]:
            #    bubbled = (total, j)

        k = answers[n - q]
        # check to see if the bubbled answer is correct
        if bubbled == 4 or idiot > 0:
            results[n - q] = 4
        else:
            if k == bubbled:
                correct[n - q] = 1
                results[n - q] = k
            else:
                results[n - q] = bubbled


def bubble(paper, n):
    width, height = paper.shape
    width_cutoff = width
    if n == 4:
        img = paper[:, :width_cutoff]
    else:
        img = paper[:, width_cutoff:]

    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = np.ones((5, 5), np.uint8)
    kernel1 = np.ones((3, 3), np.uint8)
    kernel2 = np.zeros((3, 3), np.uint8)

    thresh = cv2.dilate(thresh, kernel2, iterations = 2)
    thresh = cv2.erode(thresh, kernel2, iterations = 2)
    thresh = cv2.dilate(thresh, kernel2, iterations = 3)
    #thresh = cv2.erode(thresh, kernel2, iterations = 1)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    questionCnts = []

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)

        if w <= 80 and h <= 80 and w >= 22 and h >= 22 and ar >= 0.5 and ar <= 1.5:
            questionCnts.append(c)

    #cv2.drawContours(paper, questionCnts, -1, 255, 3)
    #cv2.imshow('Ok', paper)
    #cv2.imshow('Ok1', thresh)
    #cv2.waitKey(0)

    grade(questionCnts, thresh, n)


def rotate_image(mat, angle):
    try:
        height, width, a = mat.shape
    except:
        height, width = mat.shape

    image_center = (width/2, height/2)
    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    abs_cos = abs(rotation_mat[0,0])
    abs_sin = abs(rotation_mat[0,1])

    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat


def final():
    global answers, results, correct
    key = ["A", "B", "C", "D", "NOT_VALID", "FAIL", "OK"]

    #print("Checking the exam: \n")
    for i, a in enumerate(results):
        #print(i + 1, ". Answer: ", key[results[i]], ", Correct: ", key[answers[i]], ",", key[correct[i] + 5])
        print("%d. Answer: %s, Correct: %s, %s" % (i + 1, key[results[i]], key[answers[i]], key[correct[i] + 5]))

    total = np.sum(correct)
    print("\nScore: %d/10 = %.2f" % (total, total * 5 / 10))


def read(file):
    global answers
    key = ["A", "B", "C", "D"]
    filename = file

    with open(filename) as f:
        data = f.readlines()

    for i in range(len(data)):
        answers[i] = key.index(re.findall(r'[A-Za-z]+|\d+', data[i])[1])


def cross_rotation(cross, angle, val, k):

    rows, cols = cross.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, k)
    new_cross = cv2.warpAffine(cross, M, (cols, rows))
    #new_cross[new_cross == 0] = val

    #cv2.imshow("Try", new_cross)
    #cv2.waitKey(0)
    return new_cross


def orientation1(img, img1):
    ok = True
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    #img1 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    width, height = img.shape
    width_cutoff = width // 3
    height_cutoff = height // 7
    img = img[:height_cutoff, :width_cutoff]

    imgF1 = img.copy()
    res = cv2.matchTemplate(imgF1, img1, cv2.TM_CCOEFF_NORMED)

    threshold = 0.7
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        #print("si esta")
        ok = False
    #cv2.imshow("vaia", imgF1)
    #cv2.imshow("vaiaa", img1)
    #cv2.waitKey(0)
    return ok


def cross_finder(img, temp, img1):
    global cross_n, coord
    w, h = temp.shape[::-1]
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)

    threshold = 0.7
    loc = np.where(res >= threshold)

    x, y = 0, 0
    t = True
    s = img1.copy()

    for pt in zip(*loc[::-1]):
        l = (pt[0] + w, pt[1] + h)
        cv2.rectangle(s, pt, l, (0, 0, 255), 1)

        if t:
            x = pt[0]
            y = pt[1]

        if (np.abs(x - pt[0]) > 1 and np.abs(y - pt[1]) > 10) or (
                np.abs(x - pt[0]) > 10 and np.abs(y - pt[1]) > 1) or t:
            k = [pt, (pt[0] + w, pt[1]), (pt[0], pt[1] + h), (pt[0] + w, pt[1] + h)]
            k = np.asarray(k)
            length = k.shape[0]
            sum_x = np.sum(k[:, 0])
            sum_y = np.sum(k[:, 1])
            coord.append([sum_x / length, sum_y / length])

            bottom_right = (pt[0] + w, pt[1] + h)
            cross_n.append([pt, bottom_right])
            x = pt[0]
            y = pt[1]
            t = False
        else:
            t = False

    #cv2.imshow("Try", s)
    #cv2.waitKey(0)


def foo(x, y):
    #return int((x + 20) / 20) * 20, int((y + 20) / 20) * 20
    #return round(x,-1), round(y,-1)
    return int(np.ceil(int(x) / 10.0)) * 10, int(np.ceil(int(y) / 10.0)) * 10


def operation(img):
    global cross_n, coord
    print("Checking the exam: \n")

    #ix, iy, _ = img.shape
    #img = cv2.resize(img, (int(iy/1.5), int(ix/1.5)))

    magic = cv2.imread("superA.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (1, 1), 0)

    #plt.imshow(blurred, cmap="gray")
    #plt.show()

    #thresh1 = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)[1]
    #thresh2 = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY)[1]
    #thresh = thresh2 - thresh1
    thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY_INV )[1]
    temp = []
    maxi = [0.8, 1, 1.1, 1.2, 1.5]

    #cv2.imshow('Ok1', thresh)
    #cv2.waitKey(0)

    temp.append(cv2.imread("cruzprofe.png", 0))
    temp.append(cv2.imread("crossT4.png", 0))
    temp.append(cv2.imread("crossT1.png", 0))
    #temp.append(cv2.imread("crossT7.png", 0))
    temp.append(cv2.imread("crossT2.png", 0))
    temp.append(cv2.imread("crossT5.png", 0))
    temp.append(cv2.imread("crossT6.png", 0))
    #temp.append(cv2.imread("crossT8.png", 0))
    #temp.append(cv2.imread("crossT9.png", 0))

    #tempi = cv2.cvtColor(temp[0], cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(temp[0], (3, 3), 0)
    #tempi = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    w, h = temp[0].shape
    k = np.sum(temp[0][:, 21:])
    val = k // (2 * h)
    #cv2.imshow("temp", thresh)
    #cv2.waitKey(0)

    print("It could take a while... \n")

    for a in range(0, 360, 30):
        for b in range(0, 6):
            for c in range(0, 5):
                blurred = cv2.GaussianBlur(temp[b], (1, 1), 0)
                tempi = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
                #tempi = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)[1]
                #tempi = temp[b]
                cross_finder(thresh, cross_rotation(tempi, a, val, maxi[c]), gray)

    imgk = img.copy()
    for i, a in enumerate(cross_n):
        cv2.rectangle(imgk, a[0], a[1], 255, 3)

    #cv2.imshow('Ok1', thresh)

    cv2.imshow('Ok', imgk)
    cv2.waitKey(0)
    '''
    '''

    seen = set()
    rr = np.asarray(coord)
    rr = [foo(x, y) for x, y in rr]

    newlist, nn = [], []
    for i, item in enumerate(rr):
        t = tuple(item)
        if t not in seen:
            nn.append(coord[i])
            seen.add(t)

    x, y, t  = 0, 0, True

    nn = sorted(nn, key=lambda x: x[0], reverse=True)
    for pt in (nn):
        if t:
            x = pt[0]
            y = pt[1]

        if (np.abs(x - pt[0]) > 0.5 and np.abs(y - pt[1]) > 10) or (
                np.abs(x - pt[0]) > 10 and np.abs(y - pt[1]) > 0.5) or t:
            newlist.append(pt)
            x = pt[0]
            y = pt[1]
            t = False


    if len(newlist) != 4:
        arr = np.asarray(newlist)
        length = arr.shape[0]
        sum_x = np.sum(arr[:, 0])
        sum_y = np.sum(arr[:, 1])
        k = sum_x / length, sum_y / length

        distance = []
        for s in arr:
            dist = np.sqrt(((s[0] - k[0]) ** 2) + ((s[1] - k[1]) ** 2))
            distance.append([dist, s])

        so = sorted(distance, key=lambda x: x[0], reverse=True)
        coo = np.array([so[0][1], so[1][1], so[2][1], so[3][1]])
    else:
        coo = np.asarray(newlist)

    paper = four_point_transform(img, coo.reshape(4, 2))

    #for i, a in enumerate(newlist):
    #    print(a)
    #    cv2.rectangle(img, a[0], a[1], 255, 3)

    #cv2.imshow("Try", img)
    #cv2.waitKey(0)
    #for a in range(10, 360, 10):
    #    cross_rotation(temp, a, val)

    rows, cols, _ = paper.shape
    if rows > cols:
        # img = imutils.rotate_bound(img, 180)
        paper = rotate_image(paper, 90)
    # paper = rotate_image(paper, 180)


    paper1 = cv2.cvtColor(paper, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (9, 9), 0)
    #edged = cv2.Canny(blurred, 70, 180)
    paper = cv2.resize(paper1, (800, 450))
    tR = orientation1(paper, magic)
    # orientation1(paper, magic)

    if tR:
        paper = rotate_image(paper, 180)


    #cv2.imshow('Ok', paper)
    #cv2.imshow('Ok1', paper)
    #cv2.waitKey(0)

    bubble(paper, 4)
    bubble(paper, 9)
    final()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--answers", required = True,
                    help = "path to answers file")
    ap.add_argument("-i", "--image", required = True,
                    help = "path to exam image")

    args = vars(ap.parse_args())

    read(args["answers"])
    img = cv2.imread(args["image"])
    operation(img.copy())


if __name__ == "__main__":
   main()