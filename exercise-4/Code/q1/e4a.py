import os
import tempfile

class TemporaryFile:
    def __enter__(self):
        self.f, self.filename = tempfile.mkstemp()
        return self.f
    
    def __exit__(self, exception, error, traceback):
        os.close(self.f)
        if exception is not None:
            raise exception
        return True