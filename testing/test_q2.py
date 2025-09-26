import asyncio
import unittest
from src.questions.q_2 import async_main


class TestQ2(unittest.TestCase):
    def test_async_main(self):
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
        for res in result:
            self.assertIsInstance(res, str)
            self.assertIn("Data from", res)  # type: ignore
