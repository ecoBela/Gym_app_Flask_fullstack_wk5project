from models.member import Member
from models.activity import Activity
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
activity_repository.delete_all()
booking_repository.delete_all()

member1 = Member("Bojo the Imbecile")
member_repository.save(member1)
member2 = Member("Pretty-unkind Patel")
member_repository.save(member2)
member3 = Member("Lyca Sturgeon")
member_repository.save(member3)
member4 = Member("Dumpy Truck")
member_repository.save(member4)

activity1 = Activity("Compassion Cultivator", True)
activity_repository.save(activity1)
activity2 = Activity("Empathy Stretcher", False)
activity_repository.save(activity2)
activity3 = Activity("Kundalini Kindness", True)
activity_repository.save(activity3)
activity4 = Activity("Political Punch Class", False)
activity_repository.save(activity4)

# activity_repository.select_all()

# member1 = Member("Bojo The Imbecile")
# member_repository.update(member1)

# activity1 = Activity("Compassion Crunches", False)
# activity_repository.update(activity1)

booking1 = Booking(member2, activity3)
booking_repository.save(booking1)

booking2 = Booking(member3, activity4)
booking_repository.save(booking2)

booking3 = Booking(member1, activity2)
booking_repository.save(booking3)

booking4 = Booking(member2, activity2)
booking_repository.save(booking4)

booking5 = Booking(member4, activity2)
booking_repository.save(booking5)

print(activity_repository.get_members(activity2))
