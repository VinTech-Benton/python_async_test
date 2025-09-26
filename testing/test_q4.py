import asyncio
import unittest
from src.questions.q_4 import AsyncTimer


class TestQ4(unittest.TestCase):
    async def __test_async_timer(self):
        async with AsyncTimer() as timer:
            await asyncio.sleep(1)

        self.assertIsNotNone(timer.elapsed_second)

    def test_q4(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            loop.run_until_complete(self.__test_async_timer())
        except Exception:
            self.fail("AsyncTimer failed.")
        finally:
            loop.close()
