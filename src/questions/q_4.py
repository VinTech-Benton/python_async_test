import time


# Task 4: Implement async context manager
#
# - Goal: implement an asynchronous context manager named `AsyncTimer` that
#   measures wall-clock time for the block executed inside the async context.
# - Inputs: the context manager has no external inputs; it should record the
#   start time when entering the async context and record the end time when
#   exiting. Use `time.perf_counter()` for high-resolution timing.
# - Output: the context manager instance (returned from `__aenter__`) should
#   expose at least three attributes after exit:
#     - `start_time` (float): the perf_counter value recorded at enter
#     - `end_time` (float): the perf_counter value recorded at exit
#     - `elapsed_second` (float): the elapsed wall-clock seconds (end - start)
#   Additionally, `__aexit__` should print the elapsed time in seconds.
#
# Implementation hints:
# - Implement `async def __aenter__(self)` to record `self.start_time` with
#   `time.perf_counter()` and return `self`.
# - Implement `async def __aexit__(self, exc_type, exc, tb)` to record
#   `self.end_time`, compute `self.elapsed_second` by subtracting
#   `self.start_time` from `self.end_time`, and `print` the elapsed seconds.
# - Handle the case where `__aenter__` may not have been called (e.g., if an
#   implementation detail or user error skipped it) by treating a missing
#   `start_time` as `None` and avoiding a TypeError when computing elapsed time.
#
# Success criteria:
# - The context manager can be used as:
#     async with AsyncTimer() as t:
#         await some_async_work()
#   After the block, `t.start_time`, `t.end_time`, and `t.elapsed_second` are
#   populated and the elapsed time is printed.
# - Run `python -m unittest testing.test_q4` to validate your implementation.


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

        self.start_time = ...
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # TODO: implement __aexit__ method.
        #
        # HINT: use time.perf_counter() to get the current time
        # and calculate the elapsed time
        #
        # HINT: There is a possibility that __aenter__ was not called.
        # Bonus points if you handle this case by NOT raising an exception.

        self.end_time = ...
        self.elapsed_second = ...
        # TODO: print the elapsed time in seconds
        ...
