class Error(Exception):
    """Base class for error handling"""
    pass

class FrameNotAcceptable(Error):
    """Frame could not be accepted by the verification process"""
    pass