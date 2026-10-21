import unittest
import pas2_text_concordance as api


class Tests(unittest.TestCase):
    def test_words_and_offsets(self):
        self.assertEqual(api.concordance("Cat cat! café"), {"cat": [0, 4], "café": [9]})

    def test_apostrophe_and_case(self):
        self.assertEqual(api.concordance("Don't DON'T"), {"don't": [0, 6]})
        self.assertEqual(list(api.concordance("A a", True)), ["A", "a"])

    def test_context(self):
        self.assertEqual(api.contexts("abcdef", [2], 1), ["bcd"])
        with self.assertRaises(ValueError):
            api.contexts("abc", [3])


if __name__ == "__main__":
    unittest.main()
