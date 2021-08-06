class ExceptionSilencer:

    def __init__(self, error_type):
        self.exc = error_type

    def __enter__(self):
        return self.exc

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.exc is exc_type
