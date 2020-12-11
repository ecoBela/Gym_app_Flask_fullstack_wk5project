import unittest
from models.booking import Booking
from models.member import Member
from models.activity import Activity

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.member1 = Member("Skye")
        self.activity1 = Activity("Yoga", True)
        self.booking1 = Booking(self.member1, self.activity1)
    
    def test_booking_has_member(self):
        self.assertEqual(self.member1, self.booking1.member)
    
    def test_booking_has_activity(self):
        self.assertEqual(self.activity1, self.booking1.activity)
    
    def test_booking_has_id(self):
        self.assertEqual(None, self.booking1.id)
    