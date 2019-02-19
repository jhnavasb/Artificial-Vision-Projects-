from connect4 import *

from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
from primesense import openni2
import serial
import time
#import freenect


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


def get_video(color_stream):

    cframe = color_stream.read_frame()
    cframe_data = np.array(cframe.get_buffer_as_triplet()).reshape([480, 640, 3])
    R = cframe_data[:, :, 0]
    G = cframe_data[:, :, 1]
    B = cframe_data[:, :, 2]
    cframe_data = np.transpose(np.array([B, G, R]), [1, 2, 0])
    # print(cframe_data.shape)
    return cframe_data

def get_video_free():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array


def openni_init():

    openni2.initialize("..\Redist")  # can also accept the path of the OpenNI redistribution
    dev = openni2.Device.open_any()
    print(dev.get_device_info())
    color_stream = dev.create_color_stream()
    color_stream.start()

    return color_stream


def boardi():
    board_1 = []

    for i in range(6):
        board_1.append([])
        for j in range(7):
            board_1[i].append(' ')

    return board_1


def center_k(frame, l, board_1):
    i, j = 0, 0
    y1 = 33
    tam = 30
    limit = tam * tam * 255 * 0.4

    for y in range(6):
        x1 = 25
        i = 0

        for x in range(7):
            s = frame[y1:y1 + tam, x1:x1 + tam]

            m = np.sum(s)
            if m > limit:
                if l == 0:
                    board_1[5 - j][6 - i] = 'x'
                else:
                    board_1[5 - j][6 - i] = 'o'

            x1 += 90
            i += 1

        y1 += 80
        j += 1

    return board_1


def maskin(dst, l, board_1):

#    GreenLower = np.array([49, 50, 55])
#    GreenUpper = np.array([107, 255, 255])
    GreenLower = np.array([58, 12, 5])
    GreenUpper = np.array([99, 255, 255])
#    YellLower = np.array([0, 100, 143])
#    YellUpper = np.array([26, 255, 255])
#    YellLower = np.array([0, 37, 185])
#    YellUpper = np.array([70, 255, 255])
#    YellLower = np.array([0, 91, 133])
#    YellUpper = np.array([130, 238, 255])
#    YellLower = np.array([10, 61, 189])
#    YellUpper = np.array([148, 255, 255])
    YellLower = np.array([0, 26, 176])#176])
    YellUpper = np.array([44, 255, 255])


    # mask=cv2.Canny(frame, 1, 900)
    kernel = np.ones((7, 7), np.uint8)
    kernel1 = np.ones((3, 3), np.uint8)
    hsv1 = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

    if l == 0:
        mask1 = cv2.inRange(hsv1, YellLower, YellUpper)
    else:
        mask1 = cv2.inRange(hsv1, GreenLower, GreenUpper)

    mask1 = cv2.erode(mask1, kernel1, iterations=1)
    # mask1 = cv2.dilate(mask1, None, iterations=2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel1)
    mask1 = cv2.dilate(mask1, kernel, iterations=7)
    # mask1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel)
    mask1 = cv2.erode(mask1, kernel, iterations=6)

    cv2.imshow("Frame_im" + str(l), mask1)

    return center_k(mask1, l, board_1)


def edges(frame):
    bufferSize = 4
    pts = deque(maxlen=bufferSize)

    MagLower = np.array([86, 109, 190])
    MagUpper = np.array([179, 255, 255])
    #MagLower = np.array([31, 164, 73])
    #MagUpper = np.array([179, 255, 255])

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # hsv[:, :, 2] -= 5
    mask = cv2.inRange(hsv, MagLower, MagUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    center = None
    if len(cnts) > 0:
        # Find the biggest area contour
        c = sorted(cnts, key=cv2.contourArea)
        # print(len(c))
        for h in range(len(c)):

            # Extract the circle that encloses the contour
            ((x, y), radius) = cv2.minEnclosingCircle(c[h])
            center = (int(x), int(y))
            pts.appendleft(np.float32(center))
            # 95x26

            # only proceed if the radius meets a minimum size

            if radius > 20:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

    return order_points(pts)


def vis(points, board_1, color_stream):
    frame = get_video(color_stream)
    #frame = get_video_free()

    pts2 = np.float32([[0, 0], [640, 0], [640, 480], [0, 480]])
    M = cv2.getPerspectiveTransform(np.float32(points), pts2)
    dst = cv2.warpPerspective(frame, M, (640, 480))

    cv2.imshow('otro', dst)
    cv2.imshow('image', frame)

    board_1 = maskin(dst, 0, board_1)
    board_1 = maskin(dst, 1, board_1)

    k = cv2.waitKey(5) & 0xFF

    #print(board_1)

    #if k == 27:
    #    cv2.destroyAllWindows()

    return board_1


def seriali():
    port = serial.Serial("COM4", 9600)
    time.sleep(1)
    port.write(b'0')
    port.close()


def main():
    """ Play a game!
    """
    board_1 = boardi()
    color_stream = openni_init()
    frame = get_video(color_stream)
    # frame = get_video_free()
    points = edges(frame)

    g = Game()
    g.printState()
    player1 = g.players[0]
    player2 = g.players[1]

    win_counts = [0, 0, 0]  # [p1 wins, p2 wins, ties]

    exit = False
    while not exit:
        while not g.finished:
            super_board = vis(points, board_1, color_stream)
            g.nextMove(super_board)

            k = cv2.waitKey(5) & 0xFF

            # print(board_1)

            if k == 27:
                cv2.destroyAllWindows()

        g.findFours()
        g.printState()

        if g.winner == None:
            win_counts[2] += 1

        elif g.winner == player1:
            win_counts[0] += 1

        elif g.winner == player2:
            win_counts[1] += 1

        printStats(player1, player2, win_counts)

        print("Thanks for playing!")
        exit = True


def printStats(player1, player2, win_counts):
    print("{0}: {1} wins, {2}: {3} wins, {4} ties".format(player1.name,
                                                          win_counts[0], player2.name, win_counts[1], win_counts[2]))


if __name__ == "__main__":  # Default "main method" idiom.
    main()
