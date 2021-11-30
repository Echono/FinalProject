import os
import sys
sys.path.insert(0,'..')
import logging
from sentimentaltools.interfaces.sentimentalanalysissuper import sentimentalanalysissuper
from sentimentaltools.exceptions.sentimentalerrors import FrameNotAcceptable

class sentimentalanalysis(sentimentalanalysissuper):

    def __init__(self):
        super.__init__()

    @classmethod
    def facial_analysis(self, frame):
        """
        A method to analyze a given frame for people's emotions
        """
        pass
        
