import sys
sys.path.insert(0,'..')
import mediapipe as mp
import cv2 as cv
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
                if len(frame.shape) == 2:
                    check = True
                else:
                    msg = f'The given frame: "{frame}" was not the right amount of channels. Channels recieved: {len(frame.shape)}, accpted amount: 2. Make sure image is grayscaled'
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
        facial_recognition_results = mp.solutions.face_detection.FaceDetection().process(frame)
        return facial_recognition_results