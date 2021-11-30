import sys
sys.path.insert(0,'..')
import mediapipe as mp
import cv2 as cv
import logging
from sentimentaltools.exceptions.sentimentalerrors import FrameNotAcceptable

class sentimentalanalysissuper():

    def __init__(self):
        pass

    @classmethod
    def confirm_input(self, frame):
        """
        A method designed to confirm the input is useable in the library.
        Designed to return a true or false depended on the anwser.
        """
        raise FrameNotAcceptable()
        pass

    @classmethod
    def facial_recognition(self, frame, frame_color = "BGR"):
        """
        Returns information depended on amount of faces detected in frame
        """
        try:
            self.confirm_input(frame)
        except FrameNotAcceptable as e:
            logging.error(e.to_string())
        if frame_color == "BGR":
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        detections = mp.solutions.face_detection.FaceDetection().process(frame)
        return detections