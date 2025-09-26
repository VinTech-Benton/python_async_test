import asyncio
import unittest
from src.questions.q_5 import stream_main


class TestQ5(unittest.TestCase):
    def test_q5(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            result = loop.run_until_complete(stream_main())
        except Exception:
            self.fail("async_main failed.")
        finally:
            loop.close()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        for res in result:
            self.assertIsInstance(res, str)
            self.assertIn("a_item", res)  # type: ignore
