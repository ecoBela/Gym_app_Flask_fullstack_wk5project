import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member1 = Member("IronMan")

    def test_member_has_name(self):
        self.assertEqual("IronMan", self.member1.name)

    def test_member_has_id(self):
        self.assertEqual(None, self.member1.id)