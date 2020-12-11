import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member1 = Member("IronMan")

    def test_member_has_name(self):
        self.assertEqual("IronMan", self.member1.name)