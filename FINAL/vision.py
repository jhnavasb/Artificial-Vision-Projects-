from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
from primesense import openni2

'''
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array
'''

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

def get_video(color_stream):
    cframe = color_stream.read_frame()
    cframe_data = np.array(cframe.get_buffer_as_triplet()).reshape([480, 640, 3])
    R = cframe_data[:, :, 0]
    G = cframe_data[:, :, 1]
    B = cframe_data[:, :, 2]
    cframe_data = np.transpose(np.array([B, G, R]), [1, 2, 0])
    # print(cframe_data.shape)
    return cframe_data

openni2.initialize(".\Redist")# can also accept the path of the OpenNI redistribution
dev = openni2.Device.open_any()
print(dev.get_device_info())
color_stream = dev.create_color_stream()
color_stream.start()

def get_ball(frame , lower , upper , color):
    tanx = 10
    tany = 10
    anteriorx = 0
    anteriory = 0
    y1 = 33
    x1 = 44

    for x in range(7):

      for y in range(6):

            roi = frame[y1:y1+tany, x1:x1+tanx]
            #cv2.imshow("roi",roi)
            #cv2.waitKey(0)
            blurred = cv2.GaussianBlur(roi, (11, 11), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv, lower , upper)
            # Erode 2 times
            mask = cv2.erode(mask, None, iterations=2)
            # dilate 2 times
            mask = cv2.dilate(mask, None, iterations=2)
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            #anteriory = y * tany
            if len(cnts) > 0:
                c = sorted(cnts, key=cv2.contourArea)
                # print(len(c))
                for h in range(len(c)):

                    # Extract the circle that encloses the contour
                    ((x1, y1), radius) = cv2.minEnclosingCircle(c[h])
                    center = (int(x1), int(y1))
                    ##pts.appendleft(np.float32(center))
                    # 95x26

                    if radius > 10:

                      matrix[x][y]=color

#matrix_1 = np.zeros((6, 7), dtype=np.uint8)

board_1 = []

def board():
    for i in range(6):
        board_1.append([])
        for j in range(7):
            board_1[i].append(' ')


def center_k(frame, l):
    i, j = 0, 0
    y1 = 33
    tam = 30
    limit = tam * tam * 255 * 0.3

    for y in range(6):
        x1 = 25
        i = 0

        for x in range(7):
            s = frame[y1:y1 + tam, x1:x1 + tam]

            m = np.sum(s)
            #print(i, m, "coord:", x1, y1)

            #cv2.imshow("snap", s)
            #cv2.waitKey(0)

            if m > limit:
                if l == 0:
                    #matrix_1[j][i] = 1
                    board_1[j][i] = 'x'
                else:
                    #matrix_1[j][i] = 2
                    board_1[j][i] = 'o'

            x1 += 90
            i += 1

        y1 += 80
        j += 1

    #return matrix


GreenLower = np.array([49,50,55])
GreenUpper = np.array([107, 255, 255])
blueLower=np.array([73, 23, 80])
blueUpper=np.array([133, 201, 218])
MagLower=np.array([86, 109, 190])
MagUpper=np.array([179, 255, 255])
YellLower=np.array([0, 100, 143])
YellUpper=np.array([26, 255, 255])

bufferSize = 4
pts = deque(maxlen=bufferSize)
matrix = np.zeros( (7, 8) )

def maskin(dst, l):
    # mask=cv2.Canny(frame, 1, 900)
    kernel = np.ones((7, 7), np.uint8)
    kernel1 = np.ones((3, 3), np.uint8)
    hsv1 = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

    if l == 0:
        mask1 = cv2.inRange(hsv1, YellLower, YellUpper)
    else:
        mask1 = cv2.inRange(hsv1, GreenLower, GreenUpper)

    # mask1 = cv2.inRange(hsv1, GreenLower, GreenUpper)
    mask1 = cv2.erode(mask1, kernel1, iterations=1)
    # mask1 = cv2.dilate(mask1, None, iterations=2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel1)
    mask1 = cv2.dilate(mask1, kernel, iterations=7)
    # mask1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel)
    mask1 = cv2.erode(mask1, kernel, iterations=6)

    cv2.imshow("Frame_im" + str(l), mask1)

    center_k(mask1, l)


if __name__ == "__main__":
    board()
    while 1:
        # get a frame from RGB camera
        frame = get_video(color_stream)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        #hsv[:, :, 2] -= 5

        mask = cv2.inRange(hsv, MagLower, MagUpper)
        # Erode 2 times
        mask = cv2.erode(mask, None, iterations=2)
        # dilate 2 times
        mask = cv2.dilate(mask, None, iterations=2)
        '''
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]


        center = None
        if len(cnts) > 0:
            # Find the biggest area contour
            c = sorted(cnts, key=cv2.contourArea)
            #print(len(c))
            for h in range(len(c)):

            # Extract the circle that encloses the contour
             ((x, y), radius) = cv2.minEnclosingCircle(c[h])
             center = (int(x), int(y))
             pts.appendleft(np.float32(center))
             #95x26

            # only proceed if the radius meets a minimum size

             if radius > 20:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

        pts2 = np.float32([[0, 0], [640, 0],[640, 480], [0, 480] ])
        M = cv2.getPerspectiveTransform(np.float32(order_points(pts)), pts2)
        dst = cv2.warpPerspective(frame, M, (640, 480))

        ################################################### blue
        #get_ball(dst,blueLower,blueUpper,1)
        #print(matrix)
        cv2.imshow('otro', dst)
        ########################################################

            # Add the current center to the queue

        # Loop over the queue
        for i in range(1, len(pts)):
            # Ignore null points
            if pts[i - 1] is None or pts[i] is None:
                continue
            # Draw the line

        # show the frame to our screen


        #cv2.imshow("Frame", mask1)
        '''

        cv2.imshow("Frame2", mask)
        cv2.imshow('image', frame)

        #maskin(dst, 0)
        #maskin(dst, 1)

        # get a frame from depth sensor
        #depth = get_depth()
        # display RGB image

        # display depth image
        #cv2.imshow('Depth image', depth)

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF

        print(board_1)




        if k == 27:
            break
    cv2.destroyAllWindows()