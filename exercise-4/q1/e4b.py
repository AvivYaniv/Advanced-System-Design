import shutil
import tempfile

class TemporaryDirectory:
    def __enter__(self):
        self.d = tempfile.mkdtemp()
        return self.d
    
    def __exit__(self, exception, error, traceback):
        shutil.rmtree(self.d) 
        if exception is not None:
            raise exception
        return True
