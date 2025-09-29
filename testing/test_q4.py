import asyncio
import unittest
from src.questions.q_4 import AsyncTimer


class TestQ4(unittest.TestCase):
    async def __test_async_timer(self):
        async with AsyncTimer() as timer:
            await asyncio.sleep(1)

        self.assertIsNotNone(timer.elapsed_second)

    async def __test_exit_without_enter(self):
        timer = AsyncTimer()
        # simulate exiting without having entered
        try:
            await timer.__aexit__(None, None, None)
            return True
        except Exception:
            return False

    def test_q4(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            loop.run_until_complete(self.__test_async_timer())
        except Exception:
            self.fail("AsyncTimer failed.")

        bonus_point = loop.run_until_complete(self.__test_exit_without_enter())

        if bonus_point:
            print("Bonus point get!")
        else:
            print("No bonus point.")

        loop.close()
