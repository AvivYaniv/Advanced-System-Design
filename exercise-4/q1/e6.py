import contextlib

class ContextManager:
    def __init__(self, generator):
        self.generator = generator

    def __enter__(self):
        self.execution = self.generator()
        return next(self.execution)

    def __exit__(self, exception, error, traceback):
        with contextlib.suppress(StopIteration):
            if exception:
                self.execution.throw(exception, error, traceback)
            else:
                next(self.execution)
