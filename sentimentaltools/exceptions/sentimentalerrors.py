class Error(Exception):
    """Base class for error handling"""
    pass

class FrameNotAcceptable(Error):
    """Frame could not be accepted by the verification process"""
    @classmethod
    def to_string(self, frame):
        return (f'The given frame: {frame}, was not suitable for authentication')
