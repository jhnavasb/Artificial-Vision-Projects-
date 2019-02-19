import numpy as np
import time
import cv2
import pyttsx3
from collections import Counter


def voice(seen):
    engine = pyttsx3.init()

    seen = dict(Counter(seen))
    keys = list(seen.keys())
    values = list(seen.values())

    text = "observo "
    for a in range(len(seen)):
        temp = str(values[a]) + keys[a]
        text += temp

    engine.say(text)
    engine.runAndWait()


def draw(id_boxes, boxes, confidences, classIDs, frame):
    labels = open("yolov3.names").read().strip().split("\n")

    np.random.seed(42)
    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
    seen = []

    for i in id_boxes.flatten():
        # extract the bounding box coordinates
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])

        # draw a bounding box rectangle and label on the image
        color = [int(c) for c in colors[classIDs[i]]]
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
        cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        seen.append(labels[classIDs[i]])

    voice(seen)

def get_LayerNames(net):
    layerNames = net.getLayerNames()
    return [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]


def selection(frame, layers, min_confidence, min_threshold):
    h, w, c = frame.shape

    boxes = []
    confidences = []
    classIDs = []

    # loop over each of the layer outputs
    for output in layers:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > min_confidence:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[0:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding
    # boxes
    id_boxes = cv2.dnn.NMSBoxes(boxes, confidences, min_confidence, min_threshold)
    if len(id_boxes) > 0:
        draw(id_boxes, boxes, confidences, classIDs, frame)


def main():
    min_confidence = 0.5
    min_threshold = 0.3

    net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    camera = cv2.VideoCapture(0)
    while True:
        _, frame = camera.read()
        #frame = cv2.imread("personas.jpg")

        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)

        layers = net.forward(get_LayerNames(net))
        selection(frame, layers, min_confidence, min_threshold)

        cv2.imshow('frame', frame)
        #time.sleep(4)

        k = cv2.waitKey(1)
        if k == 27:
            break

    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()