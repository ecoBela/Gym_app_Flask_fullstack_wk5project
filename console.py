from models.member import Member
from models.activity import Activity
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
activity_repository.delete_all()

member1 = Member("Bojo the Imbecile")
member_repository.save(member1)
member2 = Member("Pretty-unkind Patel")
member_repository.save(member2)

member1 = Member("Dumpy Truck")
member_repository.update(member1)

activity1 = Activity("Compassion Cultivator", True)
activity_repository.save(activity1)
activity2 = Activity("Empathy Stretcher", False)
activity_repository.save(activity2)
activity3 = Activity("Kundalini Kindness", True)
activity_repository.save(activity3)

activity_repository.select_all()

activity1 = Activity("Compassion Crunches", False)
activity_repository.update(activity1)

