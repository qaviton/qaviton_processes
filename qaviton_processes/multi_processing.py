from multiprocessing import Process


class Task(Process):
    timeout = 0.01

    def __init__(self, *args, **kwargs):
        Process.__init__(self, *args, **kwargs)
        self.start()

    def in_progress(self, timeout=timeout):
        self.join(timeout=timeout)
        return self.is_alive()

    def is_finished(self, timeout=timeout):
        self.join(timeout=timeout)
        return not self.is_alive()

    def joinErr(self, timeout=timeout):
        if not self.is_finished(timeout=timeout):
            raise TimeoutError(f"process did not finish after {timeout}s")

    def joinTerminate(self, timeout=timeout):
        if not self.is_finished(timeout=timeout):
            self.terminate()
