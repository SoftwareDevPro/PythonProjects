
import cv2

class VideoCamera(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def __del__(self):
        self.capture.release()

    def get_frame(self):
        _, frame = self.capture.read()
        frame_flip = cv2.flip(frame, 1)
        _, frame = cv2.imencode(".jpg", frame_flip)
        return frame.tobytes()