import sys
sys.path.insert(0,'..')
from sentimentaltools.exceptions.sentimentalerrors import FrameNotAcceptable

class sentimentalanalysisIF():

    def __init__(self):
        pass

    @classmethod
    def confirm_input(self, frame):
        """
        A method designed to confirm the input is useable in the library.
        Designed to return a true or false depended on the anwser.
        """
        raise FrameNotAcceptable
        pass