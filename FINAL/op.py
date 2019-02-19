from primesense import openni2
import numpy as np
import cv2


openni2.initialize(".\Redist")# can also accept the path of the OpenNI redistribution
dev = openni2.Device.open_any()
print(dev.get_device_info())
color_stream = dev.create_color_stream()
color_stream.start()

while True:
    cframe = color_stream.read_frame()
    cframe_data = np.array(cframe.get_buffer_as_triplet()).reshape([480, 640, 3])
    R = cframe_data[:, :, 0]
    G = cframe_data[:, :, 1]
    B = cframe_data[:, :, 2]
    cframe_data = np.transpose(np.array([B, G, R]), [1, 2, 0])
    # print(cframe_data.shape)
    cv2.imshow('color', cframe_data)

    key = cv2.waitKey(10)
    if int(key) == 113:
        break

color_stream.stop()
dev.close()
