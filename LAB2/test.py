import imutils
import cv2
import numpy as np
import urllib.request as ur
from collections import deque
from matplotlib import pyplot as plt

# R = 114, G = 103, B = 98
conta = [0, 0, 0]
id = 0
pts = deque([])


def quitBackground(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] += 12
    frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    thresh = cv2.threshold(blurred, 125, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow ('T', thresh)
    res = cv2.bitwise_and(frame, frame, mask=thresh)
    return (res)


def passing(r):
    track = pts[r][3]
    end_line = 540

    if len(track) >= 2:
        if pts[r][4][0] == 0:
            if track[-1][0] > end_line and track[-2][0] <= end_line:
                pts[r][4][0] = 1
                return True
        else:
            return False
    else:
        return False


def text(frame):
    global conta

    text_r = "Red:   " + str(conta[0])
    text_g = "Green: " + str(conta[1])
    text_b = "Blue:  " + str(conta[2])

    cv2.putText(frame, text_b, (20, 30), cv2.FONT_HERSHEY_SIMPLEX
                , 1, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, text_g, (20, 60), cv2.FONT_HERSHEY_SIMPLEX
                , 1, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, text_r, (20, 90), cv2.FONT_HERSHEY_SIMPLEX
                , 1, (0, 0, 255), 1, cv2.LINE_AA)
    #cv2.imshow('Frame', frame)
    return frame


def tracking(limits, red_l, frame, ptr, first):
    global conta, id, pts
    frame = text(frame)
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]

    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    for a, cThreshold in enumerate(limits):
        kernel = np.ones((9, 9), np.uint8)

        mask = cv2.inRange(hsv, cThreshold[0], cThreshold[1])
        if a == 0:
            mask_low = cv2.inRange(hsv, red_l[0], red_l[1])
            mask = mask + mask_low

        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        #if a == 0:
         #   cv2.imshow('M', mask)
        #if a == 0:
        cv2.imshow('M'+str(a), mask)
        #if a == 2:
         #   cv2.imshow('M', mask)

        center = None
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        sorted_cnts = sorted(cnts, key=lambda ctr: cv2.boundingRect(ctr)[1])

        for i, c in enumerate(sorted_cnts):

            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            center = (cX, cY)

            if radius > 30:
                cv2.circle(frame, (center), int(radius), colors[a], 2)
                cv2.circle(frame, (center), 8, (0, 0, 0), -1)
                cv2.putText(frame, " ball", (int(x - radius), int(y - radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            colors[a], 2)

                if first:
                    pts.append((1, 0, int(x)))
                else:
                    try:
                        _, num, last = pts.popleft()
                    except:
                        last = 560
                    # cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
                    if int(x) > 540 and last <= 540:
                        if num != 1:
                            conta[a] += 1
                        pts.append((1, 1, cX))
                    elif cX < 540:
                        pts.append((1, 0, cX))

                '''
                w, h, f = 70, 70, 570

                new = True
                if cX in range(0, f + 5):
                    for i in range(len(pts)):
                        if abs(cX - pts[i][1][0]) <= w and abs(cY - pts[i][2][0]) <= h:
                            new = False

                            pts[i][1][0] = cX
                            pts[i][2][0] = cY
                            pts[i][3].append((cX, cY))

                            if passing(i):
                                conta[a] += 1

                            if pts[i][4][0] == 1:
                                if pts[i][1][0] > f:
                                    del pts[i]
                                    print("borrado", len(pts))

                            break
                if new:
                    p = (id, [cX], [cY], deque([(cX, cY)]), [0])
                    pts.append(p)
                    id += 1

            for i in range(len(pts)):
                if len(pts[i][3]) >= 2:
                    ptsr = np.array(pts[i][3], np.int32)
                    ptsr = ptsr.reshape((-1, 1, 2))
                    frame = cv2.polylines(frame, [ptsr], False, colors[a])
                '''


    cv2.line(frame, (540, 0), (540, 480), (200, 200, 0), 2)

    return (frame)


def color_detection_red(frame):
    frame = quitBackground(frame)

    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv1 = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    #cv2.imshow('F', frame)
    color = ('b', 'g', 'r')
    r_range_low, r_range_high = [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]

    k = True

    for channel, col in enumerate(color):

        if k:
            hsv = hsv1[:, :, channel]
            hsv_low = np.where(hsv >= 90, 0, hsv)
            hsv_high = np.where(hsv < 90, 0, hsv)

            med_low = np.sum(hsv_low)
            tot_low = np.count_nonzero(hsv_low)
            stds_low = int(np.std(hsv_low))

            med_high = np.sum(hsv_high)
            tot_high = np.count_nonzero(hsv_high)
            stds_high = int(np.std(hsv_high))

            with np.errstate(divide='ignore'):
                #sa_low = (med_low // tot_low)
                sb_low = (med_low // tot_low)

            a_low = 0 #sa_low - stds_low
            a_high = (med_high // tot_high) - 2 * stds_high
            if a_low < 0: a_low = 0

            b_low = sb_low + stds_low
            b_high = (med_high // tot_high) + 2 * stds_high
            if b_high > 179: b_high = 179

        else:
            hsv = hsv1[:, :, channel]
            hsv_low = hsv

            med_low = np.sum(hsv_low)
            tot_low = np.count_nonzero(hsv_low)
            stds_low = int(np.std(hsv_low))

            a_low = (med_low // tot_low) - 2 * stds_low
            if a_low < 0: a_low = 0
            a_high = a_low

            b_low = (med_low // tot_low) + 2 * stds_low
            if b_low > 255: b_low = 255
            b_high = b_low

        k = False

        r_range_low[0][channel] = int(a_low)
        r_range_low[1][channel] = int(b_low)

        r_range_high[0][channel] = int(a_high)
        r_range_high[1][channel] = int(b_high)

    r_range_low = [tuple(x) for x in r_range_low]
    r_range_high = [tuple(x) for x in r_range_high]
    print("ok")

    #mask_low = cv2.inRange(hsv1, r_range_low[0], r_range_low[1])
    #mask_high = cv2.inRange(hsv1, r_range_high[0], r_range_high[1])
    #mask = mask_low + mask_high
    # res = cv2.bitwise_and(frame, frame, mask=mask)
    #cv2.imshow('mask', mask)
    # cv2.imshow('mask high', mask_high)
    # cv2.imshow('mask', mask)
    # cv2.imshow('res', res)

    return (r_range_low, r_range_high)


def color_detection(frame):
    frame = quitBackground(frame)
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    color = ('b', 'g', 'r')
    c_range = [[0, 0, 0], [0, 0, 0]]
    k = True

    for channel, col in enumerate(color):
        med = np.sum(hsv[:, :, channel])
        tot = np.count_nonzero(hsv[:, :, channel])
        stds = int(np.std(hsv[:, :, channel]))


        if k:
            a = (med // tot) - 2 *stds
            if a < 0: a = 0
            b = (med // tot) + 2 *stds
            if b > 179: b = 179

        else:
            a = (med // tot) - 2 * stds
            if a < 0: a = 0
            b = (med // tot) + 2 * stds
            if b > 255: b = 255

        k = False

        c_range[0][channel] = int(a)  # stds
        c_range[1][channel] = int(b)  # means

    c_range = [tuple(x) for x in c_range]
    print("ok")

    #mask = cv2.inRange(hsv1, c_range[0], c_range[1])
    # res = cv2.bitwise_and(frame, frame, mask=mask)
    #cv2.imshow('mask', mask)
    # cv2.imshow('res', res)
    return (c_range)


def main():
    url = 'http://192.168.43.1:8080/shot.jpg'
    #url = 'http://10.20.33.234:8080/shot.jpg'
    #url = 'http://192.168.0.17:8080/shot.jpg'
    camera = cv2.VideoCapture(1)
    #frame = cv2.imread("Rojos.png")
    #frame = imutils.resize(frame, width=640)
    pts = deque([])
    rThreshold, bThreshold, gThreshold, rThreshold_l = [(166, 84, 141), (186, 255, 255)], [(66, 122, 129),
                                                                                           (86, 255, 255)], \
                                                       [(97, 100, 117), (117, 255, 255)], [(166, 84, 141),
                                                                                           (186, 255, 255)]
    run, first = False, True

    while True:
        #imgResp = ur.urlopen(url)
        #imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        #frame = cv2.imdecode(imgNp, -1)
        _, frame = camera.read()

        if run:
            frame = tracking([rThreshold, gThreshold, bThreshold], rThreshold_l, frame, pts, first)
            first = False

        cv2.imshow('frame', frame)

        k = cv2.waitKey(33)
        if k == 27:
            break
        elif k == 114:
            rThreshold_l, rThreshold = color_detection_red(frame)
        elif k == 98:
            bThreshold = color_detection(frame)
        elif k == 103:
            gThreshold = color_detection(frame)
        elif k == 115:
            run = True

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
