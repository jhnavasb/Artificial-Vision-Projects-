import numpy as np
import cv2
from primesense import openni2

def nothing(x):
    pass

def get_video(color_stream):
    cframe = color_stream.read_frame()
    cframe_data = np.array(cframe.get_buffer_as_triplet()).reshape([480, 640, 3])
    R = cframe_data[:, :, 0]
    G = cframe_data[:, :, 1]
    B = cframe_data[:, :, 2]
    cframe_data = np.transpose(np.array([B, G, R]), [1, 2, 0])
    # print(cframe_data.shape)
    return cframe_data

cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

openni2.initialize(".\Redist")# can also accept the path of the OpenNI redistribution
dev = openni2.Device.open_any()
print(dev.get_device_info())
color_stream = dev.create_color_stream()
color_stream.start()

while True:
    #_, frame = cap.read(3)
    frame = get_video(color_stream)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    kernel = np.ones((5, 5), np.uint8)
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask1 = cv2.erode(mask, kernel, iterations=1)
    '''
    mask1 = cv2.erode(mask, kernel, iterations=1)
    # mask1 = cv2.dilate(mask1, None, iterations=2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
    mask1 = cv2.dilate(mask1, kernel, iterations=7)
    # mask1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel)
    mask1 = cv2.erode(mask1, kernel, iterations=6)
    '''

    result = cv2.bitwise_and(frame, frame, mask=mask1)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask1)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()