import asyncio
import unittest
from src.questions.q_3 import async_main


class TestQ3(unittest.TestCase):
    def test_q3(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            result = loop.run_until_complete(async_main())
        except Exception:
            self.fail("async_main failed.")
        finally:
            loop.close()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        for i, res in enumerate(result):
            if i == 2:
                self.assertIsInstance(res, ValueError)
            else:
                self.assertIsInstance(res, str)
                self.assertIn("Data from", res)  # type: ignore
