import os
import sys
sys.path.insert(0,'..')
import cv2 as cv
import deepface as df
import mediapipe as mp
import exceptions.sentimentalerrors
from interfaces.sentimentalanalysisIF import sentimentalanalysisIF
from sentimentaltools.exceptions.sentimentalerrors import FrameNotAcceptable

class sentimentalanalysis(sentimentalanalysisIF):

    def __init__(self):
        super.__init__()

    @classmethod
    def facial_analysis(self, frame):
        """
        A method to analyze a given frame for people's emotions
        """
        pass

    @classmethod
    def facial_recognition_cut(self, frame, frame_color = "BGR"):
        """
        A simple method to detect faces in the frame given.
        Returns a true or falce depended on if faces are detected,
        also returns number of faces detected.
        """
        try:
            self.confirm_input(frame)
        except FrameNotAcceptable:
            pass
        if frame_color == "BGR":
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        detections = mp.solutions.face_detection.FaceDetection().process(frame)
        
