import io
import sys 

class StandardOutput:
    def __enter__(self):
        self._original_stdout = sys.stdout 
        sys.stdout = io.StringIO()
        self.value = ''
        return self
    
    def __exit__(self, exception, error, traceback):
        self.value = sys.stdout.getvalue()
        sys.stdout = self._original_stdout         
        if exception is not None:
            raise exception
        return True
