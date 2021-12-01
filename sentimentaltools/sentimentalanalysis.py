import sys
sys.path.insert(0,'..')
import mediapipe as mp
from deepface import DeepFace as df
import cv2 as cv
from models import facialanalysismodel
from sentimentaltools.interfaces.sentimentalanalysissuper import sentimentalanalysissuper

class sentimentalanalysis(sentimentalanalysissuper):

    def __init__(self):
        super.__init__()
        self.mp_draw =  mp.solutions.mediapipe.python.solutions.drawing_utils

    @classmethod
    def facial_sentimental_analysis(self, frame, facial_recognition_results):
        """
        A method to analyze a given frame for people's emotions.  
        """
        analysis_results = list
        if facial_recognition_results.detections:
            for id, detection in facial_recognition_results.detections:
                new_analysis_object = facialanalysismodel
                facial_location = detection.location_data
                if facial_location.HasField('relative_bounding_box'):
                    frame_row, frame_col, _ = frame.shape
                    bounding_box = facial_location.relative_bounding_box
                    rect_start_point = self.mp_draw._normalized_to_pixel_coordinates(
                        bounding_box.xmin, bounding_box.ymin, frame_col, frame_row
                    )
                    rect_end_point = self.mp_draw._normalized_to_pixel_coordinates(
                        bounding_box.xmin + bounding_box.width, 
                        bounding_box.ymin + bounding_box.height,
                        frame_col, frame_row
                    )
                    if rect_start_point and rect_end_point:
                        rect_start_x, rect_start_y = rect_start_point
                        rect_end_x, rect_end_y = rect_end_point
                        cut_frame = frame[rect_start_x:rect_start_y, rect_end_x:rect_end_y]
                        emotions = df.analyze(cut_frame, actions=['emotion'], enforce_detection=False)
                        if emotions:
                            pass
