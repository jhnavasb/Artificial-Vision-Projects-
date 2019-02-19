import numpy as np
import imutils
import cv2
from matplotlib import pyplot as plt
import re
import argparse

answers = {0: 1, 1: 2, 2: 0, 3: 3, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}
results = np.zeros((10,), dtype=int)
correct = np.zeros((10,), dtype=int)

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

    '''
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    pts = np.delete(pts, [np.argmin(s), np.argmax(s)], 0)

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    '''
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


def getC(img):
    cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    docCnt = None

    if len(cnts) > 0:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            if len(approx) == 4:
                docCnt = approx
                break
    return docCnt


def grade(questionCnts, thresh, n):
    global answers, results, correct
    key = ["A", "B", "C", "D", "NOT_VALID"]

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
            if total > 400:
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
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    questionCnts = []

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)

        if w <= 40 and h <= 40 and w >= 19 and h >= 19 and ar >= 0.5 and ar <= 1.5:
            questionCnts.append(c)

    cv2.drawContours(paper, questionCnts, -1, 255, 3)

    cv2.imshow('Ok', paper)
    cv2.imshow('Ok1', thresh)
    cv2.waitKey(0)

    grade(questionCnts, thresh, n)


def crux(img):
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cruxCnts = []
    k = []

    a = 0
    for c in cnts:
        M = cv2.moments(c)
        if cv2.contourArea(c) > 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)

            if w >= 9 and h >= 9 and ar >= 0 and ar <= 11:
                cruxCnts.append([cX, cY])
                k.append(c)
                a += 1
                if a == 2:
                    break

    cnts = sorted(cnts, key=lambda ctr: cv2.boundingRect(ctr)[1])
    for c in cnts:
        M = cv2.moments(c)
        if cv2.contourArea(c) > 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)

            if w >= 9 and h >= 9 and ar >= 0 and ar <= 11:
                cruxCnts.append([cX, cY])
                k.append(c)
                a += 1

                if a == 4:
                    break


    #cv2.drawContours(img, k, -1, (0, 255, 0), 3)
    #cv2.imshow('Ok', img)
    #cv2.waitKey(0)
    return cruxCnts


def forcito(cnts, k):
    cruxCnts = None
    cruxC = 0

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)
        rect = cv2.minAreaRect(c)
        center, w_h, angle = rect
        w = w_h[0]
        h = w_h[1]
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        if h != 0:
            ar = w / float(h)
        else:
            ar = 20
        #hull = cv2.convexHull(c)
        #if w <= 20 and h <= 20 and ar >= 0.5 and ar <= 1.8:
        #    cruxCnts = box

        #if len(approx) < 24 and len(approx) > 8:
        #    cruxCnts = approx
        #if w <= 20 and h <= 20 and ar >= 0.5 and ar <= 1.8:
            #cruxCnts = box
        if len(approx) < 30 and len(approx) > 8:
            # cruxCnts = box
            t = True
            if w >= 4.7 and h >= 4.7:
                for a in k:
                    try:
                        if box[0][1] == a[0][1] and box[0][0] == a[0][0]:
                            t = False
                    except:
                        pass
                if t:
                    cruxCnts = box
                    cruxC = center
                    break

    return cruxCnts, cruxC

def crux1(img):
    cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cruxCnts = []
    cruxC = []

    if len(cnts) > 0:
        boundingBoxes = [cv2.boundingRect(c) for c in cnts]
        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][1], reverse=False)) #ab 1
        cn, cr = forcito(cnts, cruxCnts)
        cruxCnts.append(cn)
        cruxC.append(cr)

        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][0], reverse=False)) #id

        cn, cr = forcito(cnts, cruxCnts)
        cruxCnts.append(cn)
        cruxC.append(cr)

        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][1], reverse=True)) #ba 1

        cn, cr = forcito(cnts, cruxCnts)
        cruxCnts.append(cn)
        cruxC.append(cr)

        (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                            key=lambda b: b[1][0], reverse=True)) #di

        cn, cr = forcito(cnts, cruxCnts)
        cruxCnts.append(cn)
        cruxC.append(cr)


    return cruxCnts, cruxC
    #cv2.drawContours(img1, cruxCnts, -1, (0, 255, 0), 2)
    #cv2.imshow('Ok', img1)
    #cv2.waitKey(0)

def rotate_image(mat, angle):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """
    try:
        height, width, a = mat.shape
    except:
        height, width = mat.shape

    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0])
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat


def cross_magic(img):
    temp = cv2.imread("crossT.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

    w, h = temp.shape[::-1]
    res = cv2.matchTemplate(gray, temp, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where(res >= threshold)

    num_largest = 4
    indices = (-res).argpartition(num_largest, axis=None)[:num_largest]
    ss = np.unravel_index(indices, res.shape)
    ks = np.asarray(ss).reshape(2, 4)

    x = 0
    t = True
    coord = []
    s = img.copy()
    for pt in zip(*loc[::-1]):
        l = (pt[0] + w, pt[1] + h)
        cv2.rectangle(s, pt, l, (0, 0, 255), 1)

        if t:
            x = pt[0]

        if np.abs(x - pt[0]) > 2 or t:
            k = [pt, (pt[0] + w, pt[1]), (pt[0], pt[1] + h), (pt[0] + w, pt[1] + h)]
            k = np.asarray(k)
            length = k.shape[0]
            sum_x = np.sum(k[:, 0])
            sum_y = np.sum(k[:, 1])
            coord.append([sum_x / length, sum_y / length])
            x = pt[0]
            t = False
        else:
            t = False

    #print(coord)
    #cv2.imshow("Try", s)
    #cv2.waitKey(0)

    return coord

def orientation1(img, img1):
    ok = True
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    #img1 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    w, h = img1.shape[::-1]

    width, height = img.shape
    width_cutoff = width // 2
    height_cutoff = height // 9
    img = img[:height_cutoff, :width_cutoff]

    imgF1 = img.copy()
    res = cv2.matchTemplate(imgF1, img1, cv2.TM_SQDIFF_NORMED)
    min, max, top_left, _ = cv2.minMaxLoc(res)
    if min < 0.025:
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(imgF1, top_left, bottom_right, 0, 2)
        #plt.imshow(res, cmap='gray')
        #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        #plt.show()
        ok = False
    #cv2.imshow("vaia", imgF1)
    #cv2.imshow("vaiaa", img1)
    #cv2.waitKey(0)
    return ok


def final():
    global answers, results, correct
    key = ["A", "B", "C", "D", "NOT_VALID", "FAIL", "OK"]

    print("Checking the exam: \n")
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


def operation(img):
    #img = cv2.imread("Captura.png")
    #img = cv2.imread("im11.jpeg")
    #img = cv2.imread("im16.jpg")
    #x, y, a = img.shape
    #img = cv2.resize(img, (y//4, x//4))
    magic = cv2.imread("Amagica.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)

    #thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]
    #cv2.imshow('T', img)
    #res = cv2.bitwise_and(img, img, mask=thresh)
    #cv2.imshow('1T', res)

    edged = cv2.Canny(blurred, 70, 160)
    #cv2.imshow('T', edged)
    work = True

    coord = cross_magic(img)
    if len(coord) != 4:
        cruxCnts, cruxC = crux1(edged.copy())
        try:
            cv2.drawContours(img, cruxCnts, -1, (0, 255, 0), 2)
            #cv2.imshow('Ok1', edged)
            #cv2.imshow('Ok', img)
            #cv2.waitKey(0)
        except:
            work = False
    else:
        cruxC = coord

    if work:
        paper = four_point_transform(gray, np.asarray(cruxC).reshape(4, 2))
        #cv2.imshow('Ok', paper)
        #cv2.waitKey(0)
    else:
        docCnt = getC(edged)
        paper = four_point_transform(gray, docCnt.reshape(4, 2))
        cruxCnt = np.asarray(crux(paper))
        paper = four_point_transform(paper, cruxCnt.reshape(4, 2))

    #thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    #docCnt = getC(edged)
    #paper = four_point_transform(gray, docCnt.reshape(4, 2))
    #cruxCnt = np.asarray(crux(paper))
    #paper = four_point_transform(paper, cruxCnt.reshape(4, 2))

    rows, cols = paper.shape
    if rows > cols:
        #img = imutils.rotate_bound(img, 180)
        paper = rotate_image(paper, 90)
    #paper = rotate_image(paper, 180)

    #cv2.imshow('Ok', paper)
    #cv2.waitKey(0)

    blurred = cv2.GaussianBlur(paper, (9, 9), 0)
    edged = cv2.Canny(blurred, 70, 180)
    tR = orientation1(paper, magic)
    #orientation1(paper, magic)

    if tR:
        paper = rotate_image(paper, 180)
    paper = cv2.resize(paper, (800, 450))

    bubble(paper, 4)
    bubble(paper, 9)
    final()

    #paper = cv2.resize(paper, (800, 450))
    #cv2.imshow('Ok', paper)
    #cv2.waitKey(0)

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