
import os
import cv2
import mediapipe as mp
from multiprocessing import Pool
from deepface import DeepFace
from numpy import number


class main():
  mp_face_detection = mp.solutions.face_detection
  mp_drawing = mp.solutions.drawing_utils
  # For webcam input:
  def __init__(self):
    self.test()

  def test(self):
    NumberOfFrames = 0
    dominant_Emotion = ""

    cap = cv2.VideoCapture(0)
    with self.mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0.5) as face_detection:
      while cap.isOpened():
        success, image = cap.read()
        if not success:
          continue
        if cv2.waitKey(10) & 0xff==ord("q"):
          break    
        # To improve performance, optqionally mark the image as not writeable to
        # pass by reference.
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        # Draw the face detection annotations on the image.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cutFrame = image
        if results.detections:
          for detection in results.detections:
            NumberOfFrames += 1
            print(NumberOfFrames)
            self.mp_drawing.draw_detection(image, detection)
            for id, detection in enumerate(results.detections):
                  location = detection.location_data
                  if location.HasField('relative_bounding_box'):
                      frameRow, frameCol, _ = image.shape
                      bounding_box = location.relative_bounding_box
                      rectStartPoint = self.mp_drawing._normalized_to_pixel_coordinates(
                          bounding_box.xmin, bounding_box.ymin, frameCol, frameRow
                      )
                      rectEndPoint = self.mp_drawing._normalized_to_pixel_coordinates(
                          bounding_box.xmin + bounding_box.width, 
                          bounding_box.ymin + bounding_box.height,
                          frameCol, frameRow
                      )
                      if rectStartPoint and rectEndPoint:
                          rectStartX, rectStartY = rectStartPoint
                          rectEndX, rectEndY = rectEndPoint
                          if NumberOfFrames >= 10:
                            cutFrame = image[rectStartY:rectEndY, rectStartX:rectEndX]
                            dF = DeepFace.analyze(cutFrame, actions = ['emotion'],enforce_detection=False)
                            dominant_Emotion = dF['dominant_emotion']
                            cv2.imshow("id:2",cutFrame)
                            NumberOfFrames = 0
                            #cv2.putText(cutFrame,str(dominant_Emotion), (30, 30), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)
                          cv2.putText(image,str(dominant_Emotion), (70, 70), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)
        # Flip the image horizontally for a selfie-viewdisplay.
        cv2.imshow("id:1 " + 'test fuck head', image)
        if cv2.waitKey(5) & 0xFF == 27:
          break
    
if __name__ == "__main__":
    main()
