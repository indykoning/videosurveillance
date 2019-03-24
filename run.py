#!/usr/bin/env python
import Camera
import cv2
import numpy as np

def saveFile(cam, jpeg):
    RGBImageNext = cv2.imdecode(np.fromstring(jpeg, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite('stream.jpg', RGBImageNext)


# camera = Camera.P2PCam("192.168.178.28", "192.168.178.9")
camera = Camera.P2PCam("10.42.0.1", "10.42.0.134")
camera.onJpegReceived = saveFile
camera.NB_FRAGMENTS_TO_ACCUMULATE = 20
camera.start()
