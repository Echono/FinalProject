import sys
sys.path.insert(0, '..')
import unittest
import cv2 as cv
from sentimentaltools.sentimentalanalysis import sentimentalanalysis

class sentimentalanalysis_facial_recognition_test(unittest.TestCase):

    """Edit these two values to make use of the test. Goal is the amount of people on the picture, frame is the path to the picture"""
    goal = 1
    frame = cv.imread("testdata/test1.jpg", 0)
    
    def test(self):
        sentimentalanalysis_variable = sentimentalanalysis()
        result = sentimentalanalysis_variable.facial_recognition(self.frame)
        count = 0
        for id, detections in enumerate(result.detections):
            count = count + 1
        self.assertEqual(count, self.goal)

class sentimentalanalysis_facial_sentimental_analysis_test(unittest.TestCase):

    goal = "neutral"
    test_repeats = 10
    frame = cv.imread("testdata/test1.jpg", 0)

    def test(self):
        dominants = []
        sentimentalanalysis_variable = sentimentalanalysis()
        facial_recognition_result = sentimentalanalysis_variable.facial_recognition(self.frame)
        i = 0
        while i < 10:
            result = sentimentalanalysis_variable.facial_sentimental_analysis(self.frame, facial_recognition_result)
            dominants.append(result[0].get_dominant_emotion())
            i = i + 1
        self.assertEqual(dominants[0], self.goal)


if __name__ == '__main__':
    unittest.main()
    