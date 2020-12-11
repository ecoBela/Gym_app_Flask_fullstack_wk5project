import unittest
from models.activity import Activity

class TestActivity(unittest.TestCase):
    def setUp(self):
        self.activity1 = Activity("Yoga", True)

    def test_activity_has_name(self):
        self.assertEqual("Yoga", self.activity1.name)

    def test_activity_has_id(self):
        self.assertEqual(None, self.activity1.id)