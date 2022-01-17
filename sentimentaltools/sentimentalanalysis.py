import sys
sys.path.insert(0, '..')
import mediapipe as mp
import cv2 as cv
from deepface import DeepFace as df
from sentimentaltools.models.facialanalysismodel import facial_analysis_model
from sentimentaltools.interfaces.sentimentalanalysissuper import sentimentalanalysissuper

class sentimentalanalysis(sentimentalanalysissuper):

    def __init__(self):
        self.mp_draw =  mp.solutions.mediapipe.python.solutions.drawing_utils

    def facial_sentimental_analysis(self, frame, facial_recognition_results):
        """
        A method to analyze a given frame for people's emotions.  
        """
        analysis_results = []
        colored_frame = cv.cvtColor(frame, cv.COLOR_GRAY2RGB)
        if facial_recognition_results.detections:
            for id, detection in enumerate(facial_recognition_results.detections):
                new_analysis_object = facial_analysis_model()
                facial_location = detection.location_data
                if facial_location.HasField('relative_bounding_box'):
                    frame_row, frame_col, _ = colored_frame.shape
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
                        cut_frame = colored_frame[rect_start_y:rect_end_y, rect_start_x:rect_end_x]
                        emotions = df.analyze(cut_frame, actions=['emotion'], enforce_detection=False)
                        if emotions:
                            new_analysis_object.set_related_bounding_box_id(id)
                            new_analysis_object.set_emotions(emotions)
                            new_analysis_object.set_dominant_emotion(emotions['dominant_emotion'])
                            new_analysis_object.set_location_data(facial_location)
                            new_analysis_object.set_related_frame(frame)
                            new_analysis_object.set_analyzed_frame(cut_frame)
                            analysis_results.append(new_analysis_object)
        return analysis_results