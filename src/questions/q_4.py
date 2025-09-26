import time


# Task 4: Implement async context manager
# Create an async context manager called 'AsyncTimer' that:
# - Starts a timer when entering
# - Prints the elapsed time when exiting
# - Without importing any external libraries (e.g., no 'contextlib' or 'timeit')


class AsyncTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_second = None

    async def __aenter__(self):
        # TODO: implement __aenter__ method.
        #
        # HINT: use time.perf_counter() to get the current time
        #

        ...
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # TODO: implement __aexit__ method.
        #
        # HINT: use time.perf_counter() to get the current time
        # and calculate the elapsed time
        #
        # HINT: There is a possibility that __aenter__ was not called.
        #       (Bonus points if you handle this case)
        #
        self.end_time = ...
        self.elapsed_second = ...
        # TODO: print the elapsed time in seconds
        ...
