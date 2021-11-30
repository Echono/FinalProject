import os
from mediapipe import mediapipe as mp

class sentimentalanalysis:

    def __init__(self):
        pass

    @classmethod
    def confirm_input(self, frame):
        """
        A method designed to confirm the input is useable in the library.
        Designed to return a true or false depended on the anwser.
        """
        pass

    @classmethod
    def facial_recognition(self, frame):
        """
        A simple method to detect faces in the frame given.
        Returns a true or falce depended on if faces are detected,
        also returns number of faces detected.
        """
        pass

    @classmethod
    def facial_analysis(self, frame):
        """
        A method to analyze a given frame for people's emotions
        """
        pass