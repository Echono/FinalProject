import sys
sys.path.insert(0, '..')
import unittest
import cv2 as cv
from sentimentaltools.interfaces.sentimentalanalysissuper import sentimentalanalysissuper

class sentimentalanalysissuper_test(unittest.TestCase):

    """Edit these two values to make use of the test. Goal is the amount of people on the picture, frame is the path to the picture"""
    goal = 1
    frame = cv.imread("testdata/test1.jpg", 0)
    
    def test(self):
        sentimentalanalysissuper_variable = sentimentalanalysissuper()
        result = sentimentalanalysissuper_variable.facial_recognition(self.frame)
        count = 0
        for id, detections in enumerate(result.detections):
            count = count + 1
        self.assertEqual(count, self.goal)

if __name__ == '__main__':
    unittest.main()
        