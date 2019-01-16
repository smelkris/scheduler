
import unittest
from Wakeup import *


class WakeupTest(unittest.TestCase):
    def setUp(self):
        self.model = WakeupModel("Preset.json")

    def test_default_title(self):
        self.assertEqual(self.model.title, '', 'Invalid default title')

    def test_default_tasklist(self):
        self.assertEqual(self.model.tasklist, None, 'Invalid default tasklist')

    def test_title(self):
        self.model.get_data()
        self.assertEqual(self.model.title, "Wakeup Time", 'Invalid title')

    def test_tasklist(self):
        self.model.get_data()
        self.assertEqual(len(self.model.tasklist), 3, 'Invalid tasklist size')

    def test_task(self):
        self.model.get_data()
        self.assertEqual(self.model.tasklist[1]['Task'], "Sleep", 'Invalid tasklist size')

    def test_duration(self):
        self.model.get_data()
        self.assertEqual(self.model.tasklist[1]['Duration'], 60, 'Invalid task duration')

    def test_missing_file_exception(self):
        test_passed = False
        try:
            new_model = WakeupModel("no_such_file.txt")
        except FileNotFoundError:
            test_passed = True

        self.assertEqual(test_passed, True, 'Expecting FileNotFound exception')

    def test_invalid_json_file(self):
        test_passed = False
        try:
            new_model = WakeupModel("Wakeup.py")
        except json.decoder.JSONDecodeError:
            test_passed = True

        self.assertEqual(test_passed, True, 'Expecting JSONDecodeError exception')


if __name__ == '__main__':
    unittest.main()
