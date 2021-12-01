import sys
sys.path.insert(0,'..')
import mediapipe as mp
import cv2 as cv
import logging
import numpy
from sentimentaltools.exceptions.sentimentalerrors import FrameNotAcceptable

class sentimentalanalysissuper():

    def __init__(self):
        pass

    @classmethod
    def confirm_input(self, frame):
        """
        Checks if the given frame to the library is an actual frame. If checks fails, an FrameNotAcceptable error will be raised.
        """
        check = False
        msg = ""
        if frame is not None:
            if type(frame).__module__ == numpy.__name__:
                check = True
            else:
                msg = f'The given frame: "{frame}" was not type of numpy which is the type opencv uses'
        else:
            msg = f'The given frame: "{frame}" was not a frame or not processable. Maybe you got the path wrong?'

        if not check:
            raise FrameNotAcceptable(msg)

    @classmethod
    def facial_recognition(self, frame):
        """
        Returns information depended on amount of faces detected in frame 
        """
        self.confirm_input(frame)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        detections = mp.solutions.face_detection.FaceDetection().process(frame)
        return detections